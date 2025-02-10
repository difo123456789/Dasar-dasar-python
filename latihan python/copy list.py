## teknik menduplikat list

a = ["ucup","otong","dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari a
a[1] = "micheal"
b.sort()
print(f"a ={a}")
print(f"b = {b}")


# address dari kedua list a dan  b
print(f"addres a  = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")


# menduplikat  list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy()

print(f"addres a  = {hex(id(a))}")
print(f"addres b =  {hex(id(b))}")
print(f"addres c  = {hex(id(c))}")

print(f"a ={a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
a[1] ="Dadang"

print(f"a ={a}")
print(f"b = {b}")
print(f"c = {c}")

