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
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Split the training data into features (X) and target variable (y)
X_train = train_data.drop("target", axis=1)
y_train = train_data["target"]

# Split the testing data into features (X) and target variable (y)
X_test = test_data.drop("target", axis=1)
y_test = test_data["target"]

# Scale the input features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the individual classification models with regularization
xgboost = XGBClassifier()
logistic_regression = LogisticRegression()

# Initialize the ensemble model using voting classifier
ensemble = VotingClassifier(
    estimators=[('xgb', xgboost), ('lr', logistic_regression)],
    voting='soft'  # Change to 'soft' if you want to enable soft voting
)

# Train the ensemble model
ensemble.fit(X_train_scaled, y_train)

# Save the scaler object and the ensemble model
joblib.dump(scaler, "scaler.pkl")
joblib.dump(ensemble, "ensemble_model.pkl")

# Load the trained ensemble model
ensemble_model = joblib.load("ensemble_model.pkl")

# Evaluate the performance of the model on the test data
accuracy = accuracy_score(y_test, ensemble_model.predict(X_test_scaled))
precision = precision_score(y_test, ensemble_model.predict(X_test_scaled), average='weighted')
recall = recall_score(y_test, ensemble_model.predict(X_test_scaled), average='weighted')
f1 = f1_score(y_test, ensemble_model.predict(X_test_scaled), average='weighted')

# Display the evaluation metrics
print("Evaluation Metrics:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Perform cross-validation
cv_scores = cross_val_score(ensemble_model, X_train_scaled, y_train, cv=5)  # 5-fold cross-validation
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))

# Evaluate the performance of the model on the training data
train_accuracy = accuracy_score(y_train, ensemble_model.predict(X_train_scaled))

# Display the training accuracy
print("Training Accuracy:", train_accuracy)

# Display the testing accuracy
print("Testing Accuracy:", accuracy)
