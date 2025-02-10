angka = [27,21,43,18,46,4,25,24,22,32,30,40,7,12,42]
angka = angka[2:]
angka = angka[:-4]
npm_digits = 9
angka.insert(5,npm_digits)
total = sum(angka)
print("list setelah modifikasi :", angka)
print("total nilai list:", total)