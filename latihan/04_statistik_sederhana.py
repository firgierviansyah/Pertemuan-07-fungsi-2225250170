
def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]

    for x in data:
        total += x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    rata_rata = total / len(data)

    return minimum, maksimum, rata_rata


print("Statistik Sederhana")

jumlah_data = int(input("Berapa banyak data yang ingin dimasukkan? "))

if jumlah_data > 0:
    data = []

    for i in range(jumlah_data):
        nilai = float(input(f"Masukkan data ke-{i + 1}: "))
        data.append(nilai)

    minimum, maksimum, rata_rata = statistik(data)

    print("\nHasil Statistik")
    print("Data        :", data)
    print("Nilai minimum:", minimum)
    print("Nilai maksimum:", maksimum)
    print("Rata-rata    :", rata_rata)
else:
    print("Jumlah data harus lebih dari 0.")