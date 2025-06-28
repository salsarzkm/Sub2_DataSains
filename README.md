# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

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

1. Analisis Data Mahasiswa
   Melakukan eksplorasi menyeluruh terhadap data mahasiswa yang mencakup informasi akademik, demografis, dan sosial-ekonomi.
2. Prediksi Status Mahasiswa
   Membangun model klasifikasi machine learning untuk memprediksi status akhir mahasiswa:
   `Dropout:` Mahasiswa yang keluar sebelum lulus
   `Enrolled:` Mahasiswa yang masih aktif
   `Graduate:` Mahasiswa yang telah lulus
3. Evaluasi Kinerja Model
   Mengevaluasi performa model dengan metrik seperti accuracy, precision, recall, f1-score, dan confusion matrix, dengan fokus utama pada kemampuan mendeteksi mahasiswa dropout.
4. Visualisasi & Dashboard
   Menyediakan visualisasi interaktif dan dashboard (menggunakan tools seperti Streamlit) agar pihak manajemen dapat memantau performa mahasiswa dengan mudah.

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
conda activate attrition-env

# Install library dari requirements.txt
pip install -r requirements.txt

# Jalankan jupyter notebook
pip install notebook
jupyter notebook
```

## Business Dashboard

Dashboard bisnis ini dibuat menggunakan Looker Studio untuk memvisualisasikan dan menganalisis secara menyeluruh fenomena dropout mahasiswa di Jaya Jaya Institut. Melalui dashboard ini, pengguna dapat memahami pola dan faktor utama yang memengaruhi keputusan mahasiswa untuk tidak melanjutkan studinya.
Tampilan visual  dapat memungkinkan tim akademik dan manajemen untuk mengambil keputusan berbasis data dalam pemberian intervensi atau bimbingan, menyusun kebijakan akademik dan keuangan yang lebih tepat sasaran, dan memantau performa dan kemajuan mahasiswa secara berkelanjutan.

📊 Akses dashboard dapat melalui tautan berikut: [Tautan Dashboard](https://lookerstudio.google.com/reporting/5d1fc55b-b8f9-49c9-af81-6388d0aa7593)

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

---

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
