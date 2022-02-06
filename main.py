import speech_recognition as sr
from background_listener import KeywordBackgroundListener
from functools import partial

import signal


def main():
    bl = KeywordBackgroundListener()
    bl.start()

if __name__ == "__main__":
    main()
