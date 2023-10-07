import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import pywhatkit
import subprocess
import pyjokes
import serial
import time


engine = pyttsx3.init()
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


ser = serial.Serial('COM6', 9600)

def turn_on_relay():
    ser.write(b'a')
    print("Turning ON the relay")
    speak('Turning on the light')

def turn_off_relay():
    ser.write(b'b')
    print("Turning OFF the relay")
    speak('Turning off the light')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)
    print('---------------------------------------------------------------------------------------------')


def date():
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
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Its high time sir, you should sleep now")
        print("Its high time sir, you should sleep now")


    speak("Jarvis at your service sir, please tell me how may I help you.")
    print("Jarvis at your service sir, please tell me how may I help you.")
    print('---------------------------------------------------------------------------------------------')


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\KISHAN\\OneDrive\\Documents\\Jarvis 2.0\\ss3.png")



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
                time()

            elif "date" in query:
                date()

            elif "who are you" in query:
                speak("I'm JARVIS created by Abhinav WITH TEAM and I'm a desktop voice assistant.")
                print("I'm JARVIS created by Abhinav WITH TEAM and I'm a desktop voice assistant.")
                print('---------------------------------------------------------------------------------------------')


            elif "how are you" in query:
                speak("I'm fine sir, What about you?")
                print("I'm fine sir, What about you?")
                print('---------------------------------------------------------------------------------------------')


            elif "fine" in query:
                speak("Glad to hear that sir!!")
                print("Glad to hear that sir!!")
                print('---------------------------------------------------------------------------------------------')


            elif "good" in query:
                speak("Glad to hear that sir!!")
                print("Glad to hear that sir!!")
                print('---------------------------------------------------------------------------------------------')


            elif "wikipedia" in query:
                try:
                    speak("Ok wait sir, I'm searching...")
                    query = query.replace("wikipedia","")
                    result = wikipedia.summary(query, sentences=2)
                    print(result)
                    speak(result)
                    print('---------------------------------------------------------------------------------------------')

                except:
                    speak("Can't find this page sir, please ask something else")
            
            elif 'open notepad' in query:
                speak("Openinig notepad")
                subprocess.Popen('C:\\Windows\\notepad.exe')
            
            elif 'open calculator' in query:
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')

            elif 'open wordpad' in query:
                subprocess.Popen('C:\\Program Files (x86)\\Windows NT\\Accessories\\wordpad.exe')
            elif "youtube" in query:
                wb.open("youtube.com") 

            elif "google" in query:
                wb.open("google.com") 
    
            elif "stack overflow" in query:
                wb.open("stackoverflow.com")

            elif 'open whatsapp' in query:
                wb.open('https://web.whatsapp.com/')

            elif "open chrome" in query:
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif "search chrome" in query:
                try:
                    speak("What should I search?")
                    print("What should I search?")
                    chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    search = takecommand()
                    wb.get(chromePath).open_new_tab(search)
                    print(search)


                except Exception as e:
                    speak("Can't open now, please try again later.")
                    print("Can't open now, please try again later.")
                
            elif 'jokes' in query:
                My_joke = pyjokes.get_joke(language="en", category="neutral")
                speak(My_joke)
            
            elif 'play' in query:
                yt = query.removeprefix('play')
                speak("Playing ")
                speak(query)
                pywhatkit.playonyt(yt)


            elif "remember that" in query:
                speak("What should I remember")
                data = takecommand()
                speak("You said me to remember that" + data)
                print("You said me to remember that " + str(data))
                print('---------------------------------------------------------------------------------------------')

                remember = open("data.txt", "w")
                remember.write(data)
                remember.close()

            elif "do you remember anything" in query:
                remember = open("data.txt", "r")
                speak("You told me to remember that" + remember.read())
                print("You told me to remember that " + str(remember))
                print('---------------------------------------------------------------------------------------------')


            elif "offline" in query:
                speak("Bye Bye Sir")
                print('---------------------------------------------------------------------------------------------')
                quit()

            elif 'quit' in query:
                speak('Bye Bye Sir')
                print('---------------------------------------------------------------------------------------------')
                quit()

            elif 'light on' in query:
                turn_on_relay()

            elif 'light off' in query:
                turn_off_relay()

            elif 'knowledge mode' in query:
                import pyttsx3
                import speech_recognition as sr
                import datetime
                import openai  # Import the OpenAI library

                # OpenAI API Key Setup
                openai.api_key = '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'  # Replace with your actual API key

                # Initialize Text-to-Speech Engine
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                engine.setProperty('voice', voice_id)
                def speak(audio):
                    engine.say(audio)
                    engine.runAndWait()


                def wishMe():
                    hour = datetime.datetime.now().hour
                    if 0 <= hour < 12:
                        speak("Good Morning!")

                    elif 12 <= hour < 18:
                        speak("Good Afternoon!")

                    else:
                        speak("Good Evening!")

                    speak("I am Miss Knowledge Sir. Please tell me how may I help you")


                def takeCommand():
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening...")
                        r.pause_threshold = 1
                        audio = r.listen(source)

                    try:
                        print("Recognizing...")
                        query = r.recognize_google(audio, language='en-in')
                        print(f"User said: {query}\n")

                    except Exception as e:
                        print(e)
                        print("Say that again please...")
                        return "None"

                    # Send the query to GPT-3 for a response
                    response = gpt3_interaction(query)
                    return response


                # Define the function to interact with GPT-3
                def gpt3_interaction(user_input, max_tokens=4000):  # Increase max_tokens as needed
                    try:
                        response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt=user_input,
                            max_tokens=max_tokens
                        )
                        return response.choices[0].text.strip()
                    except Exception as e:
                        return str(e)

                if __name__ == "__main__":
                    wishMe()
                    while True:
                        response = takeCommand().lower()
                        # Process GPT-3 response
                        print("Miss Knowledge Response:", response)
                        print('---------------------------------------------------------------------------------------------')
                        speak(response)
                        speak("And the current time is ")
                        speak(current_time) 
