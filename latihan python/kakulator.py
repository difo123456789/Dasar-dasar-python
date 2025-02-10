def penjumlahan (a,b):
    return a + b

def pengurangan (a,b):
    return a - b

def perkalian (a,b):
    return a * b

def pembagian (a,b):
    return a / b

bilangan1=float(input("masukan bilangan pertama:"))
bilangan2=float(input("masukan bilangan kedua:"))

print("pilihan operator")
print("1.penjumlahan")
print("2.pengurangan")
print("3.perkalian")
print("4.pembagian")

pilihan_operator = int(input("masukan pilihan operator_:"))

if pilihan_operator == 1:
    hasil = penjumlahan(bilangan1,bilangan2)
elif pilihan_operator == 2:
    hasil = pengurangan(bilangan1,bilangan2)
elif pilihan_operator == 3:
    hasil = perkalian(bilangan1,bilangan2)
elif pembagian == 4:
    hasil = pembagian(bilangan1,bilangan2)
else:
    print("pilihan operator tidak valid")

print("hasil=",hasil)

