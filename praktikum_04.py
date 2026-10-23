# Inisialisasi list nilai
nilai = [85, 70, 92, 60, 78]

# 1. Menghitung jumlah data (banyaknya elemen dalam list)
print("Jumlah data:", len(nilai))

# 2. Menghitung total (jumlah seluruh nilai)
print("Total:", sum(nilai))

# 3. Menghitung rata-rata
print("Rata-rata:", sum(nilai) / len(nilai))

# 4. Urutan naik (ascending)
print("Urut naik:", sorted(nilai))

# 5. Urutan turun (descending)
print("Urut turun:", sorted(nilai, reverse=True))

# 6. Menampilkan list asli (memastikan sorted() tidak mengubah list asli)
print("List asli:", nilai)