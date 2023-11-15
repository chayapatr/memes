import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('t3_17q6v92.jpg')
print(result)
