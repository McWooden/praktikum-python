def luas_persegi_panjang():
    print("Waktunya menghitung luas persegi panjang")

    panjang = int(input("Panjang\t:"))
    lebar = int(input("Lebar\t:"))

    return panjang * lebar

def volume_balok():
    print("Waktunya menghitung volume balok")

    panjang = int(input("Panjang\t:"))
    lebar = int(input("Lebar\t:"))
    tinggi = int(input("Tinggi\t:"))
    return panjang * lebar * tinggi

def luas_lingkaran():
    print("Waktunya menghitung luas lingkaran")

    jari_jari = int(input("Jari-jari\t:"))
    return 3.14 * jari_jari**2

def volume_bola():
    print("Waktunya menghitung volume bola")

    jari_jari = int(input("Jari-jari\t:"))
    return .75 * 3.14 * jari_jari**3

print(luas_lingkaran())