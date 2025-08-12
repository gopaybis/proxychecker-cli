import requests
import os
import concurrent.futures

# Fungsi untuk menampilkan teks dengan warna hijau
def print_green(message):
    print("\033[92m" + message + "\033[0m")  # Warna hijau

# Fungsi untuk menampilkan teks dengan warna merah
def print_red(message):
    print("\033[91m" + message + "\033[0m")  # Warna merah

# URL API yang baru untuk memeriksa proxy
url = "https://apihealtcheck-sigma.vercel.app/api/v1"

# Menyimpan hasil yang terdeteksi
results_ip_port = []
results_details = []

# Fungsi untuk memeriksa proxy
def check_proxy(proxy):
    ip, port = proxy.strip().split(":")
    params = {
        'ip': ip,
        'port': port
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

            # Memeriksa apakah proxy terdeteksi
            if data.get("proxyip") == True:
                # Format 1: ip:port
                results_ip_port.append(f"{ip}:{port}")

                # Format 2: ip,port,country,provider
                country = data.get("countryName", "Unknown")
                provider = data.get("asOrganization", "Unknown")
                results_details.append(f"{ip},{port},{country},{provider}")

                print_green(f"{ip}:{port}")  # Menampilkan hanya IP:Port jika terdeteksi
            else:
                print_red(f"{ip}:{port}")  # Menampilkan hanya IP:Port jika tidak terdeteksi
        else:
            print_red(f"{ip}:{port}")  # Menampilkan hanya IP:Port jika status code bukan 200
    except Exception as e:
        print_red(f"{ip}:{port}")  # Menampilkan hanya IP:Port jika ada kesalahan

# Mengambil nama file input dan output dari pengguna
input_file = input("Masukkan nama file input (misal: proxy_list.txt): ")
output_ip_port_file = input("Masukkan nama file output untuk format ip:port (misal: proxy_results_ip_port.txt): ")
output_details_file = input("Masukkan nama file output untuk format ip,port,country,provider (misal: proxy_results_details.txt): ")

if not os.path.exists(input_file):
    print(f"File {input_file} tidak ditemukan!")
else:
    with open(input_file, "r") as f:
        proxy_list = f.readlines()

    # Menyimpan hasil dalam format 1 dan 2 setelah proses selesai
    with open(output_ip_port_file, "w") as f1, open(output_details_file, "w") as f2:
        # Menggunakan ThreadPoolExecutor untuk menjalankan pengecekan secara paralel
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
            # Memulai pengecekan semua proxy secara paralel
            executor.map(check_proxy, proxy_list)

        # Menyimpan hasil setelah semua pengecekan selesai
        for result in results_ip_port:
            f1.write(result + "\n")
        for result in results_details:
            f2.write(result + "\n")

    # Keterangan hasil
    print(f"\nProses selesai. Hasil telah disimpan dalam file:\n{output_ip_port_file} (format ip:port)\n{output_details_file} (format ip,port,country,provider)")
