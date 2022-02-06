import speech_recognition as sr
from background_listener import BackgroundListener
from functools import partial

import signal


def main():
    bl = BackgroundListener()
    bl._start()

if __name__ == "__main__":
    main()
