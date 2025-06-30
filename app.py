import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")

# Load model pipeline
model = joblib.load("model/xgb_pipeline.pkl")
feature_order = model.input_features  # urutan fitur sesuai model

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

# Mapping pilihan deskriptif
marital_status_options = {
    1: "1 – Single",
    2: "2 – Married",
    3: "3 – Widower",
    4: "4 – Divorced",
    5: "5 – Facto union",
    6: "6 – Legally separated"
}

application_mode_options = {
    1: "1 - 1st phase - general contingent",
    2: "2 - Ordinance No. 612/93",
    5: "5 - 1st phase - special contingent (Azores Island)",
    7: "7 - Holders of other higher courses",
    10: "10 - Ordinance No. 854-B/99",
    15: "15 - International student (bachelor)",
    16: "16 - 1st phase - special contingent (Madeira Island)",
    17: "17 - 2nd phase - general contingent",
    18: "18 - 3rd phase - general contingent",
    26: "26 - Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "27 - Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "39 - Over 23 years old",
    42: "42 - Transfer",
    43: "43 - Change of course",
    44: "44 - Technological specialization diploma holders",
    51: "51 - Change of institution/course",
    53: "53 - Short cycle diploma holders",
    57: "57 - Change of institution/course (International)"
}

course_options = {
    33: "33 - Biofuel Production Technologies",
    171: "171 - Animation and Multimedia Design",
    8014: "8014 - Social Service (evening attendance)",
    9003: "9003 - Agronomy",
    9070: "9070 - Communication Design",
    9085: "9085 - Veterinary Nursing",
    9119: "9119 - Informatics Engineering",
    9130: "9130 - Equinculture",
    9147: "9147 - Management",
    9238: "9238 - Social Service",
    9254: "9254 - Tourism",
    9500: "9500 - Nursing",
    9556: "9556 - Oral Hygiene",
    9670: "9670 - Advertising and Marketing Management",
    9773: "9773 - Journalism and Communication",
    9853: "9853 - Basic Education",
    9991: "9991 - Management (evening attendance)"
}

mothers_occupation_options = {
    0: "0 – Student",
    1: "1 – Legislative/Executive Rep, Director/Manager",
    2: "2 – Intellectual/Scientific Specialist",
    3: "3 – Intermediate Level Technician/Profession",
    4: "4 – Administrative staff",
    5: "5 – Services, Security, Sellers",
    6: "6 – Farmers, Skilled Agriculture/Fishery",
    7: "7 – Skilled Industry/Construction/Crafts",
    8: "8 – Machine Operators/Assemblers",
    9: "9 – Unskilled Workers",
    10: "10 – Armed Forces",
    90: "90 – Other Situation",
    99: "99 – Blank/Unknown",
    122: "122 – Health Professionals",
    123: "123 – Teachers",
    125: "125 – ICT Specialists",
    131: "131 – Mid-level Science/Engineering Tech",
    132: "132 – Mid-level Health Technicians",
    134: "134 – Mid-level Legal/Social/Culture Services",
    141: "141 – Office Workers/Data Operators",
    143: "143 – Accounting/Finance/Registry Operators",
    144: "144 – Other Admin Support",
    151: "151 – Personal Service Workers",
    152: "152 – Sellers",
    153: "153 – Personal Care Workers",
    171: "171 – Skilled Construction Workers",
    173: "173 – Printing/Precision/Jewelry/Artisans",
    175: "175 – Food/Wood/Clothing/Crafts Industry",
    191: "191 – Cleaning Workers",
    192: "192 – Unskilled Agriculture/Fishery",
    193: "193 – Unskilled Industry/Transport",
    194: "194 – Meal Preparation Assistants"
}

fathers_occupation_options = {
    0: "0 – Student",
    1: "1 – Legislative/Executive Roles, Directors",
    2: "2 – Intellectual & Scientific Specialists",
    3: "3 – Intermediate Technicians/Professions",
    4: "4 – Administrative Staff",
    5: "5 – Services, Security, Sellers",
    6: "6 – Farmers, Agriculture Workers",
    7: "7 – Skilled Workers (Industry/Construction)",
    8: "8 – Machine Operators & Assemblers",
    9: "9 – Unskilled Workers",
    10: "10 – Armed Forces Professions",
    90: "90 – Other Situation",
    99: "99 – (Blank)",
    101: "101 – Armed Forces Officers",
    102: "102 – Armed Forces Sergeants",
    103: "103 – Other Armed Forces Personnel",
    112: "112 – Admin/Commercial Directors",
    114: "114 – Hotel/Trade/Service Directors",
    121: "121 – Physical Sciences Specialists",
    122: "122 – Health Professionals",
    123: "123 – Teachers",
    124: "124 – Finance/Admin/Relations Specialists",
    131: "131 – Mid-Level Science Technicians",
    132: "132 – Mid-Level Health Technicians",
    134: "134 – Mid-Level Legal/Cultural Technicians",
    135: "135 – ICT Technicians",
    141: "141 – Secretaries/Data Processing",
    143: "143 – Accounting/Stats/Finance Clerks",
    144: "144 – Other Admin Support Staff",
    151: "151 – Personal Service Workers",
    152: "152 – Sellers",
    153: "153 – Personal Care Workers",
    154: "154 – Security Services Personnel",
    161: "161 – Market-Oriented Farmers",
    163: "163 – Subsistence Farmers/Fishermen",
    171: "171 – Skilled Construction Workers",
    172: "172 – Metal Workers",
    174: "174 – Electricians/Electronics Workers",
    175: "175 – Food/Textile/Wood Workers",
    181: "181 – Fixed Plant Operators",
    182: "182 – Assembly Workers",
    183: "183 – Drivers/Mobile Equipment Operators",
    192: "192 – Unskilled Agri/Fish/Forest Workers",
    193: "193 – Unskilled Industry/Transport Workers",
    194: "194 – Meal Preparation Assistants",
    195: "195 – Street Vendors/Service Providers"
}

fathers_qualification_options = {
    1: "1 – Secondary Education - 12th Year",
    2: "2 – Bachelor's Degree",
    3: "3 – Higher Education - Degree",
    4: "4 – Master's",
    5: "5 – Doctorate",
    6: "6 – Frequency of Higher Education",
    9: "9 – 12th Year - Not Completed",
    10: "10 – 11th Year - Not Completed",
    11: "11 – 7th Year (Old)",
    12: "12 – Other - 11th Year",
    13: "13 – 2nd Year Complementary HS",
    14: "14 – 10th Year",
    18: "18 – General Commerce Course",
    19: "19 – Basic Ed. 3rd Cycle (9th-11th)",
    20: "20 – Complementary HS Course",
    22: "22 – Technical-professional Course",
    25: "25 – Complementary HS - Not Concluded",
    26: "26 – 7th Year",
    27: "27 – 2nd Cycle Gen. HS Course",
    29: "29 – 9th Year - Not Completed",
    30: "30 – 8th Year",
    31: "31 – Admin & Commerce Course",
    33: "33 – Supplementary Accounting",
    34: "34 – Unknown",
    35: "35 – Can't Read or Write",
    36: "36 – Can Read, No 4th Year",
    37: "37 – Basic Ed. 1st Cycle (4th/5th)",
    38: "38 – Basic Ed. 2nd Cycle (6th-8th)",
    39: "39 – Technological Specialization",
    40: "40 – Higher Ed. - Degree (1st Cycle)",
    41: "41 – Specialized Higher Studies",
    42: "42 – Professional Higher Technical",
    43: "43 – Master's (2nd Cycle)",
    44: "44 – Doctorate (3rd Cycle)"
}

mothers_qualification_options = {
    1: "1 – Secondary Education - 12th Year of Schooling or Eq.",
    2: "2 – Higher Education - Bachelor's Degree",
    3: "3 – Higher Education - Degree",
    4: "4 – Higher Education - Master's",
    5: "5 – Higher Education - Doctorate",
    6: "6 – Frequency of Higher Education",
    9: "9 – 12th Year of Schooling - Not Completed",
    10: "10 – 11th Year of Schooling - Not Completed",
    11: "11 – 7th Year (Old)",
    12: "12 – Other - 11th Year of Schooling",
    14: "14 – 10th Year of Schooling",
    18: "18 – General commerce course",
    19: "19 – Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "22 – Technical-professional course",
    26: "26 – 7th year of schooling",
    27: "27 – 2nd cycle of the general high school course",
    29: "29 – 9th Year of Schooling - Not Completed",
    30: "30 – 8th year of schooling",
    34: "34 – Unknown",
    35: "35 – Can't read or write",
    36: "36 – Can read without having a 4th year of schooling",
    37: "37 – Basic education 1st cycle (4th/5th year) or equiv.",
    38: "38 – Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "39 – Technological specialization course",
    40: "40 – Higher education - degree (1st cycle)",
    41: "41 – Specialized higher studies course",
    42: "42 – Professional higher technical course",
    43: "43 – Higher Education - Master (2nd cycle)",
    44: "44 – Higher Education - Doctorate (3rd cycle)"
}

nacionality_options = {
    1: "1 – Portuguese",
    2: "2 – German",
    6: "6 – Spanish",
    10: "10 – Italian",
    12: "12 – Dutch",
    14: "14 – English",
    17: "17 – Lithuanian",
    21: "21 – Angolan",
    22: "22 – Cape Verdean",
    24: "24 – Guinean",
    25: "25 – Mozambican",
    26: "26 – Santomean",
    32: "32 – Turkish",
    41: "41 – Brazilian",
    62: "62 – Romanian",
    100: "100 – Moldova (Republic of)",
    101: "101 – Mexican",
    103: "103 – Ukrainian",
    105: "105 – Russian",
    108: "108 – Cuban",
    109: "109 – Colombian"
}

previous_qualification_options = {
    1: "1 – Secondary education",
    2: "2 – Higher education - bachelor's degree",
    3: "3 – Higher education - degree",
    4: "4 – Higher education - master's",
    5: "5 – Higher education - doctorate",
    6: "6 – Frequency of higher education",
    9: "9 – 12th year of schooling - not completed",
    10: "10 – 11th year of schooling - not completed",
    12: "12 – Other - 11th year of schooling",
    14: "14 – 10th year of schooling",
    15: "15 – 10th year of schooling - not completed",
    19: "19 – Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "38 – Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "39 – Technological specialization course",
    40: "40 – Higher education - degree (1st cycle)",
    42: "42 – Professional higher technical course",
    43: "43 – Higher education - master (2nd cycle)"
}

with st.form("dropout_form"):
    st.subheader("Masukkan Data Mahasiswa")

    input_data = {}

    input_data["Marital_status"] = st.selectbox(
        "Status Pernikahan",
        options=marital_status_options.keys(),
        format_func=lambda x: marital_status_options[x],
        help="Status pernikahan mahasiswa."
    )

    input_data["Application_mode"] = st.selectbox(
        "Metode Pendaftaran",
        options=application_mode_options.keys(),
        format_func=lambda x: application_mode_options[x],
        help="Metode pendaftaran yang digunakan mahasiswa."
    )

    input_data["Course"] = st.selectbox(
        "Program Studi",
        options=course_options.keys(),
        format_func=lambda x: course_options[x],
        help="Program studi yang diambil."
    )

    input_data["Application_order"] = st.slider(
        "Urutan Pilihan Jurusan",
        0, 9,
        help="0 = pilihan pertama, 9 = pilihan terakhir"
    )

    input_data["Daytime_evening_attendance"] = st.radio(
        "Waktu Kuliah",
        [1, 0],
        format_func=lambda x: "Siang" if x == 1 else "Malam",
        help="1 – siang, 0 – malam"
    )

    input_data["Previous_qualification"] = st.selectbox(
        "Pendidikan Sebelumnya",
        options=previous_qualification_options.keys(),
        format_func=lambda x: previous_qualification_options[x],
        help="Tingkat pendidikan sebelum kuliah."
    )

    input_data["Previous_qualification_grade"] = st.number_input(
        "Nilai Pendidikan Sebelumnya",
        0.0, 200.0, step=1.0,
        help="Nilai dari pendidikan terakhir sebelum kuliah (0–200)"
    )

    input_data["Nacionality"] = st.selectbox(
        "Kewarganegaraan",
        options=nacionality_options.keys(),
        format_func=lambda x: nacionality_options[x],
        help="Pilih kewarganegaraan mahasiswa berdasarkan kode dan negara asal."
    )

    input_data["Mothers_qualification"] = st.selectbox(
        "Pendidikan Ibu",
        options=mothers_qualification_options.keys(),
        format_func=lambda x: mothers_qualification_options[x],
        help="Pilih tingkat pendidikan terakhir ibu mahasiswa."
    )

    input_data["Fathers_qualification"] = st.selectbox(
        "Pendidikan Ayah",
        options=fathers_qualification_options.keys(),
        format_func=lambda x: fathers_qualification_options[x],
        help="Pilih tingkat pendidikan terakhir ayah mahasiswa."
    )

    input_data["Mothers_occupation"] = st.selectbox(
        "Pekerjaan Ibu",
        options=mothers_occupation_options.keys(),
        format_func=lambda x: mothers_occupation_options[x],
        help="Pekerjaan ibu mahasiswa."
    )

    input_data["Fathers_occupation"] = st.selectbox(
        "Pekerjaan Ayah",
        options=fathers_occupation_options.keys(),
        format_func=lambda x: fathers_occupation_options[x],
        help="Pilih pekerjaan ayah berdasarkan deskripsi jabatan."
    )   

    input_data["Admission_grade"] = st.number_input(
        "Nilai Masuk",
        0.0, 200.0, step=1.0,
        help="Nilai saat diterima di perguruan tinggi (0–200)"
    )

    for bcol, label, tooltip in [
        ("Displaced", "Berasal dari Luar Daerah?", "1 – ya, 0 – tidak"),
        ("Educational_special_needs", "Kebutuhan Khusus?", "1 – ya, 0 – tidak"),
        ("Debtor", "Memiliki Tunggakan?", "1 – ya, 0 – tidak"),
        ("Tuition_fees_up_to_date", "Pembayaran Kuliah Lunas?", "1 – ya, 0 – tidak"),
        ("Gender", "Jenis Kelamin", "1 – laki-laki, 0 – perempuan"),
        ("Scholarship_holder", "Penerima Beasiswa?", "1 – ya, 0 – tidak"),
        ("International", "Mahasiswa Internasional?", "1 – ya, 0 – tidak"),
    ]:
        input_data[bcol] = st.radio(
            label,
            [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak",
            help=tooltip
        )

    input_data["Age_at_enrollment"] = st.number_input(
        "Usia saat Masuk Kuliah",
        min_value=15, max_value=70,
        help="Usia mahasiswa saat mendaftar kuliah (Usia minimal 15 tahun dan usia maksimal 70 tahun)"
    )

    # Fitur numerik tambahan
    num_fields = [
        ("Curricular_units_1st_sem_credited", "Jumlah mata kuliah semester 1 yang diakui (transfer kredit)"),
        ("Curricular_units_1st_sem_enrolled", "Jumlah mata kuliah semester 1 yang diambil"),
        ("Curricular_units_1st_sem_evaluations", "Jumlah mata kuliah semester 1 yang diikuti ujian/penilaian"),
        ("Curricular_units_1st_sem_approved", "Jumlah mata kuliah semester 1 yang lulus/diterima"),
        ("Curricular_units_1st_sem_grade", "Nilai rata-rata semester 1 (0–20)"),
        ("Curricular_units_1st_sem_without_evaluations", "Jumlah mata kuliah semester 1 tanpa evaluasi"),
        ("Curricular_units_2nd_sem_credited", "Jumlah mata kuliah semester 2 yang diakui (transfer kredit)"),
        ("Curricular_units_2nd_sem_enrolled", "Jumlah mata kuliah semester 2 yang diambil"),
        ("Curricular_units_2nd_sem_evaluations", "Jumlah mata kuliah semester 2 yang diikuti ujian/penilaian"),
        ("Curricular_units_2nd_sem_approved", "Jumlah mata kuliah semester 2 yang lulus/diterima"),
        ("Curricular_units_2nd_sem_grade", "Nilai rata-rata semester 2 (0–20)"),
        ("Curricular_units_2nd_sem_without_evaluations", "Jumlah mata kuliah semester 2 tanpa evaluasi"),
        ("Unemployment_rate", "Tingkat pengangguran (%)"),
        ("Inflation_rate", "Tingkat inflasi (%)"),
        ("GDP", "Produk Domestik Bruto (juta Euro)")
    ]

    for col, help_text in num_fields:
        input_data[col] = st.number_input(col.replace("_", " ").title(), step=1.0, help=help_text)

    submit = st.form_submit_button("Prediksi")

    if submit:
        input_df = pd.DataFrame([input_data])
        input_df = input_df[feature_order]
        prediction = model.predict(input_df)[0]
        label = ["Graduate", "Enrolled", "Dropout"][prediction]
        st.success(f"✅⏳ Hasil Prediksi: **{label}**")
