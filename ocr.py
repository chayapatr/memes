from memeocr import MemeOCR

ocr = MemeOCR()
txt = ocr.recognize('./meme.jpeg')
txt = ocr.recognize('./meme2.jpg')
print(txt)