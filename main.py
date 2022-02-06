import speech_recognition as sr
from listener import Listener, BackgroundListener
from functools import partial

import signal


def main():
    l = Listener(BackgroundListener())
    l.start()

if __name__ == "__main__":
    main()
