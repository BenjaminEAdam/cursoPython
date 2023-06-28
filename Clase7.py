# As an exercise we make an application that asks the user 
# to enter integers which will be inserted into a list.
# If you enter zero the application ends.

lista = []
lista2= []
numero = int(input("Ingrese un numero entero, cero para finalizar: "))
while(numero !=0):
    lista.append(numero)
    lista2.append(numero)
    numero = int(input("Ingrese un numero entero, cero para finalizar: "))

print(lista)

# Find the smallest and largest number in the list

if(len(lista)>0):
    maximo= lista[0]
    minimo= lista[0]
    for i in lista:
        if (i>maximo):
            maximo=i
        if (i<minimo):
            minimo=i

    print(minimo)
    print(maximo)

# Sort the list from smallest to largest
# This is that i did

for i in range (len(lista)):
    for j in range (len(lista)):
        if (lista[i]<lista[j]):
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux

print(lista)

# This is that professor did
# Advantage: higher performance, because if start with the list neatly, no enter to the loop for 

ordenada = False
print(lista2)

while (ordenada==False):
    ordenada = True
    for i in range(len(lista2)-1):
        aux1 = lista2[i]
        aux2 = lista2[i+1]
        if(aux1>aux2):
            lista2[i]=aux2
            lista2[i+1]=aux1
            ordenada = False

print(lista2)