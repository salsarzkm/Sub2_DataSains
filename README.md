# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

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

Setelah ditelaah, sehingga perlu adanya sistem prediktif yang mampu mendeteksi mahasiswa yang berisiko tinggi dropout secara otomatis dan akurat. Kedua, sistem dapat menangani kompleksitas data mahasiswa yang berasal dari berbagai sumber, seperti data demografis, akademik, sosial ekonomi, dan administrasi keuangan, serta memberi peringatan dini kepada tenaga pendidik atau manajemen kampus agar bisa melakukan intervensi yang tepat waktu.
Di sisi lain, keterbatasan waktu dan jumlah tenaga pendidik membuat proses pemantauan secara manual menjadi tidak efisien dan tidak skalabel. Maka dari itu, Jaya Jaya Institut membutuhkan pendekatan berbasis data yang modern untuk mengatasi permasalahan ini.

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

Sumber data: ....

Setup environment:
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
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

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
