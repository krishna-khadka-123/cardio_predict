from models import cardio_predict
import pandas as pd
import streamlit as st
features, target, X, Y, scaler, model, Y_pred, cr, cm = cardio_predict()

st.header('Cardiovascular Disease Prediction System')
st.subheader('Using Logistic Regression')

st.sidebar.header('Features')

# Features => 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active'

age = st.sidebar.slider(
    'Age',
    min_value=25,
    max_value=70,
    value=30,
    step=1
)

gender = st.sidebar.selectbox(
    'Gender',
    ['Female', 'Male']
)

gender = 1 if gender == 'Female' else 2

height = st.sidebar.slider(
    'Height (cm)',
    min_value=50,
    max_value=255,
    value=170,
    step=1
)

weight = st.sidebar.slider(
    'Weight (kg)',
    min_value=20,
    max_value=150,
    value=70,
    step=1
)

ap_hi=st.sidebar.slider(
  'Systolic Blood Pressure',
  max_value=190,
  min_value=100,
  value=120,
  step=1
)

ap_lo = st.sidebar.slider(
    'Diastolic Blood Pressure',
    min_value=50,
    max_value=99,
    value=60,
    step=1
)

cholesterol = st.sidebar.radio(
    'Cholesterol Level',
    (1, 2, 3),
    format_func=lambda x: {
        1: 'Normal',
        2: 'Above Normal',
        3: 'Well Above Normal'
    }[x]
)
###############################################################################################
# Glucose Level
gluc = st.sidebar.radio(
    'Glucose  Level',
    (1, 2, 3),
    format_func=lambda x: {
        1: 'Normal',
        2: 'Above Normal',
        3: 'Well Above Normal'
    }[x]
)
# Smoking
smoke = st.sidebar.radio(
    'smoke?',
    (0, 1),
    format_func=lambda x: 'No' if x == 0 else 'Yes'
)

# Alcohol Consumption
alco = st.sidebar.radio(
    'alcohol consume?',
    (0, 1),
    format_func=lambda x: 'No' if x == 0 else 'Yes'
)

# Physical Activity
active = st.sidebar.radio(
    'physically active?',
    (0, 1),
    format_func=lambda x: 'No' if x == 0 else 'Yes'
)

# st.write("Age:", age)
# st.write("Gender:", gender)
# st.write("Height:", height)
# st.write("Weight:", weight)
# st.write("Systolic BP (ap_hi):", ap_hi)
# st.write("Diastolic BP (ap_lo):", ap_lo)
# st.write("Cholesterol:", cholesterol)
# st.write("Glucose:", gluc)
# st.write("Smoking:", smoke)
# st.write("Alcohol Consumption:", alco)
# st.write("Physical Activity:", active)

# Prediction 
if st.button('predict cardio Disease'):
    with st.spinner('predicting cardio...'):   # FIX: spinner now wraps the full prediction block
        input_data = pd.DataFrame(
            [[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]],
            columns=features
        )
        input_scaler = scaler.transform(input_data)
        prediction = model.predict(input_scaler)

        if prediction == 0:
            st.write('NO Cardiovascular_Disease found!')
            st.success('person is likely to be healthy')
        else:
            st.write('Cardiovascular_Disease found!')
            st.error('person is likely to be Unhealthy')