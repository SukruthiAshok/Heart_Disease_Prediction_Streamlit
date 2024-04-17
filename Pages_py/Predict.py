import streamlit as st

def main():
    st.title("Heart Disease Prediction")

    st.write("Please provide the following information:")

    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input("Age")

        trestbps = st.text_input("Resting Blood Pressure (mm Hg)")

        chol = st.text_input("Cholesterol (mg/dl)")

        restecg = st.text_input("Resting Electrocardiographic Results (0-2)")

        exang = st.text_input("Exercise Induced Angina (1=yes, 0=no)")

        ca = st.text_input("Number of Major Vessels Colored by Flourosopy (0-3)")
        thal = st.text_input("Thalassemia (0-3)")

    with col2:
        sex = st.text_input("Sex (Male=1, Female=0)")

        cp = st.text_input("Chest Pain Type (0-3)")

        fbs = st.text_input("Fasting Blood Sugar (> 120 mg/dl)")

        thalach = st.text_input("Maximum Heart Rate Achieved")

        oldpeak = st.text_input("ST Depression Induced by Exercise")

        slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)")

    predict_btn= st.button("Predict")
    if predict_btn:
        # Call your prediction function with the collected data
        prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        st.write("Prediction:", prediction)

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Placeholder function for prediction
    # Implement your prediction logic here (e.g., using a machine learning model)
    # Return the prediction result
    return "Positive"  # Placeholder result

if __name__ == "__main__":
    main()
