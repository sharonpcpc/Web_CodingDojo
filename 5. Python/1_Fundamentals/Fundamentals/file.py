#1. Cuenta regresiva:#

def countdown(n):
    return list(range(n, -1, -1))
print(countdown(10))


#2. Imprimir y devolver:#

#option1#
def imprimir_y_devolver(list):
    print(list[0])
    return(list[1])
print(imprimir_y_devolver([1,2]))

#option2#
list = [1, 2]
def imprimir_y_devolver(list):
    print(list[0])
    return(list[1])
print(imprimir_y_devolver(list))


#3. Primero más longitud#

def suma_mas_longitud(list):
    return list[0] + len(list)
print(suma_mas_longitud([1,2,3,4,5]))


#4. alores mayores que el segundo#

def valores_mayores_que_el_segundo(list):
    if len(list) < 2:
        return False
    nueva_list = []
    for x in range(0, len(list)):
        if list[x] > list [1]:
            nueva_list.append(list[x])
    print(len(nueva_list))
    return nueva_list
print (valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

#Esta longitud, ese valor:#

def longitud_y_valor(longitud, valor):
    output = []
    for x in range(0,longitud):
        output.append(valor)
    return output
print(longitud_y_valor(4,7))
print(longitud_y_valor(6,2))