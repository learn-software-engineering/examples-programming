####
# If
####
print("### Ejemplo de uso de la estructura `if`")

edad = 15
if edad >= 18:
    print("   Eres mayor de edad")

#########
# If-Else
#########
print("### Ejemplo de uso de la estructura `if-else`")

edad = 21
if edad >= 18:
    print("   Eres mayor de edad")
else:
    print("   Eres menor de edad")

##############
# If-Elif-Else
##############
print("### Ejemplo de uso de la estructura `if-elif-else`")

edad = 5
if edad <= 13:
    print("   Eres un niño")
elif edad > 13 and edad < 18:
    print("   Eres un adolescente")
else:
    print("   Eres un adulto")

#######
# While
#######
print("### Ejemplo de uso de la estructura `while`")

i = 1
while i <= 5:
    print(i)
    i = i + 1

#####
# For
#####
print("### Ejemplo de uso de la estructura `for`")

nombres = ["María", "Florencia", "Julián"]
for nombre in nombres:
    print(f"   Hola {nombre}")

#################
# Sentencia break
#################
print("### Ejemplo de uso de la sentencia `break`")

i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

####################
# Sentencia continue
####################
print("### Ejemplo de uso de la sentencia `continue`")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

################################################
# Anidamiento de estructuras de control de flujo
################################################
print("### Ejemplo de uso de estructuras anidadas")

for i in range(5):
    for j in range(10):
        if (i % 2 == 0 and j % 3 == 0):
            print(f"i = {i}, j = {j}")

# Imprime:
# i = 0, j = 0
# i = 0, j = 3
# i = 0, j = 6
# i = 0, j = 9
# i = 2, j = 0
# i = 2, j = 3
# i = 2, j = 6
# i = 2, j = 9
# i = 4, j = 0
# i = 4, j = 3
# i = 4, j = 6
# i = 4, j = 9

###################################
# Patrones de uso comunes: búsqueda
###################################
print("### Ejemplo de uso del patrón de búsqueda")

frutas = ["manzana", "naranja"]

buscando = "naranja"
encontrado = False

for fruta in frutas:
    if fruta == buscando:
        encontrado = True
        break

if encontrado:
    print("   Fruta encontrada!")

######################################
# Patrones de uso comunes: acumulación
######################################
print("### Ejemplo de uso del patrón de acumulación")

total = 0

for i in range(10):
    total += i

print(total) # Suma de 0..9 = 45
