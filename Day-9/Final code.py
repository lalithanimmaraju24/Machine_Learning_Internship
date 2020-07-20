import pytesseract as pt
import os
from PIL import Image
from gtts import gTTS
pt.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img=Image.open("sampleimage3.jpg")
mytext=pt.image_to_string(img)
print(mytext)
language='en'
output=gTTS(text=mytext, lang=language,slow=False)
output.save("output2.mp3")
os.system("start output2.mp3")
