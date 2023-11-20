import sys
from memeocrs import MemeOCR
from autocorrect import Speller

spell = Speller()

ocr = MemeOCR()
txt = ocr.recognize("./meme.jpeg")
txt2 = ocr.recognize("./meme2.jpg")
txt3 = ocr.recognize("./meme3.webp")
txt4 = ocr.recognize("./meme4.png")

print(txt4)
print(([spell(x.lower()) for x in [*txt, *txt2, *txt4]]))