import numpy as np
import matplotlib.pyplot as plt
from criar_img_preta import criar_img_preta
from criar_img_branca import criar_img_branca
from set_pixel import set_pixel
from desenha_seno import desenha_seno
from dda import dda
from bresenham import bresenham

# Testando as funções

mat = criar_img_preta(100, 100)  # Criando uma matriz 150x100 totalmente preta
# mat = criar_img_branca(150, 100)  # Criando uma matriz 150x100 totalmente branca

# seno = desenha_seno(mat)  # Desenhando um seno na matriz
reta = dda(mat, 20, 20, 70, 90, 255)  # Desenhando uma reta na matriz

# Exibindo a matriz na escala de 0 a 255
plt.imshow(reta, cmap='gray', vmin=0, vmax=255)  # Usando cmap='gray' para exibir em escala de cinza
plt.show()