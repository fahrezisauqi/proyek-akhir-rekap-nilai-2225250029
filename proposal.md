
# PROPOSAL PROYEK
# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Latar Belakang

Guru matematika membutuhkan cara yang lebih mudah untuk mengolah nilai siswa. Penghitungan rata-rata, nilai minimum, maksimum, dan ketuntasan secara manual membutuhkan waktu.

Oleh karena itu, dibuat program Python sederhana untuk membaca data nilai, memvalidasi data, menghitung statistik, menentukan ketuntasan, dan menyimpan laporan.

## 2. Pengguna dan Tujuan

**Pengguna:** Guru matematika.

**Tujuan:**
- Mempermudah pengolahan nilai siswa.
- Mengurangi kesalahan perhitungan manual.
- Menghasilkan laporan nilai secara otomatis.

## 3. Ruang Lingkup

### Fitur wajib
1. Membaca data nilai dari file.
2. Memvalidasi nilai dari 0 sampai 100.
3. Menghitung rata-rata, minimum, dan maksimum.
4. Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
5. Menyimpan laporan ke file teks.

### Batasan proyek
- Menggunakan Python berbasis terminal/console.
- Data dibaca dari file teks.
- Tidak menggunakan database.
- Tidak menggunakan antarmuka web atau grafis.
- KKM ditetapkan sebesar 60.

## 4. Kebutuhan Sistem

### Kebutuhan fungsional
| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Membaca file nilai | Wajib |
| F02 | Memvalidasi nilai 0–100 | Wajib |
| F03 | Menghitung rata-rata, minimum, maksimum | Wajib |
| F04 | Menentukan status ketuntasan | Wajib |
| F05 | Menyimpan laporan | Wajib |
| F06 | Menampilkan statistik per kategori | Tambahan |

### Kebutuhan nonfungsional
- Mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami.
- Nama fungsi dan variabel jelas.
- Menggunakan data contoh, bukan data pribadi nyata.
- Dapat diuji kembali menggunakan test case yang sama.

## 5. Input, Proses, dan Output (IPO)

### Input
- File nilai_contoh.txt.
- Data berupa ID, nama, dan nilai.
- Nilai KKM sebesar 60.

### Proses
1. Membaca data dari file.
2. Memeriksa format data.
3. Memvalidasi nilai antara 0 sampai 100.
4. Menyimpan data yang valid.
5. Menghitung rata-rata, minimum, dan maksimum.
6. Menghitung jumlah siswa tuntas dan belum tuntas.
7. Menyimpan hasil ke file laporan.

### Output
- Jumlah data valid.
- Rata-rata nilai.
- Nilai minimum.
- Nilai maksimum.
- Jumlah siswa tuntas.
- Jumlah siswa belum tuntas.
- File laporan.txt.

## 6. Algoritma / Pseudocode

MULAI

1. Baca data dari file.
2. Jika file tidak ditemukan:
   - Tampilkan pesan kesalahan.
   - Selesai.
3. Untuk setiap baris data:
   - Periksa format data.
   - Periksa nilai antara 0 sampai 100.
   - Simpan data valid.
4. Jika tidak ada data valid:
   - Tampilkan pesan.
   - Selesai.
5. Hitung rata-rata.
6. Cari nilai minimum dan maksimum.
7. Tentukan status ketuntasan berdasarkan KKM 60.
8. Tampilkan ringkasan.
9. Simpan laporan ke file.
SELESAI.

## 7. Struktur Program dan Fungsi

| Fungsi | Tanggung jawab |
|---|---|
| baca_data() | Membaca data dari file |
| validasi_nilai() | Memeriksa nilai 0–100 |
| hitung_statistik() | Menghitung rata-rata, minimum, maksimum |
| tentukan_status() | Menentukan status tuntas atau belum tuntas |
| simpan_laporan() | Menyimpan laporan ke file |
| main() | Mengatur alur program |

## 8. Struktur Data

- List: menyimpan kumpulan nilai.
- Dictionary: menyimpan data siswa berdasarkan ID.
- String: menyimpan teks laporan.
- File teks: menyimpan data masukan dan laporan.

Contoh:

data_mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

## 9. Test Case Awal

| ID | Kategori | Input/Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas = jumlah data |

## 10. Pembagian Tugas

Jika dikerjakan sendiri:
- Perancangan: Fahrezi Sauqi Alghani.
- Programmer Data I/O: Fahrezi Sauqi Alghani.
- Programmer Logika: Fahrezi Sauqi Alghani.
- Tester/QA: Fahrezi Sauqi Alghani.
- Dokumentasi: Fahrezi Sauqi Alghani.

Jika dikerjakan berkelompok, nama dan tugas anggota disesuaikan dengan pembagian tim.

## 11. Jadwal / Milestone

| Waktu | Target |
|---|---|
| Pertemuan 14 | Proposal, struktur folder, pseudocode, test case |
| Antara P14–P15 | Implementasi awal fitur wajib |
| Pertemuan 15 | Integrasi, testing, debugging, dokumentasi |
| Pertemuan 16 | Presentasi, demonstrasi, evaluasi |

## 12. Repository

Nama repository:
proyek-akhir-rekap-nilai-2225250029

URL:
https://github.com/fahrezisauqi/proyek-akhir-rekap-nilai-2225250029

## 13. Kesimpulan

Proyek ini dirancang untuk membantu guru matematika mengolah nilai siswa secara lebih cepat dan konsisten. Rancangan mencakup kebutuhan pengguna, IPO, pseudocode, struktur program, struktur data, dan test case awal. Proposal ini menjadi pedoman implementasi pada Pertemuan 15.
