umur = input("kamu umur berapa? ")
#mengubah input menjadi integer
umurJadiInteger = int(umur)
#kalkulasi
#sisa berapa tahun? (misalkan estimasi dia hidup 75 tahun)
tahun = 75 - umurJadiInteger
#sisa berapa bulan?
bulan = tahun * 12
#sisa berapa minggu?
minggu = tahun * 52
#sisa berapa hari?
hari = tahun * 365

eksekusi = print(f"kamu memiliki {hari} hari atau {minggu} minggu atau {bulan} bulan atau {tahun} tahun tersisa")

print (eksekusi)
