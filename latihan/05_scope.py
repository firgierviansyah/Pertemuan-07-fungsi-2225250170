
# Latihan 5: Eksperimen Scope

x = int(input("Masukkan nilai x di luar fungsi: "))


def demo(x):
    y = x + 5
    print("Di dalam fungsi:")
    print("Nilai x =", x)
    print("Nilai y =", y)
    return y


nilai_fungsi = int(input("Masukkan nilai x untuk fungsi: "))

hasil = demo(nilai_fungsi)

print("\nDi luar fungsi:")
print("Nilai x =", x)
print("Nilai hasil =", hasil)