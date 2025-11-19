buahBuah = {
    'apel': 5000,
    'pisang': 3000,
    'jeruk': 7000,
    'anggur': 15000
}

def totalHarga():
    sum = 0
    for buah in buahBuah:
        sum += buahBuah[buah]

def tampilkanTotalBelanja():
    print(buahBuah)

def tambahBuah(nama, harga):
    buahBuah[nama] = harga
