import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")

# Load model
model = joblib.load("model/xgb_model.pkl")

# Daftar fitur input (selain Status/Status_num)
features = [
 'Marital_status', 'Application_mode', 'Application_order', 'Course',
 'Daytime_evening_attendance', 'Previous_qualification',
 'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
 'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
 'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
 'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_credited',
 'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations',
 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
 'Curricular_units_1st_sem_without_evaluations',
 'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
 'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
 'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
 'Unemployment_rate', 'Inflation_rate', 'GDP'
]

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

# Form input
input_data = {}
with st.form("dropout_form"):
    st.subheader("Masukkan Data Mahasiswa")
    for feature in features:
        input_data[feature] = st.number_input(f"{feature.replace('_', ' ')}", step=1.0)

    submit = st.form_submit_button("Prediksi")

# Prediksi
if submit:
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    label = ["Graduate", "Enrolled", "Dropout"][prediction]
    
    st.success(f"✅ Hasil Prediksi: **{label}**")