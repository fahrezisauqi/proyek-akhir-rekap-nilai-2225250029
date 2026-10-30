
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from analisis import (
    validasi_nilai,
    hitung_statistik,
    tentukan_status
)

print("MULAI PENGUJIAN PROGRAM")
print("=" * 35)

# TC01: Pengujian nilai normal
assert validasi_nilai(80) == True
print("TC01: Nilai normal - PASS")

# TC02: Pengujian nilai batas bawah
assert validasi_nilai(0) == True
print("TC02: Nilai batas bawah - PASS")

# TC03: Pengujian nilai batas atas
assert validasi_nilai(100) == True
print("TC03: Nilai batas atas - PASS")

# TC04: Pengujian nilai tidak valid
assert validasi_nilai(105) == False
print("TC04: Nilai tidak valid - PASS")

# TC05: Pengujian kelulusan pada batas 60
assert tentukan_status(60) == "Tuntas"
print("TC05: Batas kelulusan - PASS")

# TC06: Pengujian data kosong
hasil = hitung_statistik([])
assert hasil["rata_rata"] == 0
assert hasil["jumlah"] == 0
print("TC06: Data kosong - PASS")

print("=" * 35)
print("SEMUA PENGUJIAN BERHASIL!")
