#input
brt= input("Berat Beras: ")  #misal: 10 kilogram
hrg_brs= int(input("Harga Beras: ")) #misal: 10000 perkilogram
ongkos= int(input("Tarif angkot: ")) #misal: 3500 sekali naik angkot
uang= int(input("Jumlah Uang: ")) #misal: 150000 Total uang Rina

#proses
total_hrg= float(brt) * hrg_brs #total harga beras
pp= ongkos * 2  #total biaya tranportasi
sisa= uang - total_hrg - pp #sisa uang rina

#output
print("Total harga beras: ",total_hrg," (",brt," x ",hrg_brs,")")
print("Biaya transportasi (PP): ",pp," (2 x "+ str(ongkos) +")")
print("Sisa uang Rina: ",sisa," ("+ str(uang) +" - ",total_hrg," - "+ str(pp) +")")
