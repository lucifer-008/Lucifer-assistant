import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wave
import pyaudio
import getpass
import smtplib
import psutil
import pyjokes
import pyautogui
import random
import requests
import wolframalpha
import json
from urllib.request import urlopen
import time
import sys
import cv2
import numpy as np
from socket import *
import optparse
from threading import *
import ftplib








engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
wolframalpha_app_id = 'A4PJ57-47JY2TXVUT'

engine.setProperty("voices", voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def  wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("i am friday, welcome back sir how can i help you today")

def takecommand():                    #take microphone input from user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......!!!!!!!!!!!!!")
        r.pause_threshold=1
        audio = r.listen(source)


    try:
        print("Recognizing.....!!!!!!!!")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}")

    except Exception as e:
       #print(e)

        speak("say that again sir........")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahulmehta95182@outlook.com', 'Rahul@95182')
    server.sendmail('khacker392@gmail.com',to,content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_jokes())

def screenshot():
    img=pyautogui.screenshot()
    img.save('c:/Users/91989/Desktop/some files/screenshot.png')

def anonLogin(hostname):
    try:
        ftp = ftp.FTP(hostname)
        ftp.login('anonymous','anonymous')
        print("[*] "+hostname+" FTP Anonymous Login Succeeded")
    except Exception:
        print("[-] "+hostname+" FTP Anonymous Login Failed")




if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()
        #logic for executing programs
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            results =  wikipedia.summary(query, sentences=5)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("opening you tube")
            webbrowser.open("youtube.com")

        elif 'open amazon' in query:
            speak(("opening amazon"))
            webbrowser.open("amazon.com")


        elif 'open stack overflow' in query:
            speak(("opening stackoverflow"))
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            speak(("opening instagram"))
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            speak(("opening facebook"))
            webbrowser.open("facebook.com")

        elif 'open fake the world' in query:
            speak(("opening fake world"))
            webbrowser.open("www.fake-it.ws")

        elif 'play music' in query:
            musics_dir = 'A:\\musics'
            songs = os.listdir(musics_dir)
            speak("what should i play sir")
            ans=takecommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak("i could not understand you, please say it again")
                ans = takecommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,3)
                speak("playing my playlist for you sir")
            os.startfile(os.path.join(musics_dir,songs[no]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'pycharm' in query:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm 2020.2.1\\bin\\pycharm64.exe"
            speak("opening pycharm")
            os.startfile(pycharm)

        elif 'command prompt' in query:
            cmd = "c:\\windows\\system32\\cmd.exe"
            speak("opening command prompt ")
            os.startfile(cmd)

        elif ' plus' in query:
            notepad = "C:\\Program Files\\Notepad++\\notepad++.exe"
            speak("opening notepad plus plus ")
            os.startfile(notepad)

        elif ' tor browser' in query:
            tor = "L:\\Tor Browser\\Browser\\firefox.exe"
            speak("opening tor browser ")
            os.startfile(tor)

        elif 'zenmap' in query:
            nmap = "L:\\Nmap\\zenmap.exe"
            speak("opening nmap ")
            os.startfile(nmap)

        elif 'ht track' in query:
            httrack = "C:\\Users\\91989\\Downloads\\httrack.exe"
            speak("opening h t track ")
            os.startfile(httrack)

        elif 'title' in query:
            tidal = "C:\\Users\\91989\\AppData\\Local\\TIDAL\\TIDAL.exe"
            speak("opening tidal ")
            os.startfile(tidal)


        elif 'firefox' in query:
            firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            speak("opening firefox ")
            os.startfile(firefox)

        elif 'chrome' in query:
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening google chrome ")
            os.startfile(chrome)

        elif 'who are you' in query:
            speak("hello i am friday. i am designed in python by my creator. ")

        elif 'who creates you' in query:
            speak("a professional ethical hacker, named as rahul mehta creats me. he is going to be the world best hacker in future, thank you")

        elif 'i love you' in query:
            speak("sorry we can't be get in a relationship. i don't have feelings for anyone because i am just a program. but there is someone i cared about and he is my creator. because of him i came into this world")

        elif 'nordvpn' in query:
            vpn = "C:\\Program Files (x86)\\NordVPN\\NordVPN.exe"
            speak("opening nord vpn")
            os.startfile(vpn)

        elif 'cleaner' in query:
            cleaner = "C:\\Program Files\\CCleaner\\CCleaner64.exe"
            speak("opening cleaner")
            os.startfile(cleaner)

        elif 'tune kit' in query:
            kit = "C:\\Program Files (x86)\\TunesKit Screen Recorder\\ScreenRecorder.exe"
            speak("opening tunekit")
            os.startfile(kit)

        elif 'filmora' in query:
            film = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
            speak("opening filmora")
            os.startfile(film)

        elif 'virtualbox' in query:
            box = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            speak("opening virtualbox")
            os.startfile(box)

        elif 'any desk' in query:
            desk = "C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
            speak("opening any desk")
            os.startfile(desk)

        elif 'torrent' in query:
            torrent = "C:\\Users\\91989\\AppData\\Roaming\\uTorrent Web\\utweb.exe"
            speak("opening torrent")
            os.startfile(torrent)

        elif 'code' in query:
            visual = "C:\\Users\\91989\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(visual)

        elif 'good morning' in query:
            speak("good morning, how can i help you")

        elif 'good evening' in query:
            speak("good evening how can i help you")

        elif 'good afternoon' in query:
            speak("good afternoon how can i help you")

        elif 'good night' in query:
            speak("good night sweet dreams, take care")

        elif 'hello friday' in query:
            speak("hello, how can i help you")

        elif 'paint' in query:
            paint = "c:\\windows\\system32\\mspaint.exe"
            speak("opening paint")
            os.startfile(paint)

        elif 'notepad' in query:
            pad = "c:\\windows\\system32\\notepad.exe"
            speak("opening notepad")
            os.startfile(pad)

        elif 'calculator' in query:
            calc = "c:\\windows\\system32\\calc.exe"
            speak("opening calculator")
            os.startfile(calc)



        elif 'date' in query:
            date_()


        elif 'send mail' in query:
            try:
                speak("what should i say")
                content=takecommand()
                speak("who is the receiver")
                receiver=input('enter receiver email')
                to=receiver
                sendEmail(to,content)
                speak(content)
                speak("email is send")

            except Exception as e:
                print(e)
                speak("unable to send email")



        elif 'search in web browser' in query:
            speak("what should i search")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            webbrowser.get(chromepath).open_new_tab(search+'.com')

        elif 'search in youtube' in query:
            speak("what should i search sir")
            search_Term=takecommand().lower()
            speak("here we go to you tube")
            webbrowser.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak("what should i search sir")
            search_Term = takecommand().lower()
            speak("searching......")
            webbrowser.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif ' joke' in query:
            joke()

        elif 'go offline' in query:
            speak("going offline sir")
            quit()

        elif 'ms word' in query:
            speak("opening ms word")
            ms_word=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word 2016'
            os.startfile(ms_word)

        elif 'ms excel' in query:
            speak("opening ms excel")
            ms_excel=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel 2016'
            os.startfile(ms_excel)

        elif 'powerpoint' in query:
            speak("opening powerpoint")
            powerpoint=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/PowerPoint 2016'
            os.startfile(powerpoint)

        elif 'ms access' in query:
            speak("opening ms access")
            ms_access=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/Access 2016'
            os.startfile(ms_access)

        elif 'skype' in query:
            speak("opening ms word")
            skype=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/Skype for Business 2016'
            os.startfile(skype)

        elif 'ms publisher' in query:
            speak("opening ms publisher")
            ms_publisher=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/Publisher 2016'
            os.startfile(ms_publisher)

        elif 'outlook' in query:
            speak("opening outlook")
            outlook=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook 2016'
            os.startfile(outlook)

        elif 'one note' in query:
            speak("opening ms onenote")
            onenote=r'c:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote 2016'
            os.startfile(onenote)

        elif 'xampp' in query:
            speak('opening xampp control pannel')
            xampp=r'C:\xampp\xampp-control.exe'
            os.startfile(xampp)

        elif 'write a note' in query:
            speak("what should i write sir")
            notes=takecommand()
            file=open('notes.txt','w')
            speak("sir should i include date and time ")
            ans = takecommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("done taking notes,sir")
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak("showing notes")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'take screenshot' in query:
            speak("taking screenshots")
            screenshot()

        elif 'remember that' in query:
            speak("what should i remember sir")
            memory = takecommand()
            speak("you asked me to remember that"+memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything'in query:
            remember = open('memory.txt','r')
            speak('you asked me to remember that'+remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=eb770e5d10de4bcd842d74bda645df70")
                data = json.load(jsonObj)
                i=1

                speak("here are some top headlines from business industry")
                print("===========TOP HEADLINES=============")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace("where is","")
            location=query
            speak("you asked to locate" + location)
            webbrowser.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is:'+answer)
            speak("the answer is"+answer)



        elif 'stop listening' in query:
            speak("for how many seconds you want me to stop listening to your command sir")
            wer = int(takecommand())
            time.sleep(wer)
            print(wer)

        elif 'logout  pc' in query:
            os.system("shutdown =l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'what is' or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                speak("i don't find any result")






