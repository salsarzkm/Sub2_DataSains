# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

---

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, dalam beberapa tahun terakhir, institusi menghadapi tingkat dropout mahasiswa yang cukup tinggi, yang menjadi ancaman serius terhadap citra akademik, efisiensi operasional, serta kualitas pendidikan yang ditawarkan.

Fenomena mahasiswa yang tidak menyelesaikan pendidikannya bukan hanya merugikan dari sisi institusi, tetapi juga berdampak pada masa depan mahasiswa itu sendiri. Penyebab dropout bisa sangat kompleks, melibatkan aspek akademik, sosial, ekonomi, maupun psikologis.

---

### Permasalahan Bisnis

Meskipun telah memiliki reputasi baik sebagai institusi pendidikan tinggi dan berhasil mencetak banyak lulusan berkualitas, Jaya Jaya Institut menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan studi alias dropout. Fenomena ini berdampak negatif tidak hanya terhadap performa akademik institusi, tetapi juga pada persepsi publik, akreditasi, serta stabilitas operasional jangka panjang.

Dropout yang tinggi berpotensi menimbulkan berbagai konsekuensi, seperti:

- Menurunnya tingkat kelulusan yang dapat memengaruhi akreditasi institusi,
- Tingginya biaya sumber daya yang sudah dikeluarkan untuk mahasiswa yang tidak menyelesaikan studi,
- Penurunan reputasi institusi di mata calon mahasiswa dan orang tua,
- Kehilangan potensi lulusan berkualitas yang seharusnya bisa menjadi bagian dari alumni sukses.

Oleh karena itu, perlu adanya sistem prediktif yang mampu mendeteksi mahasiswa yang berisiko tinggi dropout secara otomatis dan akurat. Kedua, sistem dapat menangani kompleksitas data mahasiswa yang berasal dari berbagai sumber, seperti data demografis, akademik, sosial ekonomi, dan administrasi keuangan, serta memberi peringatan dini kepada tenaga pendidik atau manajemen kampus agar bisa melakukan intervensi yang tepat waktu.
Di sisi lain, keterbatasan waktu dan jumlah tenaga pendidik membuat proses pemantauan secara manual menjadi tidak efisien dan tidak skalabel. Maka dari itu, Jaya Jaya Institut membutuhkan pendekatan berbasis data yang modern untuk mengatasi permasalahan ini.

---

### Tujuan Bisnis

1. Mengidentifikasi secara dini mahasiswa yang berisiko tinggi untuk dropout.
2. Memberikan intervensi atau bimbingan khusus terhadap mahasiswa yang terdeteksi berisiko.
3. Meminimalkan tingkat dropout untuk menjaga reputasi dan efisiensi akademik institusi.

---

### Cakupan Proyek

#### ✅ Data yang Digunakan

Dataset yang digunakan berisi informasi dari institusi pendidikan tinggi dengan cakupan sebagai berikut:
- Karakteristik personal dan demografis: usia, gender, status pernikahan, kebangsaan
- Latar belakang pendidikan dan sosial: kualifikasi dan pekerjaan orang tua, jenis pendaftaran, nilai masuk
- Informasi akademik semester 1 dan 2: jumlah mata kuliah diambil, nilai, jumlah evaluasi, jumlah lulus
- Faktor ekonomi: status beasiswa, keterlambatan pembayaran biaya kuliah, apakah memiliki utang
- Kondisi khusus: kebutuhan pendidikan khusus, apakah siswa internasional, siswa pindahan, dll.

#### ✅ Langkah-Lankgah

**1. Analisis Data Mahasiswa & _Exploratory Data Analysis_ (EDA)**
   
   Tahapan awal proyek dimulai dengan eksplorasi menyeluruh terhadap data mahasiswa yang mencakup informasi akademik, demografis, dan sosial-ekonomi. Visualisasi awal terhadap variabel target menunjukkan bahwa mayoritas mahasiswa berstatus Graduate, sementara mahasiswa Dropout dan Enrolled jumlahnya lebih sedikit, mengindikasikan ketidakseimbangan kelas.
   Selanjutnya, dilakukan analisis korelasi numerik terhadap status dropout untuk memahami fitur mana yang paling berkontribusi. Ditemukan bahwa usia saat mendaftar dan status Debtor berkorelasi positif dengan dropout. Sementara itu, nilai akademik yang tinggi, jumlah mata kuliah yang disetujui, pembayaran biaya kuliah tepat waktu, dan status penerima beasiswa menunjukkan korelasi negatif dengan dropout, menandakan faktor-faktor ini berperan penting dalam keberhasilan studi.
   Lalu, Distribusi nilai semester juga dianalisis melalui boxplot, yang mengungkap bahwa mahasiswa Dropout memiliki nilai rata-rata yang jauh lebih rendah di semester 1 dan 2 dibanding mahasiswa Graduate dan Enrolled, memperkuat peran penting kinerja akademik dalam prediksi status akhir.
   Sebagai tambahan, dibuat visualisasi untuk fitur kategorikal (seperti Gender, Marital_status, International, dll) terhadap target Status menggunakan grid plot. Ini memungkinkan pengamatan langsung terhadap pola distribusi dropout berdasarkan kategori, seperti kecenderungan mahasiswa dengan status tidak menikah, internasional, atau displaced untuk memiliki tingkat dropout lebih tinggi.

**2. _Preprocessing Data_**

   Setelah pemahaman mendalam dari EDA, proses preprocessing dilakukan dengan fitur kategorikal diubah menjadi representasi numerik menggunakan encoding. Tidak lupa dengan penanganan oulier dengan winsorization. Lalu, Karena data target Status sangat tidak seimbang, digunakan metode oversampling SMOTE (Synthetic Minority Oversampling Technique) untuk menyeimbangkan representasi antara kelas mayoritas (Graduate) dan minoritas (Dropout & Enrolled). Ini penting untuk mencegah model bias terhadap kelas mayoritas. Data yang telah diproses dibagi menjadi data latih dan data uji menggunakan stratifikasi, agar distribusi kelas target tetap proporsional dalam evaluasi. 

**3. Pembangunan Model Prediktif**
   
   Model prediksi dikembangkan menggunakan algoritma XGBoost Classifier, yang dikenal sangat efektif dalam menangani dataset yang tidak seimbang serta memiliki kemampuan generalisasi yang baik. Pipeline Scikit-Learn digunakan untuk menggabungkan preprocessing (scaling) dan modeling, sehingga prosesnya lebih modular dan terstandardisasi. Model dilatih menggunakan data hasil SMOTE dan diuji menggunakan data uji asli (tanpa resampling), untuk mendapatkan evaluasi yang merefleksikan situasi nyata.

**4. Evaluasi Kinerja Model**

   Mengevaluasi performa model dengan metrik seperti accuracy, precision, recall, f1-score, dan confusion matrix, dengan fokus utama pada kemampuan mendeteksi mahasiswa dropout.
   
**6. Visualisasi & Dashboard**

   Untuk mendukung pengambilan keputusan berbasis data, dikembangkan:
   - Visualisasi interaktif dengan Streamlit, yang memungkinkan pengguna kampus (non-teknis) melakukan input data mahasiswa dan melihat prediksi status akhir secara langsung.
   - Dashboard bisnis menggunakan Google Looker Studio, yang menyajikan visual ringkasan seperti Distribusi mahasiswa berdasarkan status akhir, Faktor-faktor dominan yang memengaruhi dropout, serta Statistik berdasarkan program studi, waktu kuliah, dan status beasiswa

**CATATAN: Tidak menggunakan Metabase dalam projek ini, sehingga tidak ada metabase.db.mv.db**

---

### Persiapan

#### 👉🏼 Sumber data

Sumber data yang digunakan berasal dari repository GitHub Dicoding Academy, yaitu [dataset Students' Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md). Dataset yang dibuat dari institusi pendidikan tinggi (diperoleh dari beberapa basis data terpisah) yang terkait dengan mahasiswa yang terdaftar di berbagai program studi sarjana, seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi. Dataset ini mencakup informasi yang diketahui pada saat pendaftaran mahasiswa (jalur akademik, demografi, dan faktor sosial-ekonomi) dan kinerja akademik mahasiswa pada akhir semester pertama dan kedua. Data tersebut digunakan untuk membangun model klasifikasi untuk memprediksi tingkat putus sekolah dan keberhasilan akademik siswa.

Berikut adalah deskripsi fitur-fitur yang terdapat dalam dataset:
- `Marital status` :  Status pernikahan mahasiswa. (Kategorikal): 1 – lajang, 2 – menikah, 3 – duda/janda, 4 - cerai, 5 – kumpul kebo, 6 – pisah secara hukum
- `Application mode` : Metode pendaftaran yang digunakan mahasiswa. (Kategorikal): berbagai jenis jalur pendaftaran seperti jalur umum, jalur khusus, perpindahan, mahasiswa internasional, dll
- `Application order` : Urutan pilihan jurusan saat mendaftar (Numerik): 0 = pilihan pertama, 9 = pilihan terakhir 
- `Course` : Program studi yang diambil mahasiswa. (Kategorikal): misal Teknik Informatika, Keperawatan, Manajemen, dsb 
- `Daytime/evening attendance` : Waktu kehadiran kuliah. (Kategorikal): 1 – siang, 0 – malam 
- `Previous qualification` : Pendidikan terakhir sebelum masuk perguruan tinggi. (Kategorikal): dari pendidikan dasar hingga doktoral, termasuk kursus teknis
- `Previous qualification (grade)` : Nilai dari pendidikan terakhir sebelum kuliah (0–200)
-  `Nationality` : Kewarganegaraan mahasiswa. (Kategorikal): 1 – Portugis, 2 – Jerman, 6 – Spanyol, dst 
-  `Mother's qualification` : Tingkat pendidikan ibu mahasiswa. (Kategorikal): dari tidak bisa baca/tulis sampai doktoral
-  `Father's qualification` : Tingkat pendidikan ayah mahasiswa. (Kategorikal): dari tidak bisa baca/tulis sampai doktoral
-  `Mother's occupation` : Pekerjaan ibu mahasiswa. (Kategorikal): mulai dari pelajar, profesional, pekerja kasar, guru, kesehatan, dll
-  `Father's occupation` : Pekerjaan ayah mahasiswa. (Kategorikal): mulai dari pelajar, profesional, pekerja kasar, guru, militer, dll
-  `Admission grade` : Nilai masuk saat diterima di perguruan tinggi (0–200)
-  `Displaced` : Apakah mahasiswa berasal dari luar daerah tempat studi. (Kategorikal): 1 – ya, 0 – tidak
-  `Educational special needs` : Apakah mahasiswa memiliki kebutuhan khusus dalam pendidikan. (Kategorikal): 1 – ya, 0 – tidak
-  `Debtor` : Apakah mahasiswa memiliki tunggakan pembayaran. (Kategorikal): 1 – ya, 0 – tidak
-  `Tuition fees up to date` : Apakah pembayaran kuliah mahasiswa sudah diperbarui/lunas. (Kategorikal): 1 – ya, 0 – tidak
-   `Gender` : Jenis kelamin mahasiswa. (Kategorikal): 1 – laki-laki, 0 – perempuan
-   `Scholarship holder` : Apakah mahasiswa penerima beasiswa. (Kategorikal): 1 – ya, 0 – tidak
-   `Age at enrollment` : Usia mahasiswa saat mendaftar kuliah. (Numerik)
-   `International` : Apakah mahasiswa berasal dari luar negeri. (Kategorikal): 1 – ya, 0 – tidak
-   `Curricular units 1st sem (credited)` : Jumlah mata kuliah semester 1 yang diakui (transfer kredit). (Numerik)
-   `Curricular units 1st sem (enrolled)` : Jumlah mata kuliah semester 1 yang diambil. (Numerik)
-   `Curricular units 1st sem (evaluations)` : Jumlah mata kuliah semester 1 yang diikuti ujian/penilaian. (Numerik)
-   `Curricular units 1st sem (approved)` : Jumlah mata kuliah semester 1 yang lulus/diterima. (Numerik)
  
#### 👉🏼 Setup environment

Dengan Menggunakan Anaconda

```
# Ke folder proyek
cd C:\Users\Windows 10\Studpen_DataSains2

# Buat environment baru
conda create -n student-env python=3.9

# Aktifkan environment
conda activate student-env

# Install library dari requirements.txt
pip install -r requirements.txt

# Jalankan jupyter notebook
pip install notebook
jupyter notebook
```

---

## Business Dashboard

Dashboard ini bertujuan untuk membantu institusi memahami karakteristik dan performa mahasiswa berdasarkan status akhir mereka (Dropout, Enrolled, Graduate), serta membantu monitoring dan pengambilan keputusan berbasis data. Tampilan visual  dapat memungkinkan tim akademik dan manajemen untuk mengambil keputusan berbasis data dalam pemberian intervensi atau bimbingan, menyusun kebijakan akademik dan keuangan yang lebih tepat sasaran, dan memantau performa dan kemajuan mahasiswa secara berkelanjutan.

📊 Akses dashboard dapat melalui tautan berikut: [Tautan Dashboard](https://lookerstudio.google.com/reporting/5d1fc55b-b8f9-49c9-af81-6388d0aa7593)

---

## Menjalankan Sistem Machine Learning

Proyek ini merupakan solusi machine learning untuk memprediksi risiko dropout mahasiswa berdasarkan berbagai karakteristik pribadi dan akademik. Sistem dibangun menggunakan model XGBoost dan ditampilkan melalui aplikasi web interaktif menggunakan Streamlit.

⏩ Prototype ini juga telah berhasil di-_deploy_ dan dapat diakses secara online melalui _(Community Cloud)_ , dimana tidak memerlukan install apapun dan cukup buka link di browser melalui : [Tautan Streamlit](https://sub2datasains-ya7q4un2rthpxhzmjfnveg.streamlit.app/)

⏩ Untuk menjalankan aplikasi/prototype secara lokal di komputer, dapat dilakukan dengan:

```
# Clone repo
git clone https://github.com/salsarzkm/Sub2_DataSains.git
cd Sub2_DataSains

# Install dependency
pip install -r requirements.txt

# Jalankan aplikasi Streamlit
streamlit run app.py
```

⏩ Adapun tampilan streamlit cloud dapat dilihat sebagai berikut:

**Hasil tampilan depan**
<img width="927" alt="contoh_dashboard1" src="https://github.com/user-attachments/assets/1f99345a-34db-4f49-a44e-d645640c5141" />

**Hasil tampilan akhir prediksi setelah input seluruh data**
<img width="924" alt="contoh_dashboard2" src="https://github.com/user-attachments/assets/368ad937-7867-4a4e-a5a9-9213129cb079" />

---

## Conclusion

![distribusi_status_siswa](https://github.com/user-attachments/assets/73d01eae-8c88-4821-97cf-6c1e5bd5ae93)

Berdasarkan grafik, terlihat bahwa status "Graduate" memiliki jumlah siswa terbanyak, yaitu di atas 2000. Status "Dropout" menempati posisi kedua dengan jumlah siswa sekitar 1400. Sementara itu, status "Enrolled" memiliki jumlah siswa paling sedikit, yaitu di bawah 1000.

![10_korelasi_negatif](https://github.com/user-attachments/assets/215c6e9f-75d8-4748-863b-fe5c1dc1e450)
![10_korelasi_positif](https://github.com/user-attachments/assets/e881b5b5-cc1f-430c-819e-6e1398fcd932)

Analisis korelasi menunjukkan bahwa usia pendaftaran dan status debitur berkorelasi positif kuat dengan dropout. Sebaliknya, kinerja akademik yang baik (nilai dan unit mata kuliah yang disetujui) memiliki korelasi negatif yang sangat kuat, menunjukkan pentingnya nilai dalam mencegah dropout. Faktor lain seperti pembayaran biaya kuliah tepat waktu dan menjadi penerima beasiswa juga berkorelasi negatif, sehingga dapat mengurangi kemungkinan dropout. Secara keseluruhan, faktor finansial, demografi, dan terutama kinerja akademik adalah pendorong utama status dropout.

![distribusi_nilai](https://github.com/user-attachments/assets/2a0e5de1-7cc3-4158-8099-7027fbd45fe0)

Berdasarkan box plot distribusi nilai, mahasiswa yang mengalami dropout menunjukkan nilai rata-rata yang jauh lebih rendah di semester 1 dan 2 dibandingkan dengan mahasiswa graduate dan enrolled. Mahasiswa graduate memiliki nilai rata-rata tertinggi di kedua semester, diikuti oleh mahasiswa enrolled. Hal ini secara jelas menunjukkan bahwa kinerja akademik yang buruk, terutama nilai yang rendah, adalah indikator kuat risiko dropout.

![kategori_vs_status](https://github.com/user-attachments/assets/26de8f00-55ba-45d1-9f59-0d752016db89)

Visualisasi ini menunjukkan distribusi status mahasiswa (Dropout, Enrolled, Graduate) berdasarkan berbagai fitur kategorikal. Beberapa kategori fitur lain cenderung memiliki proporsi mahasiswa graduate atau enrolled yang lebih tinggi, mengindikasikan hubungan penting antara fitur kategorikal ini dengan keberhasilan atau kegagalan akademik. Analisis ini membantu mengidentifikasi karakteristik demografi atau latar belakang yang mungkin menjadi faktor risiko atau pelindung terhadap dropout.

---

### Rekomendasi Action Items

🎯 **A. Intervensi Berdasarkan Kinerja Akademik**
   1. Program Remedial dan Bimbingan Belajar → Sediakan kelas tambahan, remedial, atau tutor sebaya untuk mahasiswa dengan nilai rendah pada semester 1 dan 2.
   2. Sistem Peringatan Dini (Early Warning System) → Bangun sistem yang mendeteksi mahasiswa dengan nilai semester awal rendah, lalu berikan intervensi akademik sejak dini.
   3. Evaluasi Kurikulum & Dosen Pengampu → Tinjau ulang mata kuliah yang paling sering tidak lulus atau memiliki tingkat kegagalan tinggi, khususnya di program studi dengan dropout tinggi seperti Manajemen (9147 dan 9991).

💰 **B. Intervensi Berdasarkan Faktor Finansial**
1. Perluas Akses Beasiswa & Bantuan Finansial → Tingkatkan cakupan beasiswa karena terbukti menjadi pelindung signifikan terhadap dropout.
2. Program Cicilan atau Relaksasi Pembayaran → Berikan opsi pembayaran bertahap atau fleksibel agar mahasiswa tidak merasa terbebani, terutama yang bukan penerima beasiswa.
3. Edukasi Literasi Finansial
→ Adakan pelatihan keuangan dasar bagi mahasiswa agar dapat mengelola biaya kuliah dan kebutuhan akademik lainnya.

🧭 **C. Intervensi Berdasarkan Program Studi**
1. Audit Program Studi dengan Dropout Tinggi → Lakukan audit menyeluruh terhadap program Manajemen (9147 & 9991) untuk mengidentifikasi penyebab dropout tinggi: beban kurikulum, metode ajar, waktu kuliah, dsb.
2. Peningkatan Fasilitas untuk Kelas Malam → Sediakan dukungan infrastruktur dan akademik setara untuk kelas malam agar tidak tertinggal dibanding kelas reguler.
