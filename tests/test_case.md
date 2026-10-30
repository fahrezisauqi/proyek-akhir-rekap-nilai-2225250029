
# Test Case Awal
## Program Rekap dan Analisis Nilai Matematika

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima |
| TC03 | Batas | Nilai 100 | Diterima |
| TC04 | Invalid | Nilai 105 | Ditolak |
| TC05 | Invalid | File tidak ditemukan | Error ditangani |
| TC06 | Normal | Semua nilai >= 60 | Semua siswa tuntas |

## Tujuan Pengujian

1. Memastikan data normal dapat diproses.
2. Memastikan batas nilai 0 dan 100 diterima.
3. Memastikan nilai di luar rentang ditolak.
4. Memastikan file yang tidak tersedia ditangani.
5. Memastikan perhitungan ketuntasan sesuai KKM.
ID	Pengujian	Hasil aktual	Status
TC01	Nilai normal 80	Valid	PASS
TC02	Nilai 0	Valid	PASS
TC03	Nilai 100	Valid	PASS
TC04	Nilai 105	Tidak valid	PASS
TC05	Nilai 60	Tuntas	PASS
TC06	Data kosong	Rata-rata 0	PASS
