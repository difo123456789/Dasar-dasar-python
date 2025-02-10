## ==== LIST ====

# kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

#kumpulan data boolen 
data_boolean = [True,False,True,True]
print(data_boolean)

#kumpulan campuran
data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10)
print(data_range)
data_list = list (data_range)
print(data_list)

# membuat list dengan for loop, list comprehensi
list_pake_for = [ i**2 for i in range (0,10)]
print(list_pake_for)

#membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i !=5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)