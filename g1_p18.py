#%%

from mis_funciones import suma

a = suma(2,3)
print(a)

#%%

def generador_galaxias(n):
    galaxias = []

    x = generador_fibonacci(n,142)
    for _x in x:
        if x <= x and x <0.4:
            galaxias.append('eliptica')
        elif (x >= 0.4) and (x < 0.7):
            galaxias.append('espiral')
        elif (0.7 <= x) and (x <= 0.9):
            galaxias.append('enana')
        else:
            galaxias.append('irregular')
    return galaxias

g = generador_galaxias(10000)
print
    
# %%
