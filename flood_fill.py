from set_pixel import set_pixel

def flood_fill(img, cor_inicial, cor_pintura, x, y):
  if x < 0 or y < 0 or x >= len(img) or y >= len(img[0]) or img[x][y] != cor_inicial:
    return
  
  set_pixel(img, x, y, cor_pintura)

  while x + 1 < len(img) and img[x+1][y] == cor_inicial:
    flood_fill(img, cor_inicial, cor_pintura, x, y+1)
    flood_fill(img, cor_inicial, cor_pintura, x, y-1)

  while x - 1 >= 0 and img[x-1][y] == cor_inicial:
    flood_fill(img, cor_inicial, cor_pintura, x, y+1)
    flood_fill(img, cor_inicial, cor_pintura, x, y-1)