import numpy as np
import matplotlib.pyplot as plt

def criar_img_preta(larg, alt):
  # criando uma matriz totalmente preta na escala de 0 a 255
  mat = np.zeros((alt, larg)) # Criando uma matriz de zeros
  return mat

def criar_img_branca(larg, alt):
  # Criando uma matriz totalmente branca na escala de 0 a 255
  mat = np.ones((alt, larg)) * 255  # Multiplicando por 255 para obter a escala de 0 a 255
  return mat

def set_pixel(mat, x, y, valor):
  # Atribuindo um valor a um pixel da matriz
  mat[y, x] = valor

# Algoritmo para desenhar um seno na imagem, usando o algoritmo DDA
def desenha_seno(img):
  im = img

  rows, cols = img.shape

  xant = 0
  yant = int(100*np.sin(xant/16) + rows/2)  # Initialize yant to the first y-value of the sine wave

  # Desenhando um seno na matriz
  for x in range(cols):
    y = int(100*np.sin(x/16) + rows/2)
    
    im = dda(im, xant, yant, x , y, 255)

    xant = x
    yant = y

  return img

# Algoritmo DDA para desenhar uma linha na matriz
def dda(img, xi, yi, xf, yf, intensidade):
  im = img

  dx = xf - xi
  dy = yf - yi

  passos = abs(dx) if abs(dx) > abs(dy) else abs(dy)

  if passos == 0:  # If the initial and final points are the same, skip this iteration
    return im

  passo_x = dx / passos
  passo_y = dy / passos

  x = xi
  y = yi

  set_pixel(im, int(x), int(y), intensidade)

  for i in range(passos):
    x += passo_x
    y += passo_y
    set_pixel(im, int(x), int(y), intensidade)

  return im


# Testando as funções

mat = criar_img_preta(100, 100)  # Criando uma matriz 150x100 totalmente preta
# mat = criar_img_branca(150, 100)  # Criando uma matriz 150x100 totalmente branca

# seno = desenha_seno(mat)  # Desenhando um seno na matriz
reta = dda(mat, 20, 20, 70, 90, 255)  # Desenhando uma reta na matriz

# Exibindo a matriz na escala de 0 a 255
plt.imshow(reta, cmap='gray', vmin=0, vmax=255)  # Usando cmap='gray' para exibir em escala de cinza
plt.show()