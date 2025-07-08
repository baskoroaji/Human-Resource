
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang berdiri sejak tahun 2000 dengan lebih dari 1.000 karyawan tersebar di berbagai wilayah Indonesia. Pertumbuhan pesat perusahaan diikuti tantangan dalam mengelola SDM, terutama tingkat attrition >10% per tahun. Hal ini berdampak pada keuangan dan produktivitas perusahaan.

### Permasalahan Bisnis

1. Tingginya Attrition Rate
    - Hilangnya atau keluarnya salah satu anggota tim akan mempengaruhi kinerja tim tersebut

2. Belum adanya pemahaman apa saja faktor attrition
    - Belum ada identifikasi,analisa penyebab faktor attrition

3. Tidak adanya sistem monitoring
    - HR hanya tau ketika pegawai/karyawan mengundurkan diri tanpa adanya insight data kenapa karyawan tersebut mengundurkan diri dalam bentuk visual yang mudah dipahami

4. Kurang bagusnya pengambilan keputusan
    - pengambilan keputusan tidak menurut analisa data/tanpa bantuan prediksi risiko attrition

### Cakupan Proyek

1. **Data Understanding & EDA**
   - Eksplorasi data karyawan (demografi, pekerjaan, kompensasi, kepuasan) untuk identifikasi pola attrition.
2. **Data Preparation**
   - Pembersihan data, imputasi _missing values_, encoding, dan penanganan _class imbalance_.
3. **Modeling**
   - Membangun model prediksi attrition (Logistic Regression, Random Forest).
4. **Evaluation**
   - Pengukuran performa model menggunakan precision, recall, dan F1-score.
5. **Business Dashboard**
   - Pengembangan dashboard interaktif di Metabase untuk memonitor risiko attrition dan rekomendasi retensi.
6. **Deployment Lokal**
   - Penyajian model dan dashboard dalam lingkungan lokal (container docker Metabase).

### Persiapan

- **Sumber data**:  
  https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

- **Setup environment (conda)**:
  1. Buka terminal/PowerShell
  2. Buat dan aktifkan env:
     ```bash
     conda create --name HR_Attrition_prediction python=3.12.9
     conda activate prediksi_attrition
     ```
  3. Instal library yang dibutuhkan:
     ```bash
     pip install requirements.txt
     ```
  4. Jalankan Jupyter Notebook (atau VSCode):
     ```bash
     jupyter-notebook
     ```
- **Credential Supabase (untuk Metabase)**:

  - Host: `aws-0-us-east-2.pooler.supabase.com`
  - Port: `5432`
  - Database: `postgres`
  - User: `postgres.uamrqobimfgxwfswnprl`
  - Password: `<YOUR-PASSWORD>`
  - Pool mode: `session`

- **Menjalankan script prediksi**:

  1. Buka `prediksi.py`
  2. Sesuaikan hard-coded input di variabel `data`
  3. Jalankan:
     ```bash
     python prediksi.py
     ```
  4. Hasil prediksi (“Yes”/“No”) dan probabilitas akan dicetak di console.

- **Email dan password Metabase**:
  - Email: baskoroaji2@gmail.com
  - Password: Jhlee0133

## Business Dashboard

Dashboard “HR Employee Attrition Insight” mencakup beberapa kartu visualisasi utama untuk membantu departemen HR memahami faktor-faktor yang mempengaruhi attrition, yaitu: Persentase Attrition, Jumlah Attrition,Attrition By Departemen,Attrition By JobRole, Overtime Impact on Attrition, Attrition Rate by Gender and JobRole,Monthly Rate by Attrition, Average YearsAtCompany by Attrition, dan Distance From Home by Attrition. Masing-masing pertanyaan bisnis menggunakan jenis chart yang seperti bar chart, horizontal bar, dan Pie Chart —sehingga memudahkan identifikasi departemen, role, demografi, dan durasi kerja yang paling berisiko.

## Conclusion

Setelah melakukan rangkaian analisis data, pemodelan machine learning, dan pembuatan dashboard interaktif, kini kita memiliki gambaran menyeluruh mengenai faktor-faktor penting yang mendorong attrition di Jaya Jaya Maju. Dengan memadukan kekuatan model prediksi dan visualisasi data, tim HR dapat bekerja menyelesaikan permasalahan attrition rate yang tinggi dengan beberapa pendekatan proaktif dalam mempertahankan karyawan. Berikut ringkasan performa model dan insight bisnis, beserta rekomendasi langkah selanjutnya.

### Performa Model
**Logistic Regression**
- Precision: 86%
- Recall: 73%
- f1-score: 76%

**Random Forest**
- Precision: 85%
- Recall: 86%
- f1-score: 85%

Dari hasil evaluasi, model menunjukan performa yang **Cukup Baik** dalam memprediksi Attrition

### Dashboard
- Dashboard memudahkan HR dalam menentukan keputusan dengan identifikasi berdasarkan faktor faktor seperti:
    - Departemen
    - JobRole
    - Karateristik dari Pekerjaan dan Karyawan


### Rekomendasi Action Items (Optional)

Beberapa Rekomendasi yang bisa diberikan agar perusahaan dapat memenuhi target dan menurunkan resiko attrition

**1. Menurunkan Resiko Attrition pada R&D dan Sales Departemen**
- Memberikan Insentif Bonus, Career Path yang jelas pada kedua departemen

**2. Menurunkan Resiko Attrition pada Pria**
- Memberikan hak hak yang setara antara karyawan wanita dan pria
- Melakukan survey kepuasan khusus gender untuk mengukur apa saja yang harus diperbaiki terhadap permasalahan hak antar jenis kelamin karyawan

**3. Menurunkan resiko attrition pada Overtime**
- Mengimplementasi waktu maksimal lembur
- Menerapkan program konseling pada karyawan
- Memberikan bonus lembur yang jelas pada karyawan

**4. Menurunkan resiko attrition dengan jarak dari rumah/tempat tinggal**
- Memberikan insentif seperti uang transport pada karyawan yang bertempat tinggal jauh
- Memberikan insentif biaya tempat tinggal (jika karyawan menyewa kos atau apartemen) dikarenakan biasanya karyawan yang tinggal dekat dengan perusahaan menyewa rumah/kos/apartemen

**5. Menurunkan resiko attrition dari jumlah perusahaan yang tempat kerja karyawan dahulu**
- Tim HR melakukan rekrutmen ke karyawan yang memiliki potensi bekerja yang bertahan lama
- Tim HR memberikan insight benefit ke calon karyawan dikarenakan berdasarkan hasil analisa karyawan paling banyak melakukan attrition pernah bekerja di 1 atau 2 perusahaan dimana karyawan tersebut bisa jadi fresh-graduated yang sedang mencari perusahaan yang memiliki career-path yang jelas
