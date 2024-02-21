import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak (audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morninng!")

     elif hour>=12 and hour<18:
          speak("Good Afternoon!")
           
     else:
         speak("Good Evening!")
     speak("I am jarvis  sir , how can i help you ?")    

def takeCommand():
     
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("listning...")
          r.pause_threshold = 1.5
          r.energy_threshold = 3000
          audio = r.listen(source)

     try:
          print("Recognizing...")      
          query = r.recognize_google(audio, language='en_in')
          print(f"User said: {query}")

     except Exception as e: 
          print(e)
          print("say that again please.....")
          return "None"
     
     return query
       


if __name__ == "__main__":    
      wishMe()
      Command = takeCommand()
      print("Command:", Command.lower())

      if 'wikipedia' in query :
           speak("Searching Wikipedia...")
           query =query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           speak(results)

      elif 'open youtube' in query :
           webbrowser.open("youtube.com")
