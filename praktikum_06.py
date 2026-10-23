# Inisialisasi list nama mahasiswa
nama_mahasiswa = ["Ayu", "Bima", "Citra", "Doni"]

# Minta input nama yang ingin dicari dari pengguna
cari = input("Nama yang dicari: ")

# Menggunakan operator 'in' untuk memeriksa keberadaan data di dalam list
if cari in nama_mahasiswa:
    print("Nama ditemukan")
else:
    print("Nama tidak ditemukan")