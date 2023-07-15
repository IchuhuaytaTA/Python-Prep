#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
x = 2
print(x)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(x))



# 4) Crear una variable que contenga tu nombre

# In[2]:
var = 'Jheyson'
print(var)



# 5) Crear una variable que contenga un número complejo

# In[3]:
var = 3 + 3j
print(var)




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(var))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416
print(pi)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo? no

# In[3]:

var1 = 'True'
var2 = True

print(var1, var2)



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(var1), type((var2)))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

var = 5 + 5.7
print(var)


# 11) Realizar una operación de suma de números complejos

# In[2]:
x = 3 + 6j
t = 3 + 7j
suma = x + t
print(suma)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

var = 3.4 + 3j
var2 = 3.4 + 5j
suma = var + var2
print(suma)



# 13) Realizar una operación de multiplicación

# In[5]:

x = 3 * 4
print(x)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

x = 2**8
print(x)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

x = 27 / 4
print(x)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:


x = 27 // 4
print(x)


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


x = 27 % 4
print(x)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

x = 4 * 6 + 3
print(x)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
var1 = "holas "
var2 = 'como estas'
suma = var1 + var2
print(suma)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

x = 2 == '2'
print(x)


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

x = 2 == 2
print(x)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#por que el numero esta con comas y los decimales o float se escriben con punto



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:


x = 3
x -= 1
print(x)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

x = 1 << 3

print(x)
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


# uno es un int y el otro el una cadena



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

x = 'hola como estas'
y = 3
print(x*y, 'se repite', y, 'veces')

