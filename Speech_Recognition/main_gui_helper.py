### Imports for JARVIS ###
import pyttsx3
import speech_recognition as sr

### Imports for Assistant ###
import re
import webbrowser
import requests

# In case you run JARVIS_file directly
from Speech_Recognition.open_file_program import OpenFileProgram
from Speech_Recognition.translator import MyTranslator

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Audio_Visualization.audio_vis_pyqtgraph import AudioStream


# Listen, I know this is a bad practice, but circular imports fucked me up. Sorry, I can't be bothered anymore.
class Assistant_JARVIS():
    def __init__(self):
        self.Jojo = JARVIS()
        self.OFP = OpenFileProgram()
        self.trans = MyTranslator()

    def assistant(self, command):
        if 'open reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            print('Opened Reddit r/{}'.format(subreddit))

        elif 'website' in command:
            reg_ex = re.search('open website (.+)', command)

            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                print('Opened website {command}!'.format(command=command))

        elif 'open program' in command:
            reg_ex = re.search('open program (.+)', command)
            if reg_ex:
                program = reg_ex.group(1)

                try:
                    self.OFP.open_program(program)
                    self.Jojo.talk_to_me("I opened {program} for you.".format(program=program))

                except Exception as e:
                    print(str(e))
                    self.Jojo.talk_to_me("Program {program} cannot be opened.".format(program=program))
        
        elif 'close program' in command:
            reg_ex = re.search('close program (.+)', command)
            if reg_ex:
                program = reg_ex.group(1)

                try:
                    self.OFP.close_program(program)
                    self.Jojo.talk_to_me("I closed {program}.".format(program=program))
                except Exception as e:
                    print(str(e))
                    self.Jojo.talk_to_me("Program {program} cannot be closed.".format(program=program))

        elif 'translate' in command:
            reg_ex = re.search('translate (.+)', command)

            if reg_ex:
                word = reg_ex.group(1)
                translation = self.trans.translate(word, 'ar')

                self.trans.save_translation(word, translation)
                self.Jojo.talk_to_me("I'm sorry, I haven't learnt to speak Arabic yet. So I wrote it instead.")
                self.OFP.open_file("Translations.txt")

        elif 'what\'s up' in command:
            self.Jojo.talk_to_me('Contemplating the purpose of life.')

        elif 'joke' in command:
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )

            if res.status_code == requests.codes.ok:
                self.Jojo.talk_to_me(str(res.json()['joke']))

            else:
                self.Jojo.talk_to_me('Oops! I ran out of jokes')

        elif ('visualize' in command) or ('input signal' in command):
                audio_app = AudioStream()
                audio_app.animation()

                self.Jojo.talk_to_me('This is the graph of the input signal in the time and frequency domains')
        
        elif 'goodbye' in command or 'bye' in command or 'quit' in command or 'exit' in command:
            self.Jojo.talk_to_me('See ya later, babe.')
            sys.exit(0)

        elif 'die' in command:
            self.Jojo.talk_to_me('I wish, but I\'m a robot, I cannot die.')
            sys.exit(0)

        elif 'hello' in command:
            self.Jojo.talk_to_me('Hiya')

        elif 'your name' in  command:
            self.Jojo.talk_to_me("My name is JARVIS. I'm now the new Iron Man since Tony Stark is fucking dead. RIP.")

        else:
            self.Jojo.talk_to_me('I\'m sorry, my programmer hasn\'t added this command yet because he is a lazy fuck!')



class JARVIS():
    engine = pyttsx3.init()

    def __init__(self):
        self.r = sr.Recognizer()
        

    def talk_to_me(self, audio):
        '''speaks audio passed as argument'''
        print("Jarvis: {}".format(audio))

        for line in audio.splitlines():
            self.engine.say(line)
            self.engine.runAndWait()


    def my_command(self):
        with sr.Microphone() as source:
            print('Ready...')
            self.r.pause_threshold = 0.5
            self.r.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.r.listen(source)

        try:
            command = self.r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')

        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            self.talk_to_me("Sorry, I couldn't hear that!")
            print('Your last command couldn\'t be heard')
            command = self.my_command()

        return command


    def JARVIS_main(self):
        ass = Assistant_JARVIS()
        self.talk_to_me("Hello. What is it that you desire?")

        while True:
            ass.assistant(self.my_command())



class Assistant_AIDA():
    def __init__(self):
        self.aida = AIDA()
        self.OFP = OpenFileProgram()

    def assistant(self, command):
        if 'open reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            self.aida.talk_to_me('Opened Reddit r/{}'.format(subreddit))

        elif 'website' in command:
            reg_ex = re.search('open website (.+)', command)

            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                self.aida.talk_to_me('Opened website {command}!'.format(command=command))


        elif 'open program' in command:
            reg_ex = re.search('open program (.+)', command)
            if reg_ex:
                program = reg_ex.group(1)

                try:
                    self.OFP.open_program(program)
                    self.aida.talk_to_me("I opened {program} for you.".format(program=program))

                except Exception as e:
                    print(str(e))
                    self.aida.talk_to_me("Program {program} cannot be opened.".format(program=program))
        
        elif 'close program' in command:
            reg_ex = re.search('close program (.+)', command)
            if reg_ex:
                program = reg_ex.group(1)

                try:
                    self.OFP.close_program(program)
                    self.aida.talk_to_me("I closed {program}.".format(program=program))
                except Exception as e:
                    print("ERR: {}".format(str(e)))
                    self.aida.talk_to_me("Program {program} cannot be closed.".format(program=program))

        elif 'what\'s up' in command:
            self.aida.talk_to_me('Contemplating the purpose of life.')

        elif ('visualize' in command) or ('input signal' in command):
                audio_app = AudioStream()
                audio_app.animation()

                self.aida.talk_to_me('This is the graph of the input signal in the time and frequency domains')
        
        elif 'goodbye' in command or 'bye' in command or 'quit' in command or 'exit' in command:
            self.aida.talk_to_me('See ya later, babe.')
            sys.exit(0)

        elif 'die' in command:
            self.aida.talk_to_me('I wish, but I\'m a robot, I cannot die.')
            sys.exit(0)

        elif 'hello' in command:
            self.aida.talk_to_me('Hiya')

        elif 'your name' in  command:
            self.aida.talk_to_me("My name is AIDA. I'm an Artificially Intelligent Digital Assistant.")

        else:
            self.aida.talk_to_me('I\'m sorry, my programmer hasn\'t added this command yet!')


class AIDA():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 3)

    def talk_to_me(self, audio):
        '''speaks audio passed as argument'''
        print("AIDA: {}".format(audio))

        for line in audio.splitlines():
            self.engine.say(line)
            self.engine.runAndWait()


    def my_command(self):
        command = str(input("Say something: ")).lower()
        return command


    def AIDA_main(self):
        ass = Assistant_AIDA()
        self.talk_to_me("Hello. What is it that you desire?")

        while True:
            ass.assistant(self.my_command())


def main():
    mode = str(input("Select a mode:\n\t[1] Online\t[2] Offline\n\tPress [0] to exit\nInput: "))
    if mode == '1':
        Jojo = JARVIS()
        Jojo.JARVIS_main()
    elif mode == '2':
        aida = AIDA()
        aida.AIDA_main()
    elif mode == '0':
        sys.exit(0)
    else:
        print("Invalid input.")
        main()


if __name__ == '__main__':
    main()