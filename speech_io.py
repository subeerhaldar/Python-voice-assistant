import io
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please speak...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return ""

def speak(text):
    try:
        tts = gTTS(text=text, lang="en")
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio = AudioSegment.from_file(mp3_fp, format="mp3")
        play(audio)
    except Exception as e:
        print(f"Speech synthesis error: {e}")