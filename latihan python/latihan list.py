# progrm list buku


list_buku =[]
while True:
    print("\nmasukan data buku")
    judul = input("judul buku\t: ")
    penulis = input("masukan nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"data buku","="*10)
    for index,buku in enumerate (list_buku):
        print(f"{index+1}|{buku[0]}| {buku[1]}")


    print("\n\n","="*20)
    islanjut = input("apakah dilanjutkan?(y/n))")

    if islanjut == "n":
        break

    print("program selesai")




