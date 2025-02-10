nilai_tugas= float(input("masukan nilai tugas:"))
nilai_quiz= float(input("masukan nilai quiz:"))
nilai_uts=float(input("masukan nilai uts:"))
nilai_uas=float(input("masukan nilai uas:"))

nilai_akhir=0.15* nilai_tugas + 0.20* nilai_quiz + 0.20* nilai_uts + 0.30* nilai_uas
print("nilai_akhir.",nilai_akhir)

if nilai_akhir >= 65:
      print("selamat,anda lulus")
else:
    print("maaf,anda gagal")