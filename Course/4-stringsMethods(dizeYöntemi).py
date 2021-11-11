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