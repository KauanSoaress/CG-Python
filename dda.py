from set_pixel import set_pixel

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