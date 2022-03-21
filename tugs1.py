#tipe data # anka satuan (integer)
data_integer = 11
print("data: " ,data_integer)
print("_brtipe : ",type(data_integer))
#tipe data dengan koma (float)
data_float = 2.5
print("data: " ,data_float)
print("_brtipe : ",type(data_float))
#tipe data # kumpulan karakter(string)
data_string = "ical"
print("data: " ,data_string)
print("_brtipe : ",type(data_string))
#tipe data # biner True/False(Boolean)
data_bool= True
print("data:",data_bool)
print("_bertipe:",type(data_bool))
#operasi aritmatika
a = 10
b= 3
# penjumlahan 
hasil = a + b
print(a, '+' ,b, '=',hasil)
#operasi penugasan 
a = 30
b = 2
a += b # a =a + b
print(a)
x = 4 
#operasi perbandingan 
a = 10
b = 2
#sama dengan 
hasil = a == b
print(a,'==' ,b, "=" ,hasil)
#operasi logika
# operator and
x = 4 
print(x<6 and x>2)
#operator or 
a = True
b = False
print (a or b)
#operator true
c = True
d = not c 
print("not",c,"=",d)
#percabangan if 
nilai = 85
if (nilai >= 80) :
    print("Nilai A")
#percabangan if else 
nilai = 56 
if (nilai >= 60):
    print("lulus")
else:
    print("tidak lulus")
#percabangan elif 
umur = 20
if (umur > 18 and umur < 30) :
    print("Sudah Beranjak Dewasa") 
elif(umur >= 30 and umur < 45) :
    print("Masa masa Emas")
elif(umur >= 45 and umur < 55) :
    print("Masa Paruh Baya")
elif(umur >= 55) :
    print("Masa menua")
else:
    print("masih DiBawah Umur)")
 

