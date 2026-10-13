# Pertemuan 07 — Fungsi Python

**Nama:** Firgi Erviansyah
**NIM:** 2225250170  
**Kelas:** 3B

## Tujuan

Praktik ini bertujuan untuk memahami penggunaan fungsi dalam Python, meliputi definisi fungsi, parameter, argumen, return value, dan scope variabel. Program dibuat secara modular agar kode lebih mudah dibaca, diuji, diperbaiki, dan digunakan kembali.

## Struktur Folder

```text
pertemuan-07-fungsi-NIM/
|
|-- README.md
|-- .gitignore
|-- Kuis.docx
|
|-- latihan/
|   |-- 01_salam.py
|   |-- 02_luas_persegi_panjang.py
|   |-- 03_jumlah_n.py
|   |-- 04_statistik_sederhana.py
|   `-- 05_scope.py
|
`-- praktik/
    `-- utilitas_matematika.py
```

## Cara Menjalankan

Pastikan Python 3 sudah terpasang dan folder proyek telah dibuka di Visual Studio Code.

Untuk menjalankan Latihan 5, gunakan terminal:

```bash
python latihan/05_scope.py
```

Untuk menjalankan Praktik 2, gunakan perintah:

```bash
python praktik/utilitas_matematika.py
```

Jika perintah `python` tidak tersedia, coba gunakan `python3`.

Program praktik akan menampilkan menu operasi matematika. Pengguna dapat memilih operasi dan memasukkan angka sesuai permintaan program.

## Struktur Fungsi

### 1. Latihan 5 — Eksperimen Scope

File: `latihan/05_scope.py`

Program ini menggunakan fungsi `demo(x)` untuk menunjukkan perbedaan variabel di luar fungsi dan parameter di dalam fungsi.

- `demo(x)`: menerima parameter `x`, menghitung nilai `y = x + 5`, menampilkan nilai di dalam fungsi, dan mengembalikan `y` menggunakan `return`.
- `hasil`: menyimpan nilai yang dikembalikan oleh fungsi.
- `x`: variabel di luar fungsi tetap memiliki nilai awalnya meskipun fungsi menggunakan parameter dengan nama yang sama.

### 2. Praktik 2 — Utilitas Matematika Modular

File: `praktik/utilitas_matematika.py`

| Fungsi | Parameter | Kegunaan dan return value |
|---|---|---|
| `luas_persegi_panjang(p, l)` | Panjang dan lebar | Mengembalikan hasil perkalian panjang dan lebar. |
| `luas_segitiga(a, t)` | Alas dan tinggi | Mengembalikan hasil perhitungan luas segitiga. |
| `jumlah_n(n)` | Bilangan bulat `n` | Mengembalikan jumlah bilangan dari 1 sampai `n`. |
| `faktorial(n)` | Bilangan bulat `n` | Mengembalikan hasil faktorial menggunakan perulangan. |
| `tampilkan_menu()` | Tidak ada | Menampilkan pilihan operasi matematika. |
| `main()` | Tidak ada | Mengatur input pengguna, pemilihan operasi, validasi, dan penampilan hasil. |

Fungsi perhitungan menggunakan `return` agar hasilnya dapat digunakan kembali. Program juga menggunakan seleksi `if-elif-else`, perulangan, dan penanganan kesalahan input.

## Hasil Pengujian

### 1. Latihan 5 — Eksperimen Scope

| Input | Hasil yang diharapkan | Status |
|---|---|---|
| Nilai `x` di luar fungsi = 10; nilai untuk fungsi = 20 | Nilai `x` di dalam fungsi = 20, nilai `y` = 25, nilai `x` di luar fungsi = 10, dan `hasil` = 25. | Sesuai jika hasil aktual sama. |

### 2. Praktik 2 — Utilitas Matematika

| Operasi | Input | Hasil yang diharapkan | Status |
|---|---|---|---|
| Luas persegi panjang | Panjang = 8, lebar = 5 | 40.0 | Sesuai jika hasil aktual sama. |
| Luas segitiga | Alas = 10, tinggi = 6 | 30.0 | Sesuai jika hasil aktual sama. |
| Jumlah 1 sampai n | n = 10 | 55 | Sesuai jika hasil aktual sama. |
| Faktorial | n = 5 | 120 | Sesuai jika hasil aktual sama. |
| Faktorial | n = 0 | 1 | Sesuai jika hasil aktual sama. |

Status pengujian akhir diisi berdasarkan hasil aktual setelah program dijalankan di VS Code.

## Refleksi

Melalui latihan dan praktik ini, saya mempelajari bahwa fungsi dapat digunakan untuk membagi program menjadi bagian-bagian yang memiliki tugas tertentu. Penggunaan parameter memungkinkan fungsi menerima data yang berbeda, sedangkan `return` memungkinkan hasil perhitungan digunakan kembali.

Saya juga memahami bahwa variabel lokal memiliki ruang lingkup di dalam fungsi sehingga tidak dapat diakses langsung dari luar fungsi. Dengan menggunakan fungsi, program menjadi lebih terstruktur, mudah dibaca, dan lebih mudah diuji.