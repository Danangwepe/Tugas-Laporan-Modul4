def cekAngka(password):
    if any(i in password for i in "1234567890"):
        return True
    else:
        return False

def cekKarakterUnik(password):
    if any(i in password for i in "@"):
        return True
    else:
        return False

def cekPanjangPass(password):
    if (len(password) > 8 and len(password) < 32):
        return True
    else:
        return False

def cekKarakterTerlarang(password):
    if any(i in password for i in "#$%^&*():;"):
        return True
    else:
        return False