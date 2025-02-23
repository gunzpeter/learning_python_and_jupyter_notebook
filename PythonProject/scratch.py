
a = (int(input("add meg az első oldalt hosszát: ")))
b = (int(input("add meg a második oldalt hosszát: ")))
c = (int(input("add meg a harmadik oldalt hosszát: ")))

if a + b >= c or a + c >= b or c + b >= a:
    print ("ügyes vagy, létezik ilyen háromszög!")
else:
    print ("menj vissza elsőbe!")

print (""
       "")
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print (" ez egy derékszögü háromszög!")
else:
    print (" nem egy derékszögü háromszög!")

print(""
-
    "")