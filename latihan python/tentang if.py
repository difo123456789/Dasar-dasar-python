#input
nama = input("nama karyawan :")
nik = input("nik karyawan :")
status = input("status (staff/ honot:")
gol = input("golongan (a/b/c) :")
#proses
if(status == "staff"):
   gaji = 100000
   if(gol == "a"):
     bonus = 200000
   elif(gol == "b"):
     bonus = 300000
   elif(gol == "c"):
     bonus = 5000
elif(status == "honor"):
    gaji = 750000
    if(gol == "a"):
       bonus = 15000000
    elif(gol == "b"):
        bonus = 30000
    elif(gol == "c"):
       bonus = 40000
gatot = gaji + bonus
#ouput
print("gaji =", gaji)
print("bonus =", bonus)
print("gaji total=", gatot)
       