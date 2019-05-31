import pyttsx3

import speech_recognition as sr

import assistant

class JARVIS():
    engine = pyttsx3.init()

    def talk_to_me(self, audio):
        '''speaks audio passed as argument'''
        print(audio)

        for line in audio.splitlines():
            self.engine.say(line)
            self.engine.runAndWait()


    def my_command(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Ready...')
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')

        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            self.talk_to_me("Sorry, I couldn't hear that!")
            print('Your last command couldn\'t be heard')
            command = self.my_command()

        return command


if __name__ == '__main__':
    Jojo = JARVIS()
    ass = assistant.Assistant()

    Jojo.talk_to_me("Hello. What is it that you desire?")

    while True:
        try:
            ass.assistant(Jojo.my_command())
        except KeyboardInterrupt:
            Jojo.talk_to_me('Goodbye')
            sys.exit(0)