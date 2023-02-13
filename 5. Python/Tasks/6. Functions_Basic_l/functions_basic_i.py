# #1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# #Predicción: Debería devolver el número 5#



# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# #Predicción: Debería devolver un error porque el parametro de "number_of_days_in_a_week_silicon_or_triangle_sides" no se encuentra definido.#



#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# #Predicción: Debería devolver el número 10.# #Me equvoqué, salió 5#



#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Predicción: Debería devolver primero el número 10 y luego el número 5. Me equivoqué. La respuesta es 5#



# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Predicción: Se va a imprimir el 5 pero la x no se va a imprimirr porque como tal, no se ha dado un valor return#



# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Predicción: El resultado del segundo print sera 3+5=8. Me equivoqué devuleve error, porquue no hay un return.



# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Predicción: Va a mostar un 2 al lado de un 5. Siendo 25. Sin embargo no es una operación matematica porque ambos son str.#



# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Predicción: Va a mostar un 10. Parcialmentee correcta. Primero imprime un 100.



# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Predicción: Va a mostar un 7, luego un 14 y por ultimo la suma, que es 21.



# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Predicción: EL resultado es un 8




# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Predicción: Va a mostrar primero 500, luego 300, luego 300, luego 500. Me equivoqué... y aún no entiendo por qué da el resultado 500, 500, 300, 500.   




# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Predicción: 500, 500, 300, 500




# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Predicción: 500, 500, 300, 300



# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Predicción: 1 y 3. 




# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Predicción: 1 y 3, luego 5 y 10.
