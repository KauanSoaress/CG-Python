import numpy as np

def criar_img_preta(larg, alt):
  # criando uma matriz totalmente preta na escala de 0 a 255
  mat = np.zeros((alt, larg)) # Criando uma matriz de zeros
  return mat