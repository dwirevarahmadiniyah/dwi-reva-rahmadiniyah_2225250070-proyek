# Dokumentasi Hasil Pengujian (Test Case) Proyek Akhir

Berikut adalah tabel pengujian fitur program yang mencakup kondisi normal, batas (*boundary*), dan invalid[cite: 32, 35, 36]:

| ID | Fitur | Input / Kondisi | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | Rata-rata | Nilai: `80, 60, 100, 45, 75` | Rata-rata terhitung `72.0` | Rata-rata terhitung `72.0` | **PASS** |
| **TC02** | Batas KKM | Nilai tepat: `0`[cite: 32] | Diterima sebagai nilai valid | Diterima sebagai nilai valid | **PASS** |
| **TC03** | Batas KKM | Nilai tepat: `100`[cite: 32] | Diterima sebagai nilai valid | Diterima sebagai nilai valid | **PASS** |
| **TC04** | Validasi Input | Nilai invalid: `105` (di luar rentang) | Ditolak oleh fungsi validasi | Ditolak oleh fungsi validasi | **PASS**[cite: 36] |
| **TC05** | Penanganan File | Berkas sumber tidak ada (`salah.txt`) | Menangani `FileNotFoundError` tanpa *crash*[cite: 36] | Menampilkan pesan error berkas tidak ditemukan | **PASS**[cite: 36] |
| **TC06** | Kondisi Kosong | List nilai kosong `[]` | Mengembalikan nilai rata-rata `0.0` | Mengembalikan nilai rata-rata `0.0` | **PASS**[cite: 36] |

## Catatan Bug Log[cite: 37]
| ID Bug | Gejala | Penyebab | Perbaikan | Status |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Potensi pembagian dengan nol saat list data kosong[cite: 36] | Fungsi `hitung_rata_rata` langsung membagi dengan `len(data)`[cite: 36] | Menambahkan pengecekan kondisi `if not data: return 0.0`[cite: 36] | **Closed**[cite: 37] |