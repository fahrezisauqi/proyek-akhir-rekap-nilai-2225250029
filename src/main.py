
from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, tentukan_status
from utilitas import tampilkan_pesan, garis


def main():
    tampilkan_pesan("PROGRAM REKAP NILAI MATEMATIKA")
    garis()

    data = baca_data("data/nilai_contoh.txt")

    if not data:
        tampilkan_pesan("Tidak ada data siswa yang valid.")
        return

    print("\nDAFTAR NILAI SISWA")
    garis()

    for siswa in data:
        status = tentukan_status(siswa["nilai"])

        print(
            f"{siswa['kode']} | "
            f"{siswa['nama']} | "
            f"{siswa['nilai']} | "
            f"{status}"
        )

    hasil = hitung_statistik(data)

    print("\nRINGKASAN NILAI")
    garis()
    print(f"Jumlah siswa    : {hasil['jumlah']}")
    print(f"Rata-rata       : {hasil['rata_rata']:.2f}")
    print(f"Nilai minimum   : {hasil['minimum']}")
    print(f"Nilai maksimum  : {hasil['maksimum']}")
    print(f"Jumlah tuntas   : {hasil['lulus']}")

    simpan_laporan(hasil, "output/hasil_rekap.txt")
    tampilkan_pesan("Program selesai dijalankan.")


if __name__ == "__main__":
    main()
