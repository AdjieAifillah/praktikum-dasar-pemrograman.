biaya_admin = 2500 #variabel global

def hitung_total(harga):
    total = harga + biaya_admin  # variabel lokal
    return total

print(hitung_total(15000))