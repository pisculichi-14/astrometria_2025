#%%

import matplotlib.pyplot as plt
from mis_funciones import generador_fibonacci

def ej19f1():
    X = generador_fibonacci(1000,142)
    _x = x[1:]
    _y = x[:-1]
    plt.plot(_x,_y,'ro')


#%%

ej19f1()


#%%

x = np.random.random(10)
print(x)


# %%
