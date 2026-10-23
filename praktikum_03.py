# Inisialisasi awal list
daftar_matkul = ['Algoritma', 'Tipe Data']

# 1. Tambahkan 'Basis Data' di akhir
daftar_matkul.append('Basis Data')
print(daftar_matkul)

# 2. Sisipkan 'Pemrograman' pada indeks 1
daftar_matkul.insert(1, 'Pemrograman')
print(daftar_matkul)

# 3. Hapus elemen pada indeks 0 menggunakan del
del daftar_matkul[0]
print(daftar_matkul)

# 4. Hapus elemen terakhir menggunakan pop()
terhapus = daftar_matkul.pop()
print("Terhapus:", terhapus)
print(daftar_matkul)