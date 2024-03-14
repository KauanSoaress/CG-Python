import numpy as np
import matplotlib.pyplot as plt
from criar_img_preta import criar_img_preta
from criar_img_branca import criar_img_branca
from set_pixel import set_pixel
from desenha_seno import desenha_seno
from dda import dda
from bresenham import bresenham
from dda_aa import dda_aa
from cria_poligono import cria_poligono
from poligono import poligono
from insere_ponto import insere_ponto

# Testando as funções

mat = criar_img_preta(100, 100)  # Criando uma matriz 150x100 totalmente preta
# mat = criar_img_branca(150, 100)  # Criando uma matriz 150x100 totalmente branca

# teste = desenha_seno(mat)  # Desenhando um seno na matriz
# teste = dda_aa(mat, 20, 20, 70, 90, 255)  # Desenhando uma reta na matriz

teste = cria_poligono()
teste = insere_ponto(teste, 20, 20)
teste = insere_ponto(teste, 20, 80)
teste = insere_ponto(teste, 80, 80)
teste = insere_ponto(teste, 80, 20)
teste = poligono(mat, teste, 255)

# Exibindo a matriz na escala de 0 a 255
plt.imshow(teste, cmap='gray', vmin=0, vmax=255)  # Usando cmap='gray' para exibir em escala de cinza
plt.show()