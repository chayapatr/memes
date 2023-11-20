from PIL import Image

with Image.open('test.gif') as im:
    im.seek(0)
    im.save("test.png")