import os

# Fungsi untuk membersihkan layar (dipakai hanya sekali di awal)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Fungsi Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if data[mid] == target:
            return mid, count
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, count


# ===================== PROGRAM UTAMA =====================

clear_screen()

print("Nama: Indira Suci")
print("NIM: 552010125006")
print("=== PROGRAM BINARY SEARCH ===")
print("Catatan: Data akan diurutkan otomatis\n")

while True:
    # input data
    data_input = input("\nMasukkan data: ")
    data = list(map(int, data_input.split()))
    data.sort()

    # input target
    target = int(input("Masukkan angka yang dicari: "))

    print("\nData terurut:", data)

    posisi, langkah = binary_search(data, target)

    print("\n=== HASIL PENCARIAN ===")
    print("Posisi:", posisi)
    print("Jumlah langkah:", langkah)

    if posisi == -1:
        print("Hasil: Data tidak ditemukan")
    else:
        print(f"Hasil: Data ditemukan pada indeks {posisi}")

    # pilihan ulang
    ulang = input("\nIngin mencari lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Program selesai.")
        break
