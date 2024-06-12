#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
#Ejercicio 2



# # Data Science Tools and Ecosystem
# 

# **Objetivos**
# - Lenguajes de programacion para ciencia de datos
# - Herramientas para ciencia de datos
# - Ejemplo de expresiones aritmeticas

# En este cuaderno se resumen las herramientas y el ecosistema de ciencia de datos.

# In[ ]:





# In[2]:


# Ejercicio 4


# Algunos lenguajes de programacion usados para la ciencia de datos:

# In[3]:


Lenguajes = ["python","R", "JS"]
for i, Lenguaje in enumerate(Lenguajes):
    print(f"{i+1}: {Lenguaje}")


# In[4]:


# Ejercicio 5


# Algunas bibliotecas mas usadas en ciencia de datos son:

# In[5]:


Bibliotecas = ["pandas", "NumPy", "TensorFlow"]
for i, Biblioteca in enumerate(Bibliotecas):
    print(f"{i+1}: {Biblioteca}")


# In[6]:


# Ejercicio 6

Herramientas usadas en la ciencia de datos:
# In[7]:


import pandas as pd


# In[8]:


py = ["python"]
pn = ["pandas"]
np = ["NumPy"]


# In[9]:


lista_herramientas = [py, pn, np]


# In[15]:


df_herramientas= pd.DataFrame (lista_herramientas, columns= ['Nombre'])


# In[16]:


df_herramientas


# In[17]:


# Ejercicio 7


# ### A continuación se muestran algunos ejemplos de evaluación de expresiones aritméticas en Python.

# In[18]:


# Ejercicio 8


# Esta es una expresión aritmética simple para multiplicar y luego sumar números enteros.

# In[19]:


expresion = (3*4)+5
print (expresion)


# In[20]:


# Ejercicio 9


# Esto convertirá 200 minutos en horas

# In[26]:


conversion = 200*(1/60)
print(conversion )


# In[27]:


# Ejercicio 11


# **Autor:** Diego Alejandro Marulanda Martinez

# In[ ]:




