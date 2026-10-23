# List soal (ditambahkan 2 soal baru di baris ke-4 dan ke-5)
soal = [
    "Ibu kota Indonesia adalah?",
    "2 + 2 * 3 hasilnya adalah?",
    "Tipe data untuk teks pada Python disebut?",
    "Simbol untuk komentar satu baris di Python adalah?",
    "Fungsi untuk menampilkan teks ke layar adalah?"
]

# List kunci jawaban (harus seimbang/sama jumlahnya dengan list soal)
kunci = [
    "Jakarta",
    "8",
    "string",
    "#",
    "print"
]

skor = 0

# Perulangan untuk menampilkan soal satu per satu
for nomor in range(len(soal)):
    print(f"\nSoal {nomor + 1}: {soal[nomor]}")
    jawaban = input("Jawaban Anda: ")
    
    # Pemeriksaan jawaban (case-insensitive & mengabaikan spasi berlebih)
    if jawaban.strip().lower() == kunci[nomor].lower():
        print("Benar!")
        skor += 1
    else:
        print(f"Salah. Jawaban benar: {kunci[nomor]}")

# Menampilkan skor akhir
print(f"\nSkor akhir: {skor}/{len(soal)}")