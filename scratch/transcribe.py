import sys
sys.path.append('/Users/wisdom/Library/Python/3.9/lib/python/site-packages')
import speech_recognition as sr

def transcribe():
    r = sr.Recognizer()
    audio_file = "scratch/audio.wav"
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        # Use Google Speech Recognition (free web API, requires internet)
        text = r.recognize_google(audio, language="ko-KR")
        print("TRANSCRIPT_SUCCESS")
        print(text)
    except Exception as e:
        print("TRANSCRIPT_FAILED")
        print(str(e))

if __name__ == "__main__":
    transcribe()
