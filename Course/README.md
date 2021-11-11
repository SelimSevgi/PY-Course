>## 1-pythonTutorial-forBeginners
```python
# yazı tipini ve boyutunu değiştirmek için
# settings - editor - font

# konsol ekranında göstermek için kullanılır.
print("Electric and electronic enginner")
print("it is good")

# terminal yazı rengini değiştirmek için
# settings - editor - color scheme - console colors

# terminal yazı boyutunu değiştirmek için
# settings - editor - color scheme - console font
```
>## 2-variables(degiskenler)
```python
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
```
>## 3-multipleAssignment(cokluAtama)
```python
# birden fazla değişken tanımladık
#isim = "Selim"
#yas = 25
#mühendis = True

# tek satır halinde değişkenler arasına , konularak tanımlayabiliriz.
isim, yas, mühendis = "Selim", 25, True
# /Selim
# /25
# /True

# değikenlerimizi ekranda gösterelim
print(isim)
print(yas)
print(mühendis)

# birden fazla aynı değişken yanı değeri tutuyorsa
#ali = 30
#mustafa = 30
#serif = 30
#anil = 30
#selim = 30

# tek satır halinde;
ali = mustafa = serif = anil = selim = 30
# /30
# /30
# /30
# /30
# /30

print(ali)
print(mustafa)
print(serif)
print(anil)
print(selim)
```
>## 4-stringsMethods(dizeYöntemi)
```python
bolum = "yazılım"

# string ile tanımlanan değişkenin uzunluğu
print(len(bolum))
# /7

# karakterin kaçıncı indekste olduğunu gösterir
# indeksler 0 ile başlar. ilk yazılım y harfi 0. indekste bulunur.
print(bolum.find("y"))
# /0

# Arada boşluk olduğunu düşünelim. Sadece ilk kelimenin başta bulunan harfi büyük yapar.
print(bolum.capitalize())
# /Yazılım

# Değişken içinde bulunan bütün harfleri büyük yazar.
print(bolum.upper())
# /YAZILIM

# Değişken içinde bulunan bütün harfleri küçük yazar.
bolum1 = "ELEKTRİK VE ELEKTRONİK"
print(bolum1.lower())
# /elektri̇k ve elektroni̇k

# Değişken içerisinde sayı var mı? kontrolünü yapar.
print(bolum.isdigit())
# /False
sayi = "123"
print(sayi.isdigit())
# /True

# Değişken içerisinde harfler var mı? kontrolünü yapar.
print(bolum.isalpha())
# /True
# Sadece hepsi harflerden mi oluşmuş onun kontrolünü yapar. Arasında boşluk bulunduğu için
b_bolum = "y azılım"
print(b_bolum.isalpha())
# /False

# Değişken içerisinde kaç tane ("?") var? kontrolünü yapar.
print(bolum.count("ı"))
# /2

# Değişken içerinde bulunan tüm ("?" harflerini, "istediğimiz_harfe") dönüştürebiliriz
print(bolum.replace("ı","x"))
# /yazxlxm

# Değişkeni istediğimiz kadar yazdırmak
print(bolum*3)
# /yazılımyazılımyazılım
```
>## 5-typeCast(ayniRollerivermek)
```python
x = 1   # int
y = 2.0 # float
z = "3" # str

print(x)
# /1
print(y)
# /2.0
print(z)
# /3

# Aynı dönüşüm yapmak için;
# -----------------------------------------
# int
y = int(y)
print(y)
# /2

print(z*3)
# /333
z = int(z)
print(z*3)
# /9

# -----------------------------------------
# float
x = float(x)
# Önceden float'i int değerine dönüştürdüğümüz için tekrar float veritipine dönüştürmemiz lazım
y = float(y)
z = float(z)

print(x)
# /1.0
print(y)
# /2.0
print(z*3)
# /9.0

# -----------------------------------------
# string
x = str(x)
y = str(y)
z = str(z)

# En son float veritipine dönüştürdüğümüz için;
print(x)
# /1.0
print(y)
# /2.0
print(z*3)
# /3.03.03.0
```
>## 6-userInput(kullaniciGirisi)
```python
# Konsoldan kullanıcıdan veri alınmak istenirse;
# Başka bir yerde kullanmak istenirse tanımla yapmamız gerekiyor
isim = input("İsim nedir?: ")
# ^Selim

print("Merhaba " + isim)
# /Merhaba Selim

yas = int(input("Kaç yaşındasın?: "))
# ^25
# yas değeri şuan str tipindedir.
# Matematiksel işlemler kullanmak için int kullanılmalıdır
yas += 1
print(yas)
# /26

# str veri tipinde kullanırken tekrar int verisini str tipine çevirmeliyiz.
print(str(yas) + " yaşındasın.")
# /26 yaşındasın.

boy = float(input("Boyunuz?: "))
# ^1.70
print(boy)
# /1.7
print("Boyunuz " + str(boy) + " cm.")
# /Boyunuz 1.7 cm.
```
>## 7-mathFunctions(matematikselFonk)
```python

```