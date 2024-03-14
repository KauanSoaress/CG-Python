from dda import dda

def poligono(im, pol, intensidade):
  img = im

  for i in range(len(pol)-1):
    img = dda(img, pol[i][0], pol[i][1], pol[i+1][0], pol[i+1][1], intensidade)

  img = dda(img, pol[len(pol)-1][0], pol[len(pol)-1][1], pol[0][0], pol[0][1], intensidade)

  return img