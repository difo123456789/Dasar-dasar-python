def hitung_jumlah_genap(N):
 jumlah_genap = 0
 for i in range(0,N+1,2):
     jumlah_genap += i
 return jumlah_genap

N = int(input("masukan angka:"))
hasil = hitung_jumlah_genap(N)
print(f"ouput {hasil}")
 