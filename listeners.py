import time

from abc import ABC, abstractmethod

import speech_recognition as sr


class Listener(ABC):

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class GenericListener(Listener):

    def __init__(self):
        pass

    def start(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)

            print("Qual o seu desejo?")
            audio = microfone.listen(source)

            try:
                speech_text = microfone.recognize_google(audio, language='pt-BR')
                print("Você disse: " + speech_text)
            except sr.UnkownValueError:
                print("Foi mal! Eu não entendi o que você disse!")

    def stop(self):
        pass

class KeywordBackgroundListener(Listener):

    def __init__(self):
        self.stop_listening = None
        self.keywords = [("maria", 1), ("ei maria", 1), ]

    def start(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)

        self.stop_listening = r.listen_in_background(m, self.callback)

        for _ in range(10000):
            time.sleep(0.1)

    def stop(self):
        self.stop_listening(wait_for_stop=False)

    def callback(self, recognizer, audio):
        try:
            #speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=self.keywords, language='pt-BR')
            speech_text = recognizer.recognize_google(audio, language='pt-BR')

            print("Reconheci: ", speech_text)

            if "maria" in speech_text.lower():
                print("Achou a palavra chave.")

        except sr.UnknownValueError:
            print("Desculpe! Não entendi nada.")
