import time

import speech_recognition as sr

class BackgroundListener():

    def __init__(self):
        self.stop_listening = None

    def _start(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)

        self.stop_listening = r.listen_in_background(m, self._callback)

        for _ in range(1000):
            time.sleep(0.1)

    def _stop(self):
        self.stop_listening(wait_for_stop=False)

    def _callback(self, recognizer, audio):
        try:
            print("Google Speech Recognition thinks you said: " + recognizer.recognize_google(audio, language='pt-BR'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
