# Mengubah suatu tipe data menjadi tipe daya yang lain

# 1. Mengubah string menjadi number
# int() - > Mengubah tipe data menjadi int
x = '10'
print(type(x)) # mengecek tipe data dari sebuah variable
y = '5'
x = int(x)
y = int(y)
z = x + y
print(type(z))

# 2. Mengubah int menjadi float
z = float(z)
print(z)

# 3.Mengubah tipe data menadi string
z = str(z)
print(type(z))

a = input("a: ") #by default menghasilkan tipe data string
b = input("b: ")
print(a+b)