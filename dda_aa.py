from math import floor
from numpy import sign
from set_pixel import set_pixel

def dda_aa(img, xi, yi, xf, yf, intensidade):
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
    
    if passo_x == 1:
      prop = abs(y - floor(y))

      set_pixel(im, floor(x), floor(y), round((1-prop)*intensidade))
      set_pixel(im, floor(x), floor(y + sign(passo_y)), round(prop*intensidade))
    else:
      prop = abs(x - floor(x))

      set_pixel(im, floor(x), floor(y), round((1-prop)*intensidade))
      set_pixel(im, floor(x + sign(passo_x)), floor(y), round(prop*intensidade))

  return im