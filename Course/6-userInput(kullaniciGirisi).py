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