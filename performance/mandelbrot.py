"""
Drawing the Mandelbrot set

based on R code by Myles Harrison
http://www.everydayanalytics.ca

original source of the Python code:
   https://github.com/krother/Python3_Package_Examples
   MIT License
"""
import numpy as np
from PIL import Image

def get_next_iter(z, c, index):
    """calculate the next generation of the entire matrix"""
    newz = []
    for x in range(z.shape[0]):
        for y in range(z.shape[1]):
            if index[x, y]:
                newz.append(z[x, y] ** 2 + c[x, y])
            else:
                newz.append(999)
    z = np.array(newz).reshape(z.shape)
    return z


def calculate(z, k, c):
    index = z < 2
    z = get_next_iter(z, c, index)
    k[index] = k[index] + 1
    return z, k


def draw_mandelbrot(xmin=-2, xmax=1.0, nx=500,
                    ymin=-1.5, ymax=1.5, ny=500,
                    n=100):
  x = np.linspace(xmin, xmax, nx)
  real = np.outer(x, np.ones(ny))

  y = np.linspace(ymin, ymax, ny)
  imag = 1j * np.outer(np.ones(nx), y)

  c = real + imag

  z = np.zeros((nx, ny)) * 1j
  k = np.zeros((nx, ny))

  for recursion in range(1, n):
      z, k = calculate(z, k, c)

  return k


if __name__ == '__main__':
    mtx = draw_mandelbrot()
    mtx = 255 * mtx / mtx.max()
    mtx = mtx.astype(np.uint8)
    im = Image.fromarray(mtx, 'L')
    im.save('mandelbrot.png')
