# Inisialisasi list bertingkat nilai_kelas
nilai_kelas = [[80, 90], [75, 85], [88, 92]]

# 1. Menampilkan nilai pertama mahasiswa pertama (indeks baris 0, indeks elemen 0)
print(nilai_kelas[0][0])

# 2. Menampilkan nilai kedua mahasiswa ketiga (indeks baris 2, indeks elemen 1)
print(nilai_kelas[2][1])

# 3. Menghitung dan menampilkan rata-rata setiap mahasiswa menggunakan perulangan
for i, data in enumerate(nilai_kelas):
    rata_rata = sum(data) / len(data)
    print(f"Mahasiswa {i + 1}: {rata_rata}")