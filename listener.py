from __future__ import annotations

import time

from abc import ABC, abstractmethod

import speech_recognition as sr


class Listener:

    def __init__(self, state: ListenerState) -> None:
        self._state = ListenerState
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.transition_to(state)

    def transition_to(self, state: ListenerState):
        print(f"Listener: Transition to {type(state).__name__}")
        #self._state.stop()
        self._state = state
        self._state.context = self
        self._state.start(self.mic, self.recognizer)

    #def start(self) -> None:
    #    self._state.start(self.mic, self.recognizer)

    #def stop(self) -> None:
    #    self._state.stop()


class ListenerState(ABC):

    @property
    def context(self) -> Listener:
        return self._context

    @context.setter
    def context(self, context: Listener) -> None:
        self._context = context

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class GenericListener(ListenerState):

    def start(self, mic, recognizer):
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)

            print("Qual o seu desejo?")
            audio = recognizer.listen(source)

            try:
                speech_text = microfone.recognize_google(audio, language='pt-BR')
                print("Você disse: " + speech_text)
            except sr.UnkownValueError:
                print("Foi mal! Eu não entendi o que você disse!")

    def stop(self):
        self.context.transition_to(BackgroundListener())


class BackgroundListener(ListenerState):

    def __init__(self):
        self.stop_listening = None

    def start(self, mic, recognizer):
        with mic as source:
            recognizer.adjust_for_ambient_noise(mic)

        self.stop_listening = recognizer.listen_in_background(mic, self.callback)

        for _ in range(10000):
            time.sleep(0.1)

    def stop(self):
        r = self.stop_listening(wait_for_stop=True)
        print("Background Listener parou: ", r)

    def callback(self, recognizer, audio):
        try:
            #speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=self.keywords, language='pt-BR')
            speech_text = recognizer.recognize_google(audio, language='pt-BR')

            print("Reconheci: ", speech_text)

            if "maria" in speech_text.lower():
                print("Achou a palavra chave.")
                #self.stop()
                self.context.transition_to(GenericListener())

        except sr.UnknownValueError:
            print("Desculpe! Não entendi nada.")
