#1. Basico#
for count in range(0,151):
    print(count)


#2. Multiplos de 5#
for count in range(0,1000,5):
    print(count)


#3. Contar, a la manera del Dojo:#
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#4.Whoa. Es un gran idiota: #
suma = 0
for x in range(1, 500001, 2):
    suma += x
print(suma)

#5.Cuenta regresiva de a 4#
for x in range(2018, 0, -4):
    print(x)

#6Contador flexible#
lowNum=2
highNum=9
mult=3

for x in range(lowNum, highNum+1,):
    if x % mult == 0:
        print(x)