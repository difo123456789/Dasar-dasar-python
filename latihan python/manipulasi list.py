## operasi

# index 0(-3) 1 (1-2)  2(-1)
data = ["ucup","otong","dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data [-3]
print(f"data ucup = {data_ucup}")

#mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data={panjang_data}")

## manipulasi data list

#menambahkan item pada list sesuai
print(f"data sebelum ditambah =\n{data}")


data.insert(1,"asep")
print(f"data sesudah ditambah = \n{data}")

# menamdah di akhir list
data.append("jajang")
print(f"data ditambah lagi =\n{data}")

# menambahkan list dengan list
data_baru = ["ujang","usep","dadang"]
data.extend(data_baru)
print(f"data gabungan =\n={data}")

#merubah data 
#kita ubah data 2 menjadi michael
data[2] = "michael"
print(f"data remove =\n {data}")

# meremove.data
data.remove("ujang")
print(f"data mrubah =\n{data}")

#data.remove("usep") akan eror karena huruf harus sesuai yaitu"use"

# meremove data paling belakang
data.pop()
print(f"data akhir =\n{data}")

