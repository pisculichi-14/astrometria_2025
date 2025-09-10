# %%


texto = "Hello world!"
print(texto)

valor = 1.

entero = 3

complejo = 1j

# %%

nombre = "Mario"
apellido = "Sgró"

print(nombre + apellido)

# %%

a = 1
b = 2

c = a + b


#%%

a = 1e-3


# %%


a = 4**(1/b)

a = 13 % 10

abs(a)

#%%

#para definir funciones usamos esto

def mi_funcion(nombre):
    texto = f"Hola {nombre} :D"
    return texto


# %%

def suma(a, b, d = 0):
    """
    Esta función hace la suma de a con b y hace opcionalmente d

    parámetros
     a:
     b:
     d (opcional:

    Devuelve:
      c

    Modo de uso:
     c = suma(1,2,d = 4)
    """
    c = a + b + d
    return c



# %%

import mis_funciones as misfuncs

print(misfuncs.suma(1,2,d=5,e=5))