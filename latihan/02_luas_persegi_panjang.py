
def luas_persegi_panjang(p, l):
    return p * l


print("Menghitung Luas Persegi Panjang")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = luas_persegi_panjang(panjang, lebar)

print("\nHasil Perhitungan")
print("Panjang :", panjang)
print("Lebar   :", lebar)
print("Luas    :", luas)