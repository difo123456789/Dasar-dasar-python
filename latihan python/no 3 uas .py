kapasitas_tabung = int(input("masukkan kapasitas tabungan = "))
sisa_kapasitas  = kapasitas_tabung

while sisa_kapasitas >0:
    kapasitas_air = int(input("masukan kapsitas air ="))

    if kapasitas_air <= sisa_kapasitas:
        sisa_kapasitas -= kapasitas_air
        print("sisa kapasitas tabung = ",sisa_kapasitas)
    else:
        print("tabung tidak bisa  menampung lagi")
        break