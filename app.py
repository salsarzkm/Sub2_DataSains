import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")

model = joblib.load("model/xgb_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

# Form input
with st.form("dropout_form"):
    st.subheader("Masukkan Data Mahasiswa")

    input_data = {}

    # KATEGORIKAL: Selectbox dengan label
    input_data["Marital_status"] = st.selectbox("Status Pernikahan", {
        1: "Lajang", 2: "Menikah", 3: "Duda/Janda", 4: "Cerai", 5: "Kumpul kebo", 6: "Pisah hukum"
    }.keys(), format_func=lambda x: {
        1: "Lajang", 2: "Menikah", 3: "Duda/Janda", 4: "Cerai", 5: "Kumpul kebo", 6: "Pisah hukum"
    }[x])

    input_data["Application_mode"] = st.selectbox("Metode Pendaftaran", list(range(1, 18)))  # aslinya bisa disesuaikan

    input_data["Application_order"] = st.slider("Urutan Pilihan Jurusan (0=1st choice, 9=last)", 0, 9)

    input_data["Course"] = st.selectbox("Program Studi", list(range(1, 17)))  # jika kamu punya mapping real, bisa diganti

    input_data["Daytime_evening_attendance"] = st.radio("Waktu Kuliah", [1, 0], format_func=lambda x: "Siang" if x == 1 else "Malam")

    input_data["Previous_qualification"] = st.selectbox("Pendidikan Sebelumnya", list(range(1, 20)))

    input_data["Previous_qualification_grade"] = st.number_input("Nilai Pendidikan Sebelumnya (0–200)", 0.0, 200.0, step=1.0)

    input_data["Nacionality"] = st.selectbox("Kewarganegaraan", [1, 2, 6, 10, 12, 14, 17])  # disesuaikan lagi

    input_data["Mothers_qualification"] = st.selectbox("Pendidikan Ibu", list(range(1, 19)))
    input_data["Fathers_qualification"] = st.selectbox("Pendidikan Ayah", list(range(1, 19)))

    input_data["Mothers_occupation"] = st.selectbox("Pekerjaan Ibu", list(range(0, 11)))
    input_data["Fathers_occupation"] = st.selectbox("Pekerjaan Ayah", list(range(0, 11)))

    input_data["Admission_grade"] = st.number_input("Nilai Masuk (0–200)", 0.0, 200.0, step=1.0)

    # Binary features (0/1)
    for bcol, label in {
        "Displaced": "Berasal dari luar daerah?",
        "Educational_special_needs": "Kebutuhan Khusus?",
        "Debtor": "Memiliki Tunggakan?",
        "Tuition_fees_up_to_date": "Pembayaran Kuliah Lunas?",
        "Gender": "Jenis Kelamin",
        "Scholarship_holder": "Penerima Beasiswa?",
        "International": "Mahasiswa Internasional?"
    }.items():
        input_data[bcol] = st.radio(label, [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")

    input_data["Age_at_enrollment"] = st.number_input("Usia saat Masuk Kuliah", 15, 70)

    # Data perkuliahan (numerik)
    num_fields = [
        "Curricular_units_1st_sem_credited", "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_evaluations", "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade", "Curricular_units_1st_sem_without_evaluations",
        "Curricular_units_2nd_sem_credited", "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_evaluations", "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade", "Curricular_units_2nd_sem_without_evaluations",
        "Unemployment_rate", "Inflation_rate", "GDP"
    ]

    for col in num_fields:
        input_data[col] = st.number_input(col.replace("_", " ").title(), step=1.0)

    submit = st.form_submit_button("Prediksi")

# Prediksi
if submit:
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    label = ["Graduate", "Enrolled", "Dropout"][prediction]
    st.success(f"✅ Hasil Prediksi: **{label}**")
