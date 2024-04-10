import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

np.set_printoptions(threshold=np.inf)

# Load the training data
data = pd.read_csv("combined_dataset.csv")

# Split the data into features (X) and target variable (y)
X = data.drop("target", axis=1)
y = data["target"]

# Scale the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Split the training data further into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Initialize the individual classification models with regularization
random_forest = RandomForestClassifier(max_features='sqrt', min_samples_leaf=5)
xgboost = XGBClassifier()
logistic_regression = LogisticRegression()

# Initialize the ensemble model using voting classifier
ensemble = VotingClassifier(
    estimators=[('rf', random_forest), ('xgb', xgboost), ('lr', logistic_regression)],
    voting='soft'  # Change to 'soft' if you want to enable soft voting
)

# Train the ensemble model
ensemble.fit(X_train, y_train)

# Save the scaler object and the ensemble model
joblib.dump(scaler, "scaler.pkl")
joblib.dump(ensemble, "ensemble_model.pkl")

# Load the trained ensemble model
ensemble_model = joblib.load("ensemble_model.pkl")

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, ensemble_model.predict(X_test))
precision = precision_score(y_test, ensemble_model.predict(X_test), average='weighted')
recall = recall_score(y_test, ensemble_model.predict(X_test), average='weighted')
f1 = f1_score(y_test, ensemble_model.predict(X_test), average='weighted')

# Display the evaluation metrics
print("Evaluation Metrics:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Perform validation
val_accuracy = accuracy_score(y_val, ensemble_model.predict(X_val))
print("Validation Accuracy:", val_accuracy)

# Perform cross-validation
cv_scores = cross_val_score(ensemble_model, X_train, y_train, cv=5)  # 5-fold cross-validation
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))

# Evaluate the performance of the model on the training data
train_accuracy = accuracy_score(y_train, ensemble_model.predict(X_train))

# Evaluate the performance of the model on the test data
test_accuracy = accuracy_score(y_test, ensemble_model.predict(X_test))

# Display the accuracy scores
print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)
