
from operator import length_hint


my_variable =  "String en python"
print(my_variable)

my_int_variable = 6
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# concatenación variables
print(my_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funciones del sistema
print(length_hint((my_variable)))

#variables en una sola línea, pero cuidado con esta sintaxis!!!
name, surname, alias, age = "Pablo", "Quezada", "pquezada", 32
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)


# inputs
name = input('Cuál es tu nombre: ')
age = input('Cuántos años tienes? ')

print(name)
print(age)


# cambiamos su tipo
name = 32
age = "Pablo"
print(name)
print(age)

# forzamos el tipo
address: str = "Mi dirección"
address = 32
print(address)