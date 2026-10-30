BATAS_KKM = 75

def hitung_rata_rata(nilai_list):
    """Menghitung rata-rata nilai numerik dengan penanganan list kosong[cite: 34, 35, 36]."""
    if not nilai_list:
        return 0.0
    return sum(nilai_list) / len(nilai_list)

def analisis_statistik(data_siswa):
    """Memproses statistik kelas: rata-rata, min, max, dan total siswa[cite: 34, 35]."""
    if not data_siswa:
        return None
    
    nilai_list = list(data_siswa.values())
    return {
        "total": len(nilai_list),
        "rata_rata": hitung_rata_rata(nilai_list),
        "minimum": min(nilai_list),
        "maksimum": max(nilai_list)
    }

def tentukan_ketuntasan(data_siswa, kkm=BATAS_KKM):
    """Menentukan status tuntas/belum tuntas berdasarkan KKM[cite: 34, 35]."""
    hasil_ketuntasan = {}
    jumlah_tuntas = 0
    
    for nama, nilai in data_siswa.items():
        if nilai >= kkm:
            status = "Tuntas"
            jumlah_tuntas += 1
        else:
            status = "Belum Tuntas"
        hasil_ketuntasan[nama] = {"nilai": nilai, "status": status}
        
    return hasil_ketuntasan, jumlah_tuntas