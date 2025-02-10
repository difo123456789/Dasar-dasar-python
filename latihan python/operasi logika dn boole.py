# operasi logika dan boolean
#not ,or, and, xor
#not
print('===not===')
a = False
c = not a
print('data  a =',a)
print('--------- not')
print('data c=',c)

# (jika salah satu true ,maka hasilnya adalah true)
# or
print('===or===')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c =  a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

#and
print('===and===')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c =  a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)


# xor
print('===xor===')
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = False
c =  a ^ b
print(a,'xor',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)

