# farnur.hacking
Hacking IP Adress

# FARNUR

**FARNUR** is a multifunctional tool designed to help you with various tasks like IP tracking, GeoIP lookup, port scanning, ASCII text conversion, and more. This tool was built to run on both Termux and Linux, providing a user-friendly interface with gradient logos and dynamic menus.

**FARNUR** adalah alat multifungsi yang dirancang untuk membantu Anda dalam berbagai tugas seperti pelacakan IP, GeoIP lookup, pemindaian port, konversi teks ke ASCII, dan lainnya. Alat ini dibuat untuk berjalan di Termux dan Linux, dengan antarmuka yang ramah pengguna, logo gradasi, dan menu dinamis.

## Features / Fitur
1. **IP Tracking** - Track the location of any IP address and view it on Google Maps.  
   **Pelacakan IP** - Melacak lokasi alamat IP dan melihatnya di Google Maps.
2. **Date & Time** - Display the current date and time.  
   **Tanggal & Waktu** - Menampilkan tanggal dan waktu saat ini.
3. **Run Command** - Execute shell commands within the tool.  
   **Menjalankan Perintah** - Menjalankan perintah shell dalam alat ini.
4. **GeoIP Lookup** - Get detailed information on an IP address, including location and organization.  
   **Pencarian GeoIP** - Mendapatkan informasi rinci dari alamat IP, termasuk lokasi dan organisasi.
5. **Port Scanner** - Scan the first 1024 ports of a specified IP address.  
   **Pemindai Port** - Memindai 1024 port pertama dari alamat IP yang ditentukan.
6. **ASCII Converter** - Convert text to ASCII codes for individual characters.  
   **Konverter ASCII** - Mengonversi teks ke kode ASCII untuk setiap karakter.

## Requirements / Persyaratan

To run this tool, you need:  
Untuk menjalankan alat ini, Anda memerlukan:
- Python 3.6 or higher / Python 3.6 atau lebih tinggi
- **pip** to install dependencies / **pip** untuk menginstal dependensi
- Internet connection for certain features (like IP tracking and GeoIP)  
  Koneksi internet untuk fitur tertentu (seperti pelacakan IP dan GeoIP)

## Installation Instructions / Instruksi Instalasi

### 1. Termux
1. Update and upgrade Termux packages:  
   Perbarui dan tingkatkan paket Termux:
    ```bash
    pkg update && pkg upgrade
    ```

2. Install Python and necessary packages:  
   Instal Python dan paket yang diperlukan:
    ```bash
    pkg install python
    pkg install git
    ```

3. Clone the repository:  
   Clone repository:
    ```bash
    git clone https://github.com/FarelDev5/farnur.hacking
    ```

4. Change directory to the project folder:  
   Ubah direktori ke folder proyek:
    ```bash
    cd ip_tracker
    ```

5. Install Python dependencies:  
   Instal dependensi Python:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the tool:  
   Jalankan alat:
    ```bash
    python farnur.py
    ```

### 2. Linux
1. Update and upgrade packages:  
   Perbarui dan tingkatkan paket:
    ```bash
    sudo apt update && sudo apt upgrade
    ```

2. Install Python and git:  
   Instal Python dan git:
    ```bash
    sudo apt install python3 python3-pip git
    ```

3. Clone the repository:  
   Clone repository:
    ```bash
    git clone https://github.com/FarelDev5/farnur.hacking
    ```

4. Change directory to the project folder:  
   Ubah direktori ke folder proyek:
    ```bash
    cd ip_tracker
    ```

5. Install Python dependencies:  
   Instal dependensi Python:
    ```bash
    pip3 install -r requirements.txt
    ```

6. Run the tool:  
   Jalankan alat:
    ```bash
    python3 farnur.py
    ```

## Usage / Penggunaan
Upon running the tool, you will see a logo and menu with the following options:  
Setelah menjalankan alat, Anda akan melihat logo dan menu dengan opsi berikut:
- **1. IP Tracking:** Enter an IP address to track its location.  
  **1. Pelacakan IP:** Masukkan alamat IP untuk melacak lokasinya.
- **2. Date & Time:** Displays the current date and time.  
  **2. Tanggal & Waktu:** Menampilkan tanggal dan waktu saat ini.
- **3. Run Command:** Allows you to run shell commands within the tool.  
  **3. Menjalankan Perintah:** Memungkinkan Anda menjalankan perintah shell di dalam alat.
- **4. GeoIP Lookup:** Enter an IP for detailed information about its location.  
  **4. Pencarian GeoIP:** Masukkan IP untuk informasi rinci tentang lokasinya.
- **5. Port Scanner:** Enter an IP to scan for open ports.  
  **5. Pemindai Port:** Masukkan IP untuk memindai port yang terbuka.
- **6. ASCII Converter:** Converts input text to ASCII codes.  
  **6. Konverter ASCII:** Mengonversi teks input menjadi kode ASCII.
- **7. Exit:** Exit the program.  
  **7. Keluar:** Keluar dari program.

Each feature can be accessed by selecting the respective number from the menu.  
Setiap fitur dapat diakses dengan memilih nomor yang sesuai dari menu.

## Author / Pembuat
Created by Farel Alfareza  
Dibuat oleh Farel Alfareza  
Instagram/TikTok: [@farel.project_5](https://instagram.com/farel.project_5)

