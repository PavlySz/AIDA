import re
import webbrowser
import requests
import sys

from JARVIS import JARVIS
from open_file_program import OpenFileProgram
from translator import MyTranslator

# to import a class from a file in another package
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Audio_Visualization.audio_vis_pyqtgraph import AudioStream

class Assistant():
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
            print('Done!')

        elif 'open website' in command:
            reg_ex = re.search('open website (.+)', command)

            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                print('Opened website {command}!'.format(command=command))
            else:
                pass

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

                self.Jojo.talk_to_me('This is the graph of the input signal in the time and frequency domains')

                audio_app.animation()

                reg_ex = re.search('(.+)', command)

                if reg_ex:
                    word = reg_ex.group(1)
                    if 'close' in word:
                        self.Jojo.talk_to_me('You said close graph')
                        audio_app.close_graph()
        
        elif 'goodbye' in command:
            self.Jojo.talk_to_me('See ya later, babe.')
            sys.exit(0)

        elif 'hello' in command:
            self.Jojo.talk_to_me('Hiya')

        elif 'your name' in  command:
            self.Jojo.talk_to_me("My name is JARVIS. I'm now the new Iron Man since Tony Stark is fucking dead. RIP.")

        else:
            self.Jojo.talk_to_me('I\'m sorry, my programmer hasn\'t added this command yet because he is a lazy fuck!')