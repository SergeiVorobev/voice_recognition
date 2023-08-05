import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio = recognizer.listen(source, timeout=5)

            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            if text.lower() == "stop":
                print("Stopping the program.")
                break

        except sr.WaitTimeoutError:
            print("Listening timed out. Say something or say 'stop' to exit.")

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")

        except sr.RequestError as e:
            print("Could not request results; check your network connection:", str(e))

if __name__ == "__main__":
    main()