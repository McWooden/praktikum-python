import random
import string

# Persiapan
gudang = {
    "ASDJBT": {
        "nama": "Baju Tidur",
        "harga": 75000,
        "stok": 10
    },
    "HASDHB": {
        "nama": "Karung Bantal",
        "harga": 10000,
        "stok": 8
    }
}
# a. Tambah barang (kode, nama, harga, stok)
def tambah_barang():
    kode = "".join([random.choice(string.ascii_uppercase) for i in range(6)])
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    gudang[kode] = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

# b. Hapus barang berdasarkan kode
def hapus_barang(kode):
    del gudang[kode]

# c. Cari barang berdasarkan nama
def cari_barang(nama):
    for barang in gudang:
        if (barang.nama == nama):
            return barang

# d. Tampilkan semua barang dengan stok kurang dari 5
def tampilkan_stok_kurang_dari_5():
    for barang in gudang:
        if (barang.stok < 5):
            return barang

# e. Urutkan barang berdasarkan harga (termahal → termurah)
def urutkan_berdasarkan_harga():
    gudang_list = []
    
    # pindahin setiap barang dari dictionary ke list
    for kode, value in gudang.items():
        # **value itu buat naikin tingkat dictionary
        item = {"kode": kode, **value}
        # masukin item baru ke list
        gudang_list.append(item)

    ## Fungsi ini untuk mengambil harga dari item
    def ambil_harga(barang):
        return barang["harga"]

    ## ini mengurutkan berdasarkan harga
    gudang_list.sort(key=ambil_harga)

    ## karena sudah urut dari termurah, mari kita balikkan supaya dari yang termahal ke termurah
    gudang_list.reverse()
    
    return gudang_list

print(urutkan_berdasarkan_harga())