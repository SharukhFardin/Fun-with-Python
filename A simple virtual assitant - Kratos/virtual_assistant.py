# allows python to talk to us
import pyttsx3
# Recognizes voice and transforms it o voice
import speech_recognition as sr
# allow us to open websites
import pywhatkit
# A library with large amount of jokes
import pyjokes

# Other imports
import datetime
import webbrowser
import wikipedia

# Voice options
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id5 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'


# Head microphone and return audio as text
def transform_audio_into_text():
    # store recognizer in variable
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can speak")

        # Save what you hear as audio
        audio = r.listen(source)

        try:
            # search on Google
            request = r.recognize_google(audio, language="en-US")

            # test in text
            print("You said " + request)

            # return request
            return request

        # In case it doesn't understand audio
        except sr.UnknownValueError:
            print("Ups! I didn't understand the voice.")

            return "Try again. I am waiting."

        # In case the request cannot be resolved
        except sr.RequestError:
            print("Service Unavailable")
            return "Try again."

        # Unexpected Error
        except:
            print("Ups! something went wrong.")
            return "Try again."


# Function so the God of War can be heard
def speak(message):

    # start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id5)

    # deliver message
    engine.say(message)
    engine.runAndWait()


# Inform day of the week
def ask_day():

    # Create a variable with today information
    day = datetime.date.today()
    # print(day)

    # Create variable for day of the week
    week_day = day.weekday()
    # print(week_day)

    # Names of days
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # Say the day of the week
    speak(f'Today is {calendar[week_day]}')


# Inform what time it is
def ask_time():

    # Variable with time information
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours and {time.minute} minutes'

    print(time)

    # Say the time
    speak(time)


# Create initial greeting
def initial_greeting():

    # Say greeting
    speak('Hello I am Kratos, the god of war. How can I help you today?')


# Main function of the assistant
def my_assistant():

    # Activate the initial greeting
    initial_greeting()

    # Cut-off variable
    go_on = True

    # Main loop
    while go_on:

        # Activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('Sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            speak('Of course, I am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue
        elif 'what is the time' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak('I am looking for it')
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=2)
            speak('according to wikipedia: ')
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak('of course, right now')
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('this is what i found')
            continue
        elif 'play' in my_request:
            speak('oh, what a great idea! I´ll play it right now')
            pywhatkit.playonyt(my_request)
            continue
        elif 'jokes' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'goodbye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break

        # Many more functionalities can be added


# Calling my assistant who is a GOD. The ghost of sparta. Killer of ODIN, ZEUS. KRATOS.
my_assistant()

