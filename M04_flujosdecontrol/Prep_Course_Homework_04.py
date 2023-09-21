#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

num = -1

if (num>0):
    print(str(num) + " es mayor a 0")
else:
    print(str(num) + " es menor a 0")
    



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 41
b = "25"

if(type(a)==type(int(b))):
    print("Son del mismo tipo de dato: " + str(type(a)) )
else:
    print("No son del mismo tipo de dato")
    




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

a=20

while (a>=1):
    if(a%2==0):
        print("El numero " +str(a)+ " es par")
    else:
        print("El numero " +str(a)+ " es impar")

    a -=1
        



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range (0,6):
    print("El valor de la potencia de " + str(i) + " al cubo es " +  str(i**3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

num = 5

for i in range(0,num):
    print("Ciclo " + str(i))



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

a = 12
if (type(a) == int):
    if (a > 0):
        factorial = a
        while (a > 2):
            a = a - 1
            factorial = factorial * a
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

a = 0
while(a<20):
    a += 1
    for i in range (0,a):
        print('Ciclo while nro ' + str(a))
        print('Ciclo for nro ' + str(i))

        



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

a = 20

for i in range (0,a):
    while(a>0):
        a-=1
        print('Ciclo while nro ' + str(a))
        print('Ciclo for nro ' + str(i))



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1




# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:


n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:





# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:



