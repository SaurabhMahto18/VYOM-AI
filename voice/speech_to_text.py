import speech_recognition as sr


recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:

        print("\n🎤 VYOM is listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        audio = recognizer.listen(source)

    try:
        print("🧠 Processing your voice...")

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        print("VYOM: I couldn't understand that.")
        return ""

    except sr.RequestError as error:
        print("VYOM: Speech recognition service is unavailable.")
        print("Error:", error)
        return ""