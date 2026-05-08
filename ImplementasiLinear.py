import os

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def linear_search(data, target):
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i] == target:
            return i, count
    return -1, count


# ===================== PROGRAM UTAMA =====================

# Data tetap
data = [4, 8, 15, 16, 23, 42]

# Bersihkan layar hanya sekali di awal
clear_screen()

print("Nama: Indira Suci")
print("NIM: 552010125006")
print("=== PROGRAM LINEAR SEARCH ===")

while True:
    # tampilkan data setiap pencarian
    print("\nData:", data)

    # input target
    target = int(input("Masukkan angka yang dicari: "))

    posisi, langkah = linear_search(data, target)

    print("\n=== HASIL ===")
    print("Posisi         :", posisi)
    print("Jumlah langkah :", langkah)

    if posisi == -1:
        print("Hasil: Data tidak ditemukan")
    else:
        print(f"Hasil: Data ditemukan pada indeks {posisi}")

    # pilihan ulang
    ulang = input("\nIngin mencari lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Program selesai.")
        break
