def tampilkan_nama(nama_list):    #fungsi untuk menampilkan daftar nama
    for nama in nama_list:
        print(nama)

nama_list = ["andi", "budi", "didi"]
tampilkan_nama(nama_list)
print("============================")
def urutkan_daftar(daftar):   #fungsi untuk mengurutkan daftar
    return sorted(daftar)
daftar = [10, 3, 7, 12, 4, 5, 9]
print(urutkan_daftar(daftar))
print("============================")
def luas_persegi_panjang(panajang, lebar):
     return panajang * lebar                #fungsi menghitung luas persegi panjang
print(luas_persegi_panjang(12, 30))
