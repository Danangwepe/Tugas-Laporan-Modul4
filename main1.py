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