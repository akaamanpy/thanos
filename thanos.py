from PIL import ImageTk,Image
import os
import requests
import wikipedia
import pyttsx3
import pyjokes
import pywhatkit
from tkinter import*
import webbrowser
import subprocess


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

root=Tk()
root.title("Thanos Command Bar")



def search():
    cmd=entry.get()
    
    if "google" in cmd:
        webbrowser.open("https://www.google.com/")
        talk("oppening google")
    
    elif "play" in cmd:
        song = cmd.replace("play", "")
        pywhatkit.playonyt(song)
        talk('playing ' + song)
    
    elif "tell me jokes" in cmd:
        talk(pyjokes.get_joke())
    
    elif 'who is' in cmd:
        person = cmd.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
            
    
    elif "play hiphop" in cmd:
        webbrowser.open("https://www.youtube.com/watch?v=lsJLLEwUYZM&list=PLAPo1R_GVX4IZGbDvUH60bOwIOnZplZzM")
        talk("playing hiphop")
    
    elif "play billboard" in cmd:
        webbrowser.open("https://www.youtube.com/watch?v=H5v3kku4y6Q&list=PLDIoUOhQQPlXr63I_vwF9GD8sAKh77dWU")
    
    elif 'what is' in cmd:
        person = cmd.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "weather" in cmd:
        wthr = cmd.replace("weather of", "")

        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = wthr

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            talk("the weather outside of" + str(wthr) + "is" + str(temp) + "degree fahrenheit and a" + str(weather) + "day")

    elif "who made you" in cmd:
        talk("my master who programed me is aka aman he is a junior in python course")

    elif "open notepad" in cmd:
        note = subprocess.Popen("notepad")
        talk("oppening notepad")
    
    elif "sh /-l" in cmd:
        talk("logging off computer")
        os.system("shutdown /l")

    elif "sh /-s" in cmd:
        talk("shutting down computer")
        os.system("shutdown /s")

    elif "sh /-r" in cmd:
        talk("restarting computer")
        os.system("shutdown /r")
    elif "youtube" in cmd:
        webbrowser.open("https://www.youtube.com")
        talk("oppening youtube")

    elif "gmail" in cmd:
        webbrowser.open("https://accounts.google.com/b/1/AddMailService")
        talk("oppening gmail")
    elif "insta" in cmd:
        webbrowser.open("https://www.instagram.com/")
        talk("oppening instagram")

    elif "telegram" in cmd:
        webbrowser.open("https://web.telegram.org/")
        talk("oppening telegram")

    elif "facebook" in cmd:
        webbrowser.open("https://www.facebook.com/")
        talk("oppening facebook")
    elif "help" in cmd:
        webbrowser.open("https://docs.google.com/uc?export=download&id=1YzQCbCovCA6nrS8N_4QnywKOaW6YrFFx")
        talk("dawnloading commands")
    


label1=Label(root,text="Enter command here :",font=("arial",10,"bold"))
label1.grid(row=0,column=0)

label1=Label(root,text='you can dawnload commands by entering "help" command',font=("italic",7))
label1.grid(row=2,column=0)


entry=Entry(root,width=40)
entry.grid(row=0,column=1)

button=Button(root,text="submit",command=search)
button.grid(row=1,column=0,columnspan=2,pady=10)

root.mainloop()
