# Link: https://drive.google.com/file/u/3/d/1tdfA9NgH6iBTSxQVRQONtDacq-1EhN1H/view?usp=classroom_web&pli=1
# Note: Gampang aja, kalian tinggal copy paste kodingan dari tugas 10 sebelumnya di Google Colab

# import module yang dibutuhkan
import datetime
import random
import string

# lemari buku sebagai database
lemari = {}

print("Selamat datang di dashboard Kapten!")
print("Pasti ingin mengelola lemari buku ini!\n")

while True:
    print("Silahkan tambah buku baru")
    # buat buku baru, logika: mulai bikin dictionary kosong, ntar di isi pake input
    buku_baru = {}

    # perbarui buku_baru dengan data baru
    buku_baru["judul"] = input("Masukkan judul buku: ")
    buku_baru["penulis"] = input("Masukkan penulis buku: ")
    buku_baru["tahun_terbit"] = input("Masukkan tahun terbit buku: ")

    # minta tanggal terakhir dipinjam
    tahun = int(input("Masukkan tahun terakhir dipinjam (YYYY): "))
    bulan = int(input("Masukkan bulan terakhir dipinjam (1-12): ")) 
    tanggal = int(input("Masukkan tanggal terakhir dipinjam (1-31): "))
    buku_baru["tanggal_terakhir_dipinjam"] = datetime.datetime(tahun, bulan, tanggal)

    # minta status ketersediaan
    dipinjam = input("Apakah buku tersedia? (y/n): ").lower()
    if dipinjam == "y":
        buku_baru["status"] = True
    else:
        buku_baru["status"] = False

    # buat key buat akses buku baru, logika: dia bakal milih huruf kapital 6 kali -> awalnya looping dapet karakter acak di dalem list, misal ["H", "U", "D", "D", "I", "N"], terus di gabungin pake join jadi string "HUDDIN"
    key = "".join([random.choice(string.ascii_uppercase) for i in range(6)])

    # tambahin ke lemari, logika: lemari dengan key yang baru aja dibuat ditempati buku baru
    lemari[key] = buku_baru
    print("\nBuku berhasil ditambahkan dengan key:", key)

    # tampilkan lemari pake tabel
    print("\nDaftar Buku di Lemari:\n")
    print(f"{'KODE':<8} {'JUDUL':<25} {'PENULIS':<20} {'TAHUN':<6} {'TERAKHIR DIPINJAM':<18} {'STATUS':<10}")
    print("-" * 90)
    for kode, data in lemari.items():
        terakhir_dipinjam = data['tanggal_terakhir_dipinjam'].strftime("%Y-%m-%d")
        status = "Tersedia" if data['status'] else "Tidak"
        print(f"{kode:<8} {data['judul']:<25} {data['penulis']:<20} {data['tahun_terbit']:<6} {terakhir_dipinjam:<18} {status:<10}")

    # tanya user mau nambah buku lagi atau gak
    lagi = input("\nMau tambah buku lagi? (y/n): ").lower()
    if lagi != "y":
        print("Terima kasih Kapten, silahkan datang kembali!")
        break








# Catatan logika:
# 1. pakai uuid lebih anti konflik double key daripada string + random number, tapi yaudahlah ya.. ini cuma tugas sederhana
# 2. kalo ada format kayak "data['judul']:<25", itu maksudnya bikin kolom 25 karekter, terus rata kekiri(<), kalo kanan ya >, kalo tengah ^
