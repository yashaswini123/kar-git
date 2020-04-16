import PyPDF2 as Pydf
import googletrans
from googletrans import Translator

pdf_file = open('sample.pdf','rb') # enter the name of your pdf 
pdfreader = Pydf.PdfFileReader(pdf_file) # reading the pdf
page = pdfreader.getPage(0) # give the page number of pdf (starts with 0)
a = page.extractText() # extracting the data from pdf 

# google translate 

translator = Translator()
translated = translator.translate(a,dest='de') # dest = the language you want to translate
print(translated.text)







