from src.input_data import baca_data_siswa
from src.proses import analisis_statistik, tentukan_ketuntasan, BATAS_KKM
from src.output import format_laporan, simpan_ke_file

def main():
    print("=== MENJALANKAN PROGRAM ANALISIS NILAI MATEMATIKA ===")
    file_input = "data/contoh_data.txt"
    file_output = "output/laporan.txt"

    # 1. Membaca dan memvalidasi data dari file[cite: 34]
    data_siswa = baca_data_siswa(file_input)
    if not data_siswa:
        print("[SISTEM] Program dihentikan karena data kosong atau berkas bermasalah[cite: 34].")
        return

    # 2. Proses perhitungan statistik dan ketuntasan[cite: 34]
    statistik = analisis_statistik(data_siswa)
    _, jumlah_tuntas = tentukan_ketuntasan(data_siswa, kkm=BATAS_KKM)

    # 3. Format hasil ke layar[cite: 34]
    teks_laporan = format_laporan(statistik, jumlah_tuntas, BATAS_KKM)
    print("\n" + teks_laporan)

    # 4. Simpan laporan ke berkas[cite: 34, 35]
    simpan_ke_file(file_output, teks_laporan)

if __name__ == "__main__":
    main()