import easyocr
import pytesseract
from PIL import Image

def easy_ocr(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image, detail=0, paragraph=True, y_ths = -0.05)
    return result

def tess(image):
    print(pytesseract.image_to_string('test.jpeg'))

from wordsegment import load, segment
load()

print([segment(i) for i in easy_ocr('meme2.jpg')])
# print([i[1] for i in easy_ocr('jews.jpeg')])

import sys
from memeocr import MemeOCR
from autocorrect import Speller

spell = Speller()

ocr = MemeOCR()
txt = ocr.recognize("./meme.jpeg")

print(txt)
# print(([spell(x.lower()) for x in [*txt, *txt2, *txt4]]))