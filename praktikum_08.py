# Inisialisasi list angka dari 1 sampai 10
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. List comprehension untuk menyaring bilangan genap
genap = [x for x in angka if x % 2 == 0]

# 2. List comprehension untuk menghitung kuadrat semua angka
kuadrat = [x ** 2 for x in angka]

# Menampilkan hasil
print("Genap:", genap)
print("Kuadrat:", kuadrat)