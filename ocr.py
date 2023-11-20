import easyocr
from wordsegment import load, segment
from PIL import Image
import csv
import pandas as pd

load()

def extract_image_from_gif(n):
    with Image.open(f"fetched/{n}.gif") as im:
        im.seek(0)
        im.save(f"fetched/{n}.png")

def easy_ocr(path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(path, detail=0, paragraph=True, y_ths = -0.05)
    return result

def word_segment(sentences):
    return "\n".join([ " ".join(segment(sentence)) for sentence in sentences ])

def read_meme(path):
    [n, t] = path.split(".")
    if t == "gif":
        extract_image_from_gif(n)
    return word_segment(easy_ocr(f"fetched/{n}.{t if t != 'gif' else 'png'}"))

fetched = pd.read_csv('fetched.csv')

ocrd = open('ocrd.csv', "w", newline='', encoding="utf-8")
writer = csv.writer(ocrd)
writer.writerow(['post_name', 'text', 'caption'])

img_paths = fetched.img_path
for img_path in img_paths:
    print(f"read {img_path}")
    if(img_path.split(".")[-1] == "gifv"):
        continue
    text = read_meme(img_path)
    writer.writerow([img_path.split(".")[0], text, fetched.loc[fetched['img_path'] == img_path]['post_caption'].item()])
ocrd.close()