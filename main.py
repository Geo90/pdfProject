from PIL import Image
import PIL.Image
from google_trans_new import google_translator

# https://medium.com/@ahmetxgenc/how-to-use-tesseract-on-windows-fe9d2a9ba5c6
# https://developer.ibm.com/languages/python/tutorials/document-scanner/
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'

#https://pyshark.com/translate-text-using-python/
# languages:
# ro, sv, hu, en
translator = google_translator()

files = ['d1', 'd2']
for file in files:
    output = pytesseract.image_to_string(PIL.Image.open(file+'.jpg').convert("RGB"), lang='eng')
    with open(file=file+".txt", mode="w", encoding='utf-8') as output_file:
        translation = translator.translate(output, lang_src='en', lang_tgt='sv')
        output_file.write(str(translation))

