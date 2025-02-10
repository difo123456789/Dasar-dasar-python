# membuat array
import array as arr

a = arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i],end =" ")
   

b = arr.array('d',[2.5,3.2,3.3])
for i in range(0,3):
    print(b[i],end=" ")
    print()

# menambahkan elemen ke array
import array as arr

a = arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i],end=" ")
  
a.insert(1,4)
for i in (a):
    print(i,end=" ")
    

b = arr.array ('d',[2.5,3.2,3.3])
for i in range(0,3):
    print(b [i],end=" ")
   
b.append(4.4)
for i in (b):
    print(i, end=" ")
    print( )
    

# mengakses elemen dari array
import array as arr

a = arr.array('i',[1,2,3,4,5,6])
print("access element is:", a[0])
print("access element is:", a[3])

b = arr.array('d',[2.5,3.2,3.3])
print("access element is:", b[1])
print("access element is:", b[2])

#menghapus elemen dari array
import array
arr = array.array('i',[1,2,3,4,5])
for i in range (0,5):
    print(arr[i], end=" ")
print(arr.pop(2))
for i in range (0,4):
    print(arr[i], end=" ")
arr.remove (1)
for i in range(0,2):
    print(arr[i], end=" ")
    

# mengiris array
import array as arr 

l =[1,2,3,4,5,6,7,8,9,10]
a = arr.array('i',l)
 
for i in (a):
    print(i, end=" ")

sliced_arry = a [3:8]
print(sliced_arry)

sliced_arry = a [5:]
print(sliced_arry)

sliced_arry = a [:]
print(sliced_arry)

#elemen pencarian dalam array
import array
arr = array.array('i',[1,2,3,1,2,5])
for i in range (0,6):
    print(arr[i],end =" ")
print (arr.index(2))
print (arr.index(2))

# memperbarui elemen dalam array
import array
arr = array.array('i',[1,2,3,1,2,5])
for i in range (0, 3):
    print(arr[i], end=" ")

arr[2]=6
for i in range (0, 6):
    print(arr [i], end=" ")
    print()

arr[4]=8
for i in range (0, 6):
    print(arr [i], end=" ")