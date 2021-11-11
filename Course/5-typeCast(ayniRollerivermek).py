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
