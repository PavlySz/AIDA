import pyttsx3

import speech_recognition as sr
import sys

import re
import webbrowser
import requests

engine = pyttsx3.init()

def talkToMe(audio):
    '''speaks audio passed as argument'''
    print(audio)

    for line in audio.splitlines():
        engine.say(line)
        engine.runAndWait()


def myCommand():
    '''listens for commands'''
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe("Sorry, I couldn't hear that!")
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )

        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))

        else:
            talkToMe('Oops! I ran out of jokes')
    
    elif 'goodbye' in command:
        talkToMe('See ya later, babe.')
        sys.exit(0)

    elif 'hello' in command:
        talkToMe('Hiya')

    elif 'your name' in  command:
        talkToMe("My name is JARVIS. I'm now the new Iron Man since Tony Stark is fucking dead. RIP.")

    else:
        talkToMe('I don\'t know what you mean!')

talkToMe("Hello. What is it that you desire?")

#loop to continue executing multiple commands
while True:
    assistant(myCommand())

# TODO:
# Add translator
# Open programs
# Draw the signal
# Handle exceptions from SpeechRecognition.ipynb