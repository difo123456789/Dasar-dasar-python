# latihan perulangan membuat segitiga

sisi = 10

# menggunakan for
# dummy variabel
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1


print(" akhir dari for")
# 2. menggunakan while 

print("awal while")
count = 1
while  True:
    print("*")
    count += 1

    if count > sisi:
        break

print("akhier while")  

#3 . hanya ganjil saja
print("awal while")
count = 1

while  True:
    # print jika ganjil
    if (count%2):
        print("+"*count)
        count += 1
    else:
         # akan kembalui keatas jika ganjil
        count += 1
        continue
   

# akan break jika count  melebihi sisi
    if count > sisi:
        break

print("akhier while")  