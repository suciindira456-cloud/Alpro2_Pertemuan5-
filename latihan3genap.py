import os

# ================= CLEAR TERMINAL =================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# DATA GENAP 2 SAMPAI 100
data = list(range(2, 101, 2))


# ================= LINEAR SEARCH =================
def linear_search(data, target):
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i] == target:
            return i, count
    return -1, count


# ================= BINARY SEARCH =================
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


# ================= PROGRAM =================
while True:
    clear_screen()
    print("DATA:", data)
    print("\n=== PERBANDINGAN LINEAR VS BINARY SEARCH ===\n")

    target = int(input("Masukkan angka yang ingin dicari (0 untuk keluar): "))

    if target == 0:
        print("Program selesai.")
        break

    # Proses pencarian
    lin_pos, lin_step = linear_search(data, target)
    bin_pos, bin_step = binary_search(data, target)

    clear_screen()
    print("DATA:", data)
    print("\n=== HASIL PENCARIAN ===\n")
    print(f"Target: {target}")
    print(f"Linear Search  -> Posisi: {lin_pos}, Langkah: {lin_step}")
    print(f"Binary Search  -> Posisi: {bin_pos}, Langkah: {bin_step}")

    input("\nTekan ENTER untuk lanjut...")
