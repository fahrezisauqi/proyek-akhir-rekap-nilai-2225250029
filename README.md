
# Program Rekap dan Analisis Nilai Matematika Kelas

## Identitas

Nama: Fahrezi Sauqi Alghani  
NIM: 2225250029  
Kelas: 3E

## Deskripsi

Proyek Python sederhana untuk membantu guru matematika
membaca data nilai, memvalidasi nilai, menghitung statistik,
menentukan ketuntasan, dan menyimpan laporan.

## Fitur

1. Membaca file nilai.
2. Memvalidasi nilai 0-100.
3. Menghitung rata-rata.
4. Mencari nilai minimum dan maksimum.
5. Menghitung jumlah siswa tuntas dan belum tuntas.
6. Menyimpan laporan.

## Struktur Folder

- data: data nilai contoh.
- src: rancangan modul program.
- tests: test case.
- output: tempat laporan.

## Cara Menjalankan

Implementasi program akan dibuat pada Pertemuan 15.

## Dokumen

- proposal.md: rancangan proyek.
- tests/test_case.md: test case awal.

## KKM

KKM yang digunakan dalam rancangan ini adalah 60.

## Tahapan Proyek

- Pertemuan 14: perancangan proyek.
- Pertemuan 15: implementasi dan pengujian.
- Pertemuan 16: presentasi dan evaluasi.

## Implementasi Pertemuan 15

Program sudah diimplementasikan menggunakan Python.

### Fitur
- Membaca data nilai siswa dari file.
- Memvalidasi nilai antara 0 sampai 100.
- Menghitung rata-rata nilai.
- Menentukan nilai minimum dan maksimum.
- Menghitung jumlah siswa yang tuntas.
- Menyimpan laporan hasil rekap.

### Pengujian
Pengujian dilakukan menggunakan file `tests/test_program.py`.

| ID | Pengujian | Status |
|---|---|---|
| TC01 | Nilai normal | PASS |
| TC02 | Nilai batas bawah | PASS |
| TC03 | Nilai batas atas | PASS |
| TC04 | Nilai tidak valid | PASS |
| TC05 | Batas kelulusan | PASS |
| TC06 | Data kosong | PASS |

### Cara Menjalankan

Jalankan program:

```bash
py src/main.py
```

Jalankan pengujian:

```bash
py tests/test_program.py
```
