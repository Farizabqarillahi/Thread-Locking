a = float(input("masukan input A : "))
b = float(input("masukan input B : "))
c = float(input("masukan input C : "))


while a <= 0 or b <= 0 or c <= 0:
  print("segitiga tidak dapat dibangun")
  print()
  a = float(input("masukan input A : "))
  b = float(input("masukan input B : "))
  c = float(input("masukan input C : "))

if(a > c+b or b > a+c or c > b+a):
  print("Segitiga tidak bisa dibangun")

print()

if(a==b and a!=c or a==c and a!=b or b==c and b!=a):
  print("segitiga sama kaki")

print()

if(round(a)==round(b) and round(b)==round(c)):
  print("segitiga sama sisi")


if(a > b and a > c ):
  hasilreal = a
  hasilsec = b
  HasilThird = c

elif(b > a and b > c ):
  hasilreal = b
  hasilsec = a
  HasilThird = c
elif(c > b and c > a ):
  hasilreal = c
  hasilsec = a
  HasilThird = b

if(hasilreal*2 == hasilsec2 + HasilThird*2 ):
  print("segitiga siku-siku")

if(hasilreal < hasilsec+HasilThird and round(a)!=round(b) and round(a)!=round(c) and round(b)!=round(a) and round(b)!=round(c) and round(c)!=round(a) and round(c)):
  print("segitiga bebas")