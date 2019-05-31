from googletrans import Translator
import io

class MyTranslator():
    def __init__(self):
        self.translator = Translator()

    def translate(self, word, dest_language):
        ret = self.translator.translate(word, src='en', dest=dest_language)
        return ret

    def save_translation(self, word, translation):
        with io.open("Translations.txt", 'a', encoding='utf-8') as f:
            f.write('{} --{}--> {}\n'.format(word, translation.dest, translation.text))


if __name__ == '__main__':
    trans = MyTranslator()
    word = "Hello"
    dest_language = 'ar'

    translation = trans.translate(word, dest_language)
    trans.save_translation(word, translation)