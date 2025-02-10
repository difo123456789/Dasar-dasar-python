nama = input ("nama:")
nilai_semester_1 = float(input("nilai ip semester ke 1:"))
nilai_semester_2 = float(input("nalai ip semseter ke 2:"))
nilai_semester_3 = float(input("nalai ip semseter ke 3:"))
nilai_semester_4 = float(input("nalai ip semseter ke 4:"))
nilai_semester_5 = float(input("nalai ip semseter ke 5:"))

total_semester = nilai_semester_1 + nilai_semester_2 + nilai_semester_3 + nilai_semester_4 + nilai_semester_5
ipk = total_semester / 5
print (f"ipk{nama}:{ipk:.2f}")                