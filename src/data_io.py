
def baca_data(path):
    """Membaca data nilai siswa dari file."""
    data = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                bagian = baris.strip().split(",")

                if len(bagian) != 3:
                    print(f"Baris {nomor} tidak valid.")
                    continue

                try:
                    kode = bagian[0].strip()
                    nama = bagian[1].strip()
                    nilai = float(bagian[2].strip())

                    if not kode or not nama:
                        print(f"Baris {nomor}: data kosong.")
                        continue

                    if not 0 <= nilai <= 100:
                        print(f"Baris {nomor}: nilai harus 0-100.")
                        continue

                    data.append({
                        "kode": kode,
                        "nama": nama,
                        "nilai": nilai
                    })

                except ValueError:
                    print(f"Baris {nomor}: nilai harus berupa angka.")

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    return data


def simpan_laporan(hasil, path):
    """Menyimpan hasil rekap ke file."""
    with open(path, "w", encoding="utf-8") as file:
        file.write("LAPORAN NILAI MATEMATIKA\n")
        file.write("=======================\n")
        file.write(f"Jumlah siswa: {hasil['jumlah']}\n")
        file.write(f"Rata-rata: {hasil['rata_rata']:.2f}\n")
        file.write(f"Nilai minimum: {hasil['minimum']}\n")
        file.write(f"Nilai maksimum: {hasil['maksimum']}\n")
        file.write(f"Jumlah tuntas: {hasil['lulus']}\n")
