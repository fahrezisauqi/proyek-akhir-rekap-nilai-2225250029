
BATAS_LULUS = 60


def validasi_nilai(nilai):
    """Memeriksa nilai antara 0 sampai 100."""
    return 0 <= nilai <= 100


def hitung_statistik(data):
    """Menghitung statistik nilai siswa."""

    if not data:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0
        }

    daftar_nilai = [siswa["nilai"] for siswa in data]

    return {
        "jumlah": len(daftar_nilai),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "lulus": sum(1 for nilai in daftar_nilai if nilai >= BATAS_LULUS)
    }


def tentukan_status(nilai, kkm=BATAS_LULUS):
    """Menentukan status kelulusan."""
    if nilai >= kkm:
        return "Tuntas"
    return "Belum Tuntas"
