
a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
c = float(input("Masukkan nilai c : "))

if a <= 0 or b <= 0 or c <= 0:
    print ("Tidak ada segitiga yang dapat dibangun")
    
elif a >= b + c or b >= a + c or c >= a + b:
    print ("Tidak ada segitiga yang dapat dibangun")
    
elif (round(a)==round(b) and round(b)==round(c)):
    print ("Segitiga sama sisi")
    
elif a == b or b == c or a == c:
    print ("Segitiga sama kaki")
    
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print ("Segitiga siku-siku")

else :
    print ("Segitiga bebas")
