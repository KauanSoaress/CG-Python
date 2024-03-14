import numpy as np
from set_pixel import set_pixel

def bresenham(img, xi, yi, xf, yf, intensidade):
  im = img

  if xf < xi:
    aux = xf
    xf = xi
    xi = aux
    aux = yf
    yf = yi
    yi = aux

  dx = abs(xf - xi)
  dy = abs(yf - yi)

  aux = 0
  if dy > dx:
    aux = dx
    dx = dy
    dy = aux
    aux = 1

  y = 0

  dy2 = 2*dy
  dy2dx2 = dy2 - 2*dx
  s = np.sign(yf-yi)

  p = dx - dy2

  for x in range(dx):
    if p < 0:
      p = p - dy2dx2
      y = y + 1
    else:
      p = p - dy2
    
    if aux == 0:
      im = set_pixel(im, xi + x, yi + s*y, intensidade)
      im = set_pixel(im, xi + y, yi + s*x, intensidade)
  
  return im