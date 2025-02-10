import datetime
import os

# template edit mahasiswa
mahasiswa_template = {
        'nama':'nama',
        'nim':'000001',
        'sks_lulus':0,
        'lahir':datetime .datetime(1111,1,11)
 }

data_mahasiswa = {}

os.system("cls") # untuk windows
#os.system("clear")
print(f"{'selamat datang':^20}")
print(f"{'selamat datang':^20}")
print("_"*8)


mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa ['nama']= input ("nama mahasiswa:")
mahasiswa ['nim']= input ("nim mahasiswa:")
mahasiswa ['sks_lulus']= int  (input ("sks_lulus mahasiswa:"))
tahun_lahir = int(input("tahun lahir(YYYY):"))
bulan_lahir = int(input("bulan lahir(1-12):"))
tanggal_lahir = int(input("tanggal lahir(1-31):"))
mahasiswa['lahir'] =(tahun_lahir,bulan_lahir,tanggal_lahir)
print (mahasiswa)

