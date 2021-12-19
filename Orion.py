import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import pyautogui
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
pyautogui.FAILSAFE = False

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("ORION at your service sir. What would you like to do sir?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        #r.adjust_for_ambient_noise(source, duration=0)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak('Say that again please')
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube Sir')
            #c = webbrowser.get('Google Chrome')
            webbrowser.open("youtube.com")

        elif 'how are you' in query:
            speak('M good sir,how are you ?')
        elif ' am also good' in query:
            speak('Well thats very good sir')
        elif 'not good' in query:
            speak('Why sir,what happened? Is everything alright?')

        elif 'open google' in query:
            speak('Opening Google Sir')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'terminate' in query:
            speak('Okay sir and sorry sir for any inconvenience caused by me')
            sys.exit()        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'bank project' in query:
            speak('Opening Bank.py')
            pyautogui.press('winleft');pyautogui.doubleClick(138,1063);pyautogui.typewrite("python");pyautogui.press('enter');pyautogui.doubleClick(1079,1048);pyautogui.doubleClick(1272,941);pyautogui.hotkey('ctrl','n');pyautogui.hotkey('ctrl','o');pyautogui.doubleClick(576,604);pyautogui.typewrite("bank.py");pyautogui.press('enter')

            #speak('Sir,shall I run your project?')
        elif 'run my project' in query:
            speak('Executing Bank.py')
            pyautogui.press('f5')
            speak('executing your project,please wait')
            speak('What would you like to do in your project sir?')
          #  pyautogui.hotkeys('alt','f4');pyautogui.press('enter')
       # elif 'execute my project' in query:
        #    speak('Okay Sir.Which option would you like to choose sir?')

        elif ' to log in' in query:
            pyautogui.typewrite('1');pyautogui.press('enter')
            speak('Okay Sir,May I login as Mr Aman ?')
        elif 'login my account' in query:
            pyautogui.typewrite('ospredator7@gmail.com');pyautogui.press('enter');pyautogui.typewrite('piroplayer');pyautogui.press('enter')
            speak('loading...')
            speak('Please Wait')
            speak('Login successful')
            time.sleep(3)
            #speak('Redirecting to the home page')
            speak('now what would you like to do sir?')
            

        elif 'withdraw money' in query:
            pyautogui.typewrite('1');pyautogui.press('enter')
            speak('sir ,if you allow ,may i enter your account credentials?')
            
        elif 'please enter my account number' in query:
            speak('okay sir')
            pyautogui.typewrite('98637854782');pyautogui.press('enter')
            speak('how much money would you like to withdraw from your account sir')
        elif '500' in query:
            speak('okay sir,as you say.')
            pyautogui.typewrite('500');pyautogui.press('enter')
            time.sleep(3)
            speak('Sir,can you please enter the OTP sent on your email')
            time.sleep(15)
            speak('Congratulations,Money successfully withdrawn from your account')

        elif 'add money' in query:
            speak('Okay Sir.')
            pyautogui.typewrite('2');pyautogui.press('enter')
            speak('sir ,if you allow ,may i enter your account credentials?')
        elif 'enter my account number' in query:
            speak('okay sir')
            pyautogui.typewrite('98637854782');pyautogui.press('enter')
            speak('how much money you would like to add sir')
        elif 'add 10000 rupees ' in query:
            speak('okay sir,as you say')
            pyautogui.typewrite('10000');pyautogui.press('enter')
            speak('Adding money to your account,please wait')
            speak('Sending request')
            time.sleep(2)
            speak('Sir,can you please enter the OTP sent on your email')
            time.sleep(15)
            speak('Congratulations,Money Added Sucessfully to your Account')
        
        elif 'close my project' in query:
            speak('sure sir')
            pyautogui.hotkey('alt','f4');pyautogui.press('enter')

        elif 'email to Aman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "demo@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e :
                print(e)
                speak("Sorry my friend Aman bhai. I am not able to send this email")
        elif 'created' in query:
                speak("Mr SYED AMAN SHAH created me.")
        elif 'shut down my laptop' in query:
            #pyautogui.press(['alt','f4'])
            os.system("shutdown /s /t 1")

        elif 'register' in query:
            speak('Okay sir.')
            pyautogui.typewrite('2');pyautogui.press('enter')
            speak('Sir,may i create a demo user with your information')
        elif 'demo user' in query:
            speak('okay sir,as you say')
            pyautogui.typewrite('Sohail');pyautogui.press('enter');pyautogui.typewrite('Basu');pyautogui.press('enter');pyautogui.typewrite('9875467865');pyautogui.press('enter');pyautogui.typewrite('Indore');pyautogui.press('enter');pyautogui.typewrite('1000');pyautogui.press('enter');pyautogui.typewrite('sohailbasuu@gmail.com');pyautogui.press('enter');pyautogui.typewrite('12345');pyautogui.press('enter');pyautogui.typewrite('12345');pyautogui.press('enter')
            speak('Sir,can you please enter the OTP sent on your email')
         #   speak('Congratulations sir,new account created successfully')
        #elif '' in query:
        #   pyautogui.typewrite()

        elif 'transaction statistics' in query:
            speak('loading transaction statistics')
            pyautogui.typewrite('3');pyautogui.press('enter')
        elif 'maximize the graph window' in query:
            speak('Maximizing the window')
            pyautogui.click(916,214)
            pyautogui.click(662,511)
            pyautogui.hotkey('win','up')

        elif 'net banking' in query:
            speak('Okay sir')
            pyautogui.typewrite('4');pyautogui.press('enter')
            speak('Now what would you like to do sir?')
        elif 'send money' in query:
            speak('Okay sir')
            pyautogui.typewrite('1');pyautogui.press('enter')
            #speak('Would you like to transfer money to any AMD Bank Account')
        #elif 'bank account' in query:
         #   speak('okay sir,as you say')
            pyautogui.typewrite('1');pyautogui.press('enter')
          #  speak('sir,may i enter your account number in field of sender account number ')
        #elif 'enter my account number in field of sender account number' in query:
            pyautogui.typewrite('98637854782');pyautogui.press('enter')
         #   speak('sir, to whom do you want to send money?')
            
        #elif ' Arjun' in query:
         #   speak('okay sir,entering Mr Arjuns account')
            pyautogui.typewrite('87720167469');pyautogui.press('enter')
            pyautogui.typewrite('demo');pyautogui.press('enter')
            speak('sir,may i know how much money is to be sent?')
        elif 'send 3000 ' in query:
            speak('okay sir')
            pyautogui.typewrite('3000');pyautogui.press('enter')
            speak('sir,can you please enter the OTP sent on your registered email.')
            speak('sending request,please wait')
            time.sleep(20)
            speak('Congratulations,Money Tranferred Successfully')

        elif 'account statement' in query:
            speak('Okay sir')
            pyautogui.typewrite('2');pyautogui.press('enter')
            speak('do you want to view account statement?')
        elif 'view it' in query:
            speak('Okay sir,as you say')
            pyautogui.typewrite('1');pyautogui.press('enter')

        elif 'delete account' in query:
             pyautogui.typewrite('5');pyautogui.press('enter')
             speak('DELETING YOUR ACCOUNT WILL LEAD TO PERMANENT LOSS OF DATA WHICH WOULD NOT BE RECOVERED.')
             speak('Are you sure you want to delete your Account?')
        elif 'yes delete my account' in query:
             speak('okay sir')
             pyautogui.typewrite('Yes');pyautogui.press('enter')
             speak('sir,can you please enter the OTP sent on your registered email.')
             time.sleep(13)
             speak('Congratulations,Account Deleted Successfully')
             
             
        elif 'close all windows' in query:
            speak('Closing All opened windows')
            pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4'); pyautogui.hotkey('alt','f4')

        elif 'execute my project again' in query:
            speak('Sure sir,please wait')
            pyautogui.hotkey('alt','f4'); pyautogui.press('f5')
            speak('What would you like to do sir')

        elif 'switch to other window' in query:
            speak('Switching to other window')
            pyautogui.hotkey('alt','tab')

        elif 'close this window' in query:
            speak('Closing current window')
            pyautogui.hotkey('alt','f4')

        elif 'appreciating' in query:
            speak('well thank you very much Ms Malti Saahi for appreciating me and thank you very much for sparing time from your busy schedule')

            
        elif 'bye' in query:
                speak("Goodbye Sir,Have Nice Day.")
                sys.exit()
