#list
# menggunakan kurung siku
data_list = [10,2,4,3,2]
print(data_list)
# tuple
data_tuples = (7,8,9,10)
print(data_tuples)
print(data_tuples[1])

# menhapus tuple
tuple = (0,1,2,3,4)
del tuple

print(tuple)

#membuat tuple
tuple1 = ()
print(tuple)

tuple1 = ("kita","kamu")
print(tuple1)

tuple1 = tuple("kalian")
print(tuple1)

#  membuat tuple denagn menggunakan tipe data yang berbeda

tuple1 = (5,"selamat",7,"datang")
print(tuple1)

tuple1 = (0,1,2,3)
tuple2 = ('python','greek')
tuple3 = (tuple1,tuple2)
print(tuple3)

tuple1 = ("geeks",)*3
print(tuple1)

#mengakses tuple
#WITH INDEXING
tuple1 = tuple ("selamat")
print(tuple1[1])

# Tuple unpacking 
tuple1 = ("selamat","buat","kamu")
a,b,c = tuple1
print(a)
print(b)
print(c)

# rangkaian tuple
tuple1 = (0,1,2,3)
tuple2 =("selamat","buat","kamu")
tuple3 = tuple1 + tuple2

print(tuple1)
print(tuple2)
print(tuple3)

# mengisi tuple
tuple1 = tuple ("selamat datang")
print(tuple1[3:])

print(tuple1[::-1])

print(tuple1[4:9])