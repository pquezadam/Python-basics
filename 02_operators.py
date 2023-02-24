#Operadores

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(10 // 5)
print(5 ** 2)

print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola" + "Python")
print(" Hola " + str(5))
print(" Hola " * 5)
print(" Hola " *(2 ** 3))

my_float = 2.5 * 2
print("hola " * int(my_float))


print("Hola" < "Python")
print("aaaa" >= "abaa") #Ordenación alfabética por ASCII
print(len("aaaa") >= len("aaaa")) #Cuenta los caracteres dentro de las comillas
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores lógicos
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 > 4 or "Hola" > "Python" and 4 == 4)
print(not(3 > 4))