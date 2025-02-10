# operator dictionary

data_dict = {
    "ucup":"ucucp surucup",
    "tong":"otong suotong",
    "dung":"dudng surudung"
}

# panjang  dictionaly
LENDICT = len(data_dict)
print(f"panjang dicrionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "ucup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses values (read) dengan get
print(data_dict["ucup"])
print(data_dict.get("ucup"))
print(data_dict.get("kis","key tidak ditemukan")) #


# mengupdate data
data_dict["ucup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasep"
print(data_dict)

data_dict.update({"ucup":"ucup surucup"})
print(data_dict)
data_dict.update({"difo":"difo si keren "}) # kalau gak ada di add aja
print(data_dict)

#mendelete data pada dictionary
del data_dict["difo"]
print(data_dict)



