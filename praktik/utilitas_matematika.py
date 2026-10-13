
# Praktik : Utilitas Matematika Modular


def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif")

    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif")

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")


def main():
    tampilkan_menu()
    pilihan = input("Pilih operasi (1-4): ")

    try:
        if pilihan == "1":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))

            if p < 0 or l < 0:
                print("Panjang dan lebar tidak boleh negatif.")
            else:
                hasil = luas_persegi_panjang(p, l)
                print("Luas persegi panjang =", hasil)

        elif pilihan == "2":
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))

            if a < 0 or t < 0:
                print("Alas dan tinggi tidak boleh negatif.")
            else:
                hasil = luas_segitiga(a, t)
                print("Luas segitiga =", hasil)

        elif pilihan == "3":
            n = int(input("Masukkan nilai n: "))
            print("Jumlah 1 sampai", n, "=", jumlah_n(n))

        elif pilihan == "4":
            n = int(input("Masukkan nilai n: "))
            print("Faktorial", n, "=", faktorial(n))

        else:
            print("Pilihan tidak valid. Pilih angka 1 sampai 4.")

    except ValueError as error:
        print("Input tidak valid:", error)


if __name__ == "__main__":
    main()