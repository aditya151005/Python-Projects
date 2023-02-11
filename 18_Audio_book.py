import pyttsx3
import PyPDF2
book=open("core_Python.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init() 
rate=speaker.setProperty('rate', 120)
rate = speaker.getProperty('rate')   
print(rate)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

for num in range(450,pages):  
     page=pdfReader.getPage(num)
     text=page.extractText()
     speaker.say(text)
     speaker.runAndWait()
speaker.stop()