
def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


print("Menghitung Jumlah 1 sampai N")

n = int(input("Masukkan nilai N: "))

if n >= 1:
    hasil = jumlah_n(n)

    print("\nHasil Perhitungan")
    print("Nilai N :", n)
    print("Jumlah  :", hasil)
else:
    print("Nilai N harus lebih besar atau sama dengan 1.")