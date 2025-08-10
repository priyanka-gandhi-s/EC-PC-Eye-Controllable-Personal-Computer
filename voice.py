'''owner of the Eye contollable personal computer S.Priyanka Gandhi lanched at 15.6.2022

'''
import smtplib
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess
from email.message import EmailMessage
import webbrowser
MASTER = "master"


#speak function to pronounce the given string
def speak(text):
    engine = pyttsx3.init('sapi5')  # initialize engine fresh each time
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("Welcome to EC PC")
speak("This is a test to check if speech is working multiple times.")
speak("If you hear this, it is working fine.")

#the hello function
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning "+ MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon "+ MASTER)
    else:
        speak("Good Evening "+ MASTER)

wishme()

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said : {query}\n")
    except Exception as e:
        print("say that again")
        return None  # Return None (not string "None")
    return query



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('softwarevidhai16@gmail.com', 'ekovycjmmloaksdd')
    email = EmailMessage()
    email['From'] = 'softwarevidhai16@gmail.com'
    email['To'] =  receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)



def assistant(query):
    if 'time' in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "wikipedia" in query :
        query = query.replace('wikipedia','')
        speak("Searching Wikipedia ...")
        results = wikipedia.summary(query,sentences=2)
        speak(results)
        speak("Done Sir, Anything Else !")

     

    elif "google" in query :
        speak("Opening google ")
        url = "https://google.com"

        webbrowser.open(url)
        speak("Opened , Anything Else Sir")
    
    elif "enable eye control" in query :
        speak("Let's go")
        subprocess.Popen(["python", "mains.py"])
        speak("Done Sir, Anything Else !")
        
    elif "enable keyboard" in query :
        speak("Let's go")
        subprocess.Popen(["python", "vkeyboard.py"])
        speak("Done Sir, Anything Else !")

    elif "disable keyboard" in query :
        speak("Let's go")
        subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
        speak("Eye control disabled. Anything else, Sir?")

 
    elif "disable eye control" in query:
        speak("Disabling eye control...")
        subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
        speak("Eye control disabled. Anything else, Sir?")
    elif "send mail"in query:
        def get_email_info():
            speak('To whom do you want to send email?')
            receiver = 'codewith01tech@gmail.com'  # You hardcoded it here, good for testing
            print(receiver)

            speak('What is the subject of your email?')
            subject = takecmd()
            if subject is None or subject == "None":
                speak("I didn't get the subject. Please say it again.")
                subject = takecmd()

            speak('Tell me the text in your email')
            message = takecmd()
            if message is None or message == "None":
                speak("I didn't get the message content. Please say it again.")
                message = takecmd()

            if message and subject:  # Only send if both are valid strings
                send_email(receiver, subject, message)
                speak('Your email has been sent.')
            else:
                speak('Failed to get email content properly. Please try again.')

            speak('Do you want to send another email?')
            send_more = takecmd()
            if send_more and 'yes' in send_more.lower():
                get_email_info()
            else:
                return 0
            


        get_email_info()


    elif "bye" in query :
        speak(f"My pleasure to help you, {MASTER}. See you later")
        return 0
        
    else:
        print("I am not able to do this !")

while True:
    query = takecmd()  # may return None
    if query is None:
        continue  # skip this iteration and listen again
    if assistant(query.lower()) == 0:
        break

