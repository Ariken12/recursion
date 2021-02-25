import PIL
from PIL import ImageDraw, Image

h = 12000
w = 12000
r = 12
tup = (0, 0, h, w)
a = 0
name = "recursion.png"
black = (0, 0, 0)
white = (255, 255, 255)
color = {'b': black, 'w': white}

def alert(text):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(text)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

img = Image.new('RGB', (h, w), "black")
draw = ImageDraw.Draw(img)

def line(xb, yb, xe, ye, r):

    dx = abs(xe - xb) / (r * r)
    dy = abs(ye - yb) / (r * r)
    x = xb
    y = yb
    while x < xe:

        draw.rectangle((x, y, x + dx, y + dy), color['w'], color['b'])
        print(x, y)
        x += dx
        y += dy

def poligon(tup):
    global r
    draw.rectangle((tup[0], tup[1], tup[2], tup[3]), color['w'])
    tup = (tup[0]+r, tup[1]+r, tup[2]-r, tup[3]-r)
    draw.rectangle((tup[0]+5, tup[1]+5, tup[2]-5, tup[3]-5), color['b'])
    return (tup[0], tup[1], tup[2], tup[3])

def ellipse(tup):
    global r
    draw.ellipse(tup, color['w'])
    tup1 = (tup[0]+r, tup[1]+r, tup[2]-r, tup[3]-r)
    draw.ellipse(tup1, color['b'])
    return tup[0] + (tup[2] - tup[0]) / 2 - (tup[2] - tup[0]) / (2*(2 ** 0.5)), tup[1] + (tup[3] - tup[1]) / 2 - (tup[2] - tup[0]) / (2*(2 ** 0.5)), tup[0] + (tup[2] - tup[1]) / 2 + (tup[2] - tup[0]) / (2*(2 ** 0.5)), tup[1] + (tup[3] - tup[1]) / 2 + (tup[2] - tup[0]) / (2*(2 ** 0.5))

while a < 15:
    alert(a)
    color = {'b': white, 'w': black}
    tup = poligon(tup)
    tup = ellipse(tup)
    color = {'b': black, 'w': white}
    tup = poligon(tup)
    tup = ellipse(tup)
    
    a += 1

## line(h/4, h/4, w*0.75, h*0.75, 100)

img.show()
img.save(name)
