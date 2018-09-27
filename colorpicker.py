import argparse
from PIL import Image


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = Image.open(args['image'])
rgb = image.convert('RGB')
r, g, b = rgb.getpixel((1, 1))
print(f'red={r}, green={g}, blue={b}')
print(f'rgba({r},{g},{b},1)')
r = hex(r)
g = hex(g)
b = hex(b)
print()
print(f'red={r}, green={g}, blue={b}')
r = r[2:]
g = g[2:]
b = b[2:]
print(f'#{r}{g}{b}')
