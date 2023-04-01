from cek import *

poinkeamanan = int(0)
mauUlang = bool(True)

#Kita buat function terlebih dahulu

def kriteriaPass():
    print("Kriteria Password")
    print("1. Password tidak boleh kurang dari 8 karakter dan tidak boleh lebih dari 32 karakter")
    print("2. Password tidak boleh menggunakan karakter terlarang")

def pilihUlang():
    pilihanulang = input(str("Apakah Anda ingin mengulangi pengecekan (Y/N): "))

    if (pilihanulang == "Y" or pilihanulang == "y"):
            return True
    else:
            return False

        
while (mauUlang == True):
    kriteriaPass()
    password = input(str("Masukkan password yang ingin dicek : "))
    panjangPass = cekPanjangPass(password)
    karakterTerlarang = cekKarakterTerlarang(password)

    if (panjangPass == True and karakterTerlarang == False):
        adaAngka = cekAngka(password)
        adakarakterunik = cekKarakterUnik(password)

        if adaAngka == True:
            print("Password anda sudah memiliki Angka")
            poinkeamanan += 10
        else:
            print("Password anda belum memiliki Angka")

        if adakarakterunik == True:
            print("Password anda sudah ada karakter unik")
            poinkeamanan += 10
        else:
            print("Password anda belum memiliki karakter unik")
    
        if (poinkeamanan == 20):
            print("Password anda sangat kuat")
        elif(poinkeamanan == 10):
            print("Password anda lumayan kuat")
        else:
            print("Password anda masih lemah")

        mauUlang = pilihUlang()
    
        else:
            print("Maaf password anda tidak memenuhi syarat")

        mauUlang = pilihUlang()
