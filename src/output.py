def format_laporan(statistik, jumlah_tuntas, kkm):
    """Memformat hasil analisis statistik menjadi string teks laporan[cite: 35]."""
    laporan = "=" * 45 + "\n"
    laporan += "      LAPORAN ANALISIS NILAI MATEMATIKA\n"
    laporan += "=" * 45 + "\n"
    laporan += f"Batas KKM            : {kkm}\n"
    laporan += f"Total Siswa Valid    : {statistik['total']}\n"
    laporan += f"Rata-rata Kelas      : {statistik['rata_rata']:.2f}\n"
    laporan += f"Nilai Tertinggi      : {statistik['maksimum']}\n"
    laporan += f"Nilai Terendah       : {statistik['minimum']}\n"
    laporan += f"Jumlah Siswa Tuntas  : {jumlah_tuntas}\n"
    laporan += "=" * 45 + "\n"
    return laporan

def simpan_ke_file(path_output, teks_laporan):
    """Menyimpan hasil laporan ke dalam berkas teks di direktori output[cite: 35]."""
    try:
        import os
        os.makedirs(os.path.dirname(path_output), exist_ok=True)
        with open(path_output, 'w', encoding='utf-8') as file:
            file.write(teks_laporan)
        print(f"[INFO] Laporan berhasil disimpan ke '{path_output}'.")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan berkas: {e}")