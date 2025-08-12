# Proxy Checker

Script ini digunakan untuk memeriksa apakah proxy yang diberikan dapat terdeteksi menggunakan API. Script akan membaca daftar proxy dari file input dan memeriksa setiap proxy menggunakan API, kemudian hasilnya akan disimpan dalam dua file output yang berbeda.

## Fitur:
- Membaca daftar proxy dari file input (misal: `proxy_list.txt`).
- Memeriksa proxy menggunakan API untuk menentukan apakah terdeteksi atau tidak.
- Menyimpan hasil dalam dua format:
  - **ip:port** (format dasar).
  - **ip,port,country,provider** (format dengan informasi tambahan).
- Menampilkan hasil pengecekan di terminal dengan warna hijau untuk proxy yang terdeteksi dan merah untuk yang tidak terdeteksi.
- Proses dilakukan secara paralel menggunakan `ThreadPoolExecutor` untuk meningkatkan kecepatan pengecekan.

## Persyaratan:
- Python 3.x
- Library Python:
  - `requests`
  - `concurrent.futures`
  
  Untuk menginstal library yang dibutuhkan, jalankan perintah berikut:
  ```bash
  pip install requests

## Penggunaan:
**Jalankan Script:**
```bash
python check-proxy.py
