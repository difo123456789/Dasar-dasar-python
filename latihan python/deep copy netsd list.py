data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

#mengambil data dari nested list

data = data_2d[1][0]
print(f"data = {data}")

# address semuanya

print(f"address asli ={hex(id(data_2d))}" )
print(f"address copy ={hex(id(data_2d_copy))}" )

print("addreas dari member ke-1")
print(f"address asli ={hex(id(data_2d[0]))}" )
print(f"address copy ={hex(id(data_2d_copy[0]))}" )

data = data_2d[1][0]=5
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

nomor = 3
nim = 4
print(nomor*nim)