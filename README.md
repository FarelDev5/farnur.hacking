# FARNUR HACKING

**FARNUR HACKING** adalah alat multifungsi yang membantu pengguna dalam melakukan pelacakan IP, GeoIP lookup, pemindaian port, konversi teks ke ASCII, dan berbagai fungsi lainnya yang bermanfaat dalam pengujian jaringan atau eksplorasi informasi IP. Alat ini dirancang agar kompatibel dengan Termux dan Linux.

## Fitur
1. **IP Tracking** - Melacak lokasi alamat IP dan melihatnya di Google Maps.
2. **GeoIP Lookup** - Mendapatkan informasi rinci dari alamat IP, termasuk lokasi dan organisasi.
3. **Port Scanner** - Memindai port yang terbuka pada alamat IP yang ditentukan.
4. **ASCII Converter** - Mengonversi teks ke kode ASCII untuk setiap karakter.
5. **Run Command** - Menjalankan perintah shell dalam alat ini.

## Persyaratan
- **Python 3.6** atau versi lebih baru
- Koneksi internet (untuk fitur IP tracking dan GeoIP lookup)
- **pip** untuk menginstal dependensi Python

## Instalasi

### 1. Termux
1. Perbarui dan tingkatkan paket Termux:
    ```bash
    pkg update && pkg upgrade
    ```

2. Instal Python dan Git:
    ```bash
    pkg install python
    pkg install git
    ```

3. Clone repository:
    ```bash
    git clone https://github.com/FarelDev5/farnur.hacking.git
    ```

4. Masuk ke direktori `farnur.hacking`:
    ```bash
    cd farnur.hacking
    ```

5. Instal dependensi Python:
    ```bash
    pip install -r requirements.txt
    ```

6. Jalankan alat:
    ```bash
    python farnur.py
    ```

### 2. Linux
1. Perbarui dan tingkatkan paket:
    ```bash
    sudo apt update && sudo apt upgrade
    ```

2. Instal Python dan Git:
    ```bash
    sudo apt install python3 python3-pip git
    ```

3. Clone repository:
    ```bash
    git clone https://github.com/FarelDev5/farnur.hacking.git
    ```

4. Masuk ke direktori `farnur.hacking`:
    ```bash
    cd farnur.hacking
    ```

5. Instal dependensi Python:
    ```bash
    pip3 install -r requirements.txt
    ```

6. Jalankan alat:
    ```bash
    python3 farnur.py
    ```

## Penggunaan
Setelah menjalankan alat, Anda akan melihat logo dan menu dengan opsi berikut:
- **1. IP Tracking:** Masukkan alamat IP untuk melacak lokasinya.
- **2. GeoIP Lookup:** Masukkan IP untuk informasi rinci tentang lokasinya.
- **3. Port Scanner:** Masukkan IP untuk memindai port yang terbuka.
- **4. ASCII Converter:** Mengonversi teks input menjadi kode ASCII.
- **5. Run Command:** Menjalankan perintah shell di dalam alat.
- **6. Exit:** Keluar dari program.

Setiap fitur dapat diakses dengan memilih nomor yang sesuai dari menu.

## Pembuat
Dibuat oleh Farel Alfareza  
Instagram/TikTok: [@farel.project_5](https://instagram.com/farel.project_5)
