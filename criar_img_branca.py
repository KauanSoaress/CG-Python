import numpy as np

def criar_img_branca(larg, alt):
  # Criando uma matriz totalmente branca na escala de 0 a 255
  mat = np.ones((alt, larg)) * 255  # Multiplicando por 255 para obter a escala de 0 a 255
  return mat