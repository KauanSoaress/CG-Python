from cmath import cos, sin
import numpy as np
from math import floor
from cria_poligono import cria_poligono
from poligono import poligono
from insere_ponto import insere_ponto

def circunferencia(im, xc, yc, r, intensidade):
  img = im

  c = cria_poligono()

  for ang in np.arange(0, 2*np.pi, 0.25):
    c = insere_ponto(c, floor(xc + r*cos(ang)), floor(yc + r*sin(ang)))
  
  img = poligono(img, c, intensidade)

  return img 