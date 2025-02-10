nilai=int (input("nilai:"))

if(nilai < 50 ):
   skor_akhir= "E"
elif( 50<= nilai < 55):
   skor_akhir=  "D"
elif( 55<= nilai < 60):
   skor_akhir=  "C"
elif( 60<= nilai < 65):
   skor_akhir=  "C+"
elif( 65<= nilai < 70):
   skor_akhir=  "B-"
elif( 70<= nilai < 75):
   skor_akhir=  "B"
elif( 75<= nilai < 80):
   skor_akhir=  "B+"
elif( 80<= nilai < 85):
   skor_akhir=  "A-"
elif( 85<= nilai <100):
   skor_akhir=  "A+"
   
   


print("skor akhir:",skor_akhir)