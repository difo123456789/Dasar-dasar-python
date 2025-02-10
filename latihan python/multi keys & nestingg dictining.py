import datetime

mahasiswa ={
    'nama':'difo',
    'nim':'2301283',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2002,4,10)
}

mahasiswa2 ={
    'nama':'amel',
    'nim':'2301234',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2000,2,15)
}

mahasiswa3 ={
    'nama':'toto',
    'nim':'23015466',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,5,23)
}

data_mahasiswa = {
    'MAH001':mahasiswa,
    'MAH002':mahasiswa3,
    'MAH003':mahasiswa
}


print(f"{'KEY':<6} {'nama':<17}  {'SKS':<3}  {'beasiswa':<9}  {'LAHIR':<10}" )
print("_"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM  = data_mahasiswa[KEY]['nim']
    SKS  = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<6} {NAMA:<17}  {SKS:<3}  {BEASISWA:<9}  {LAHIR:<10}")