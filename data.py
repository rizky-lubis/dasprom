def uang_keluar(beras, harga_beras, ongkos_transport, uang):
  total_harga_beras = beras * harga_beras
  sisa_uang = uang - total_harga_beras - ongkos_transport
  return sisa_uang

beras = 10
harga_beras = 10000
ongkos_transport = 3500
uang = 150000

sisa_uang = uang_keluar(beras, harga_beras, ongkos_transport, uang)

print("Sisa uang Rina adalah: Rp.{}".format(sisa_uang))
