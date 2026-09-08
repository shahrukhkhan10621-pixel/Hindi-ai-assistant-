import os
import tempfile
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
import pyttsx3

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit(
        "OPENAI_API_KEY nahi mila. .env file mein apni API key daalo."
    )

client = OpenAI(api_key=API_KEY)
recognizer = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty("rate", 175)

SYSTEM = """You are a helpful Hindi-English voice assistant.
Reply naturally and concisely. The user may speak Hindi, Hinglish, or English.
Do not use markdown unless it is genuinely useful for a spoken answer."""

history = []

def speak(text):
    print("AI:", text)
    speaker.say(text)
    speaker.runAndWait()

def ask_ai(text):
    history.append({"role": "user", "content": text})
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=SYSTEM,
        input=history,
        store=False,
    )
    answer = response.output_text.strip()
    history.append({"role": "assistant", "content": answer})
    return answer

def listen():
    with sr.Microphone() as source:
        print("\n🎙️ Sun raha hoon...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("⏱️ Koi awaaz nahi mili.")
            return None

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        print("Tum:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Samajh nahi aaya.")
    except sr.RequestError as e:
        print("❌ Speech service error:", e)
    return None

def main():
    speak("Namaste! Main ready hoon. Boliye.")
    while True:
        text = listen()
        if not text:
            continue

        if text.lower().strip() in {"exit", "quit", "stop", "band ho jao", "बंद हो जाओ"}:
            speak("Theek hai, milte hain.")
            break

        try:
            answer = ask_ai(text)
            speak(answer)
        except Exception as e:
            print("AI error:", e)
            speak("Sorry, AI se connect nahi ho paaya. API key aur internet check karo.")

if __name__ == "__main__":
    main()
