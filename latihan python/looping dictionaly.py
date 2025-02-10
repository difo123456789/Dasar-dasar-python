# looping dictionaly\

teman_teman  = {
    "ucup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucup surucuy"
}

# looping first try (yang keluar adalah kenya)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
    
values = teman_teman.values()
print(values)

for values in teman_teman.values():
   print(values)

items = teman_teman.items()
print(items)



