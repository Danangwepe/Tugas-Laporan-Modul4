from cek import *

poinkeamanan = int(0)
mauUlang = bool(True)

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