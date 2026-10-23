
harga_satuan = int(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah barang: "))
persen_diskon = float(input("Masukkan persentase diskon (%): "))
subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * (persen_diskon / 100)
total_bayar = subtotal - nominal_diskon
print(f"subtotal = Rp{int(subtotal):,}".replace(",", "."))
print(f"diskon = Rp{int(nominal_diskon):,}".replace(",", "."))
print(f"total bayar = Rp{int(total_bayar):,}".replace(",", "."))