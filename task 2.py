import speech_recognition as sr


def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        print("🎧 Listening from file...")
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
            print("\n📝 Transcribed Text:\n", text)
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print("❌ Could not request results; check internet connection:", e)


if __name__ == "__main__":
    path = input("Enter path to your audio file (WAV format): ")
    speech_to_text(path)
