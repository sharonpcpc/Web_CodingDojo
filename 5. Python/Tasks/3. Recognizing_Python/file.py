num1 = 42      #variable declaration, Numbers entero#
num2 = 2.3     #variable declaration, Numbers decimal o flotante#
boolean = True      #variable declaration, Boolean#
string = 'Hello World'  #variable declaration, Strings#
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, list initialize#
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration, diccionario initialize#
fruit = ('blueberry', 'strawberry', 'banana')   #variable declaration, Tuples initialize#


print(type(fruit))      #revisar el tipo de dato: tupla#
print(pizza_toppings[1])        #list access value: Sausage#
pizza_toppings.append('Mushrooms')      #list add value: Mushrooms#
print(person['name'])       #dictionary: access value#
person['name'] = 'George'       #dictionary: change value#
person['eye_color'] = 'blue'        #dictionary: add value#
print(fruit[2])         #tuples: access value#



if num1 > 45:       #conditional if, evaluatuion conditional else#
    print("It's greater")
else:
    print("It's lower")



if len(string) < 5:         #conditional if, evaluatuion of length check, conditional else if, conditional else#
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")




for x in range(5):          #for loop starts at 0 and ends at 5#
    print(x)

for x in range(2,5):        #for loop starts at 2 and ends at 5#
    print(x)

for x in range(2,10,3):     #for loop starts at 2 and ends at 10 increasing at 3#
    print(x)

x = 0       #variable, Numbers#
while(x < 5):       #while loop#
    print(x)
    x += 1

pizza_toppings.pop()        #list delete value at the end#
pizza_toppings.pop(1)       #list delete value#

print(person)       #print to console dictionary#
person.pop('eye_color')         #list delete value#
print(person)       #print to console without the value mentioned before#


for topping in pizza_toppings:          #for loop, conditional if, print and stops loop#
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


def print_hello_ten_times():            #function declaration, for a number that starts at 0 and goes up to 10#
    for num in range(10):
        print('Hello')

print_hello_ten_times()         #function call#

def print_hello_x_times(x):         #function declaration, with default parameter#
    for num in range(x):
        print('Hello')

print_hello_x_times(4)          #function call argument 4#

def print_hello_x_or_ten_times(x = 10):         #function declaration, with default parameter#
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()        #function call goes to 10#
print_hello_x_or_ten_times(4)       #function call goes to 4#


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)