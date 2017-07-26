# from pytesser import *
# image = Image.open('2.jpg')  # Open image object using PIL
# print image_to_string(image)     # Run tesseract.exe on image

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print ("Import Error !")
    raise  SystemExit

import  os
print(os.path.exists('2.jpg'))
#C:\Program Files (x86)\Tesseract-OCR
#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
tessdata_dir = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

ima = Image.open('test.png')
#print(pytesseract.image_to_string(image))
print(pytesseract.image_to_string(image=ima, lang='eng', config=tessdata_dir))
