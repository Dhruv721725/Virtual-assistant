import speech_recognition as sr
import pyautogui as ptg 
import pyttsx3 as ptx

def spk(text):
   e= ptx.init()
   speakers=e.getProperty('voices')
   e.setProperty('voice',speakers[1].id)
   e.setProperty('rate',125)
   e.setProperty('volume',1)
   e.say(text)
   e.runAndWait()

def speech_to_text():
   r=sr.Recognizer()
   with sr.Microphone() as src:
      print("listening...")
      spk('i')
      r.pause_threshold=0.5
      r.energy_threshold=1500
      aud=r.listen(src)
      try:
         print("recognizing...")
         q=r.recognize_google(aud,language="en-in")
         return q
      except Exception:
         print("voice not recognized, check internet connection.")
         return ""

def start():
   ptg.press('f5')

def close():
   ptg.press('esc')

def cont():
   ptg.keyDown('shift')
   ptg.keyDown('f5')
   ptg.keyUp('f5')
   ptg.keyUp('shift')

def next():
   ptg.press('right')

def prev():
   ptg.press('left')

while True:
   text=speech_to_text()
   words=text.split(' ')
   lwords=list(map(str.lower,words))
   print(lwords)

   if 'jimmy' in lwords:
    if 'quit' in lwords:
       spk('quitting')
       break
    elif 'next' in lwords:
       spk('next slide')
       next()
    elif 'previous' in lwords:
       spk('previous slide')
       prev()
    elif 'start' in lwords:
       spk('starting slide show')
       start()
    elif 'close' in lwords:
       spk('closing slide show')
       close()
    elif 'continue' in lwords:
       spk('cointinuing slide show')
       cont()
    else:
       continue




