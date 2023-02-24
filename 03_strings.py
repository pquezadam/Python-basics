### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(my_string + " " + my_other_string)

print(len(my_string))
print(len(my_other_string))

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

## Formateo 

name, surname, age = "Pablo", "Quezada", 32

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
