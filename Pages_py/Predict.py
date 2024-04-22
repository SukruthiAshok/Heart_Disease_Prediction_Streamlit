# import streamlit as st

# def main():
#     st.title("Heart Disease Prediction")

#     st.write("Please provide the following information:")

#     col1, col2 = st.columns(2)

#     with col1:
#         age = st.text_input("Age")

#         trestbps = st.text_input("Resting Blood Pressure (mm Hg)")

#         chol = st.text_input("Cholesterol (mg/dl)")

#         restecg = st.text_input("Resting Electrocardiographic Results (0-2)")

#         exang = st.text_input("Exercise Induced Angina (1=yes, 0=no)")

#         ca = st.text_input("Number of Major Vessels Colored by Flourosopy (0-3)")
#         thal = st.text_input("Thalassemia (0-3)")

#     with col2:
#         sex = st.text_input("Sex (Male=1, Female=0)")

#         cp = st.text_input("Chest Pain Type (0-3)")

#         fbs = st.text_input("Fasting Blood Sugar (> 120 mg/dl)")

#         thalach = st.text_input("Maximum Heart Rate Achieved")

#         oldpeak = st.text_input("ST Depression Induced by Exercise")

#         slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)")

#     predict_btn= st.button("Predict")
#     if predict_btn:
#         # Call your prediction function with the collected data
#         prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
#         st.write("Prediction:", prediction)

# def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
#     # Placeholder function for prediction
#     # Implement your prediction logic here (e.g., using a machine learning model)
#     # Return the prediction result
#     return "Positive"  # Placeholder result

# if __name__ == "__main__":
#     main()


import streamlit as st
import joblib
import numpy as np
import datetime
from session_state import SessionState

def load_model():
    # Load the trained model
    with open('ensemble_model.pkl', 'rb') as model_file:
        model = joblib.load(model_file)
    return model

def load_scaler():
    # Load the scaler
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = joblib.load(scaler_file)
    return scaler

def insert_user_data(userid, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Insert data into the user_data table
    sql = "INSERT INTO user_data (userid, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (userid, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target, timestamp)
    cursor.execute(sql, data)
    connection.commit()

def predict():
    st.title("Heart Disease Prediction")
    st.write("Please provide the following information:")

    age = st.text_input("Age")
    sex = st.text_input("Sex (Male=1, Female=0)")
    cp = st.text_input("Chest Pain Type (0-3)")
    trestbps = st.text_input("Resting Blood Pressure (mm Hg)")
    chol = st.text_input("Cholesterol (mg/dl)")
    fbs = st.text_input("Fasting Blood Sugar (> 120 mg/dl)")
    restecg = st.text_input("Resting Electrocardiographic Results (0-2)")
    thalach = st.text_input("Maximum Heart Rate Achieved")
    exang = st.text_input("Exercise Induced Angina (1=yes, 0=no)")
    oldpeak = st.text_input("ST Depression Induced by Exercise")
    slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)")
    ca = st.text_input("Number of Major Vessels Colored by Flourosopy (0-3)")
    thal = st.text_input("Thalassemia (0-3)")
    prediction=0

    predict_btn= st.button("Predict")
    if predict_btn:
        # Call the function to load the model and scaler
        model = load_model()
        scaler = load_scaler()
        # Transform input data
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]], dtype=float)
        input_data = scaler.transform(input_data)
        # Make prediction
        prediction = model.predict(input_data)
        if prediction[0] == 0:
            st.write("Prediction: Negative (No Heart Disease)")
        else:
            st.write("Prediction: Positive (Heart Disease Detected)")

        session_state = SessionState.get()
        userid = session_state.userid
        insert_user_data(userid, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction[0])
# if __name__ == "__main__":
#     main()
