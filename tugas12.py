# Link Tugas https://drive.google.com/file/d/1P8BTsMXpr0thyzCeOfeHYGOu_E1FuX5i/view
# Materinya udah aku jelasin di Medium sebelumnya: https://medium.com/@halohuddin/modul-rakitan-fun-fun-function-10f159abfe76

# Note: Simple aja, kalian tinggal bikin fungsi sesuai instruksi di artikel Medium di atas
# Cara bikinnya tinggal bikin terima input dari user terus return rumusnya

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

# Contoh pemanggilan fungsi
print("Luas Persegi Panjang:", luas_persegi_panjang())
print("Volume Balok:", volume_balok())
print("Luas Lingkaran:", luas_lingkaran())
print("Volume Bola:", volume_bola())