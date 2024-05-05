import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import pyautogui
import pywhatkit
import subprocess
import pyjokes


engine = pyttsx3.init()
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

engine.setProperty('voice', voice_id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def current_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)
    print('---------------------------------------------------------------------------------------------')


def current_date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
    print('---------------------------------------------------------------------------------------------')


def wishme():
    print("Welcome back mam!!")
    speak("Welcome back mam!!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning mam!!")
        print("Good Morning mam!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon mam!!")
        print("Good Afternoon mam!!")
    elif 16 <= hour < 24:
        speak("Good Evening mam!!")
        print("Good Evening mam!!")
    else:
        speak("Its high time mam, you should sleep now")
        print("Its high time mam, you should sleep now")

    speak("Jarvis at your service mam, please tell me how may I help you.")
    print("Jarvis at your service mam, please tell me how may I help you.")
    print('---------------------------------------------------------------------------------------------')


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\abhin\\Downloads\\ss.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        print('---------------------------------------------------------------------------------------------')

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            current_time()

        elif "date" in query:
            current_date()

        elif "who are you" in query:
            speak("I'm Alexa created by Payomanti Ghosh WITH TEAM and I'm a desktop voice assistant.")
            print("I'm Alexa created by Payomanti Ghosh WITH TEAM and I'm a desktop voice assistant.")
            print('---------------------------------------------------------------------------------------------')

        elif "how are you" in query:
            speak("I'm fine mam, What about you?")
            print("I'm fine mam, What about you?")
            print('---------------------------------------------------------------------------------------------')

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot Successfull")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that mam!!")
            print("Glad to hear that mam!!")
            print('---------------------------------------------------------------------------------------------')

        elif "wikipedia" in query:
            try:
                speak("Ok wait mam, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
                print('---------------------------------------------------------------------------------------------')

            except Exception as e:
                print(e)
                speak("Can't find this page mam, please ask something else")

        elif 'open notepad' in query:
            speak("Opening notepad")
            subprocess.Popen('C:\\Windows\\notepad.exe')

        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'open wordpad' in query:
            subprocess.Popen('C:\\Program Files (x86)\\Windows NT\\Accessories\\wordpad.exe')

        elif "youtube" in query:
            wb.open("https://www.youtube.com")

        elif "google" in query:
            wb.open("https://www.google.com")

        elif 'open whatsapp' in query:
            wb.open('https://web.whatsapp.com/')

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            subprocess.Popen(chromePath)

        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)
            print(My_joke)

        elif 'play' in query:
            yt = query[5:]
            speak("Playing ")
            speak(yt)
            pywhatkit.playonyt(yt)

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            print('---------------------------------------------------------------------------------------------')

            remember = open("data.txt", "a")
            remember.write(data + '\n')
            remember.close()

        elif "do you remember" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))
            print('---------------------------------------------------------------------------------------------')

        elif "offline" in query or 'quit' in query:
            speak("Bye Bye mam")
            print('---------------------------------------------------------------------------------------------')
            quit()
