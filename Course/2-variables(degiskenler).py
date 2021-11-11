# -----------------------------------------
# strings metin türü
firstName = "Selim"
lastName = "Sevgi"

fullName = firstName + lastName
# /Hello SelimSevgi
fullName = firstName + " " + lastName
# /Hello Selim Sevgi

# print içine yazığımız ifadeyle değişkeni + işaretiyle kullanıyoruz.
# bu şekilde dizeleri birleştiriyoruz.
# print içinde yazılan ifadeler string tipindedir.
print("Hello "+firstName)
# /Hello Selim

# değişken veri tipini öğrenmek için
print(type(firstName))
# /<class 'str'>

# fullName değişkenini (SelimSevgi) olarak oluşturduk.
print("Hello "+fullName)

# -----------------------------------------
# integer tamsayı
yas = 21

# yas olarak tanımladığımız değişkeni bir artırmak için
#yas = yas + 1
# kısayolu
yas += 1
print(yas)

# veri tipi
print(type(yas))
# yas = "21" veri tipi sting oluyor.
# string bir ifadeyle matematiksel işlem yapılamıyor.

# int veri tipini str veri tipine dönüştürdük.
print("Yaşınız: " + str(yas))

# -----------------------------------------
# float ondalıklı sayı
yukseklik = 250.5
print(yukseklik)

# veri tipi
print(type(yukseklik))

# float veritipinide str e dönüştürerek kullanabiliriz.
print("Masanın yüksekliği: " + str(yukseklik)+ "cm.")

# -----------------------------------------
# boolean (true/false)
# bool genellikle karar yapılarında kontrol edilmesiyle daha çok kullanılır.
insan = True
print(insan)

# veri tipi
# insan = "False" şeklinde str veritipine dönüşmüş oluyor.
print(type(insan))

# bool veri tipinide str veritipine dönüştürerek kullanabiliriz.
print("O insan mı?: " + str(insan))