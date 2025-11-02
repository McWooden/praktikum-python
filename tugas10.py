# 100% gapake ai, berotak senku :D
# Created by Huddin
# MIT Licence

# 1. Tuples:
# a. buat tuple mahasiswa (Nama, NIM, Prodi)
mahasiswa = ("Sholahuddin Ahmad", "2505060070", "Teknologi Informasi")
# b. Tampilkan NIM dan Prodi
print(mahasiswa[1])
print(mahasiswa[2])

# 2. Dictionary:
# a. Buat dictionary keranjang dengan data buah-buahan
buahBuah = {
    'apel': 5000,
    'pisang': 3000,
    'jeruk': 7000,
    'anggur': 15000
}

# Setup memori
memori_total_barang = 0
memori_tampilkan_buah = ''
memori_total_harga = 0

# Mari kita buat loopingnya
for barang, value in buahBuah.items():
    # b. Gunakan perulangan untuk menghitung semua barang
    memori_total_barang += 1
    # c. Tampilkan setiap barang dan harga dalam format: ex:"Harga apel: Rp 5000"
    memori_tampilkan_buah += f'Harga {barang}\t: Rp {value}\n'
    # d. Tampilkan harga total belanja
    memori_total_harga += value

print('a.', buahBuah)
# Sebenernya bisa pakai len(), tapi baiklah, aku udah buat memori di setup
print('b.', memori_total_barang)
# ini gatau kenapa aku kepikiran pake ini, daripada pake array kudu di looping dulu makannya aku tambahin ke string
print('c.', memori_tampilkan_buah)
# ini yang d bisa aja sih pake -> print(sum(buahBuah.values()))
print('d.', memori_total_harga)
