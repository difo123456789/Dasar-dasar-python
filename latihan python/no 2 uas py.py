tahun = int(input("tahun:"))
if tahun % 4 == 0 and (tahun % 100 !=0 or tahun % 400 ==0):
    print("tahun kabisat")
else:
    print("bukan tahun kabisat")

