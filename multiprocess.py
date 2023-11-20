import easyocr
from wordsegment import load, segment
from PIL import Image
import csv
import pandas as pd
from torch.multiprocessing import Process, Pool
import os

load()

cluster = 'memesopdidnotlike'
reader = easyocr.Reader(['en'])
fetched = pd.read_csv(f'{cluster}.csv')
ocrd = open('ocrd-op.csv', "w", newline='', encoding="utf-8")
writer = csv.writer(ocrd)
writer.writerow(['post_name', 'text'])

# ---------------------------------------- #

def extract_image_from_gif(n):
    with Image.open(f"{cluster}/{n}.gif") as im:
        im.seek(0)
        im.save(f"{cluster}/{n}.png")

def easy_ocr(reader, path):
    result = reader.readtext(path, detail=0, paragraph=True, y_ths = -0.05)
    return result

def word_segment(sentences):
    return "\n".join([ " ".join(segment(sentence)) for sentence in sentences ])

def read_meme(path):
    print(f"read {path}")
    [n, t] = path.split(".")
    if t == "gif":
        extract_image_from_gif(n)
    text = word_segment(easy_ocr(reader, f"{cluster}/{n}.{t if t != 'gif' else 'png'}"))
    writer.writerow([path.split(".")[0], text, fetched.loc[fetched['img_path'] == path]['post_caption'].item()])
    return [path, text]

# ---------------------------------------- #

docs = []
if __name__ == '__main__':
    img_paths = fetched.img_path
    n = 4
    print(n)
    p = Pool(n)
    for res in p.imap(read_meme, img_paths):
        writer.writerow([res[0].split(".")[0], res[1], fetched.loc[fetched['img_path'] == res[0]]['post_caption'].item()])
        print("writing", res[0])