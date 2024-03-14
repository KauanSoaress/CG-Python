import numpy as np
from dda import dda

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