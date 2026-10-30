def validasi_nilai(nilai_str):
    """Memvalidasi apakah input angka dan berada pada rentang 0 sampai 100[cite: 32]."""
    try:
        nilai = float(nilai_str)
        if 0 <= nilai <= 100:
            return True, nilai
        return False, None
    except ValueError:
        return False, None

def baca_data_siswa(path_file):
    """Membaca data dari file teks eksternal dan mengembalikan dictionary data valid[cite: 34, 35]."""
    data_siswa = {}
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                parts = baris.split(',')
                if len(parts) == 2:
                    nama = parts[0].strip()
                    is_valid, nilai = validasi_nilai(parts[1].strip())
                    if is_valid:
                        data_siswa[nama] = nilai
        return data_siswa
    except FileNotFoundError:
        print(f"[ERROR] Berkas '{path_file}' tidak ditemukan.")
        return None