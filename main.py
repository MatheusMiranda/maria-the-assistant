import speech_recognition as sr

def main():

    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Say something to me: ")

        audio = microfone.listen(source)

        try:
            frase = microfone.recognize_google(audio,language='pt-BR')

            print("You said: " + frase)

        except sr.UnkownValueError:
            print("Im sorry! I didn't understood what you said!")

    return frase

if __name__ == "__main__":
    main()
