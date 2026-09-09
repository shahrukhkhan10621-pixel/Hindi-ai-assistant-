HINDI-ENGLISH AI VOICE Jarvis 
================================

Aapka original Python assistant installable Android project ke base mein convert kiya gaya hai.

IMPORTANT:
- Original script desktop Python ke liye tha (speech_recognition + pyttsx3).
- Android par native voice input ke liye Android Speech Recognizer use kiya gaya hai.
- OpenAI API key APK ke andar hard-code NA karein.
- Build karne ke liye Linux/WSL + Buildozer/Android SDK ki zarurat hoti hai.

BUILD (Linux/WSL):
1. Python 3 install karein.
2. Buildozer install karein.
3. Is folder mein:
      buildozer android debug
4. Build hone ke baad bin/ folder mein APK milega.
5. APK phone mein bhej kar install karein.

API KEY:
Build/run environment mein OPENAI_API_KEY set karein.
Example:
      export OPENAI_API_KEY="YOUR_KEY"

NOTE:
Agar aap public app banana chahte hain, API key ko APK mein rakhna unsafe hai.
Production app ke liye ek small backend/proxy banana better hai.

MODEL:
Original uploaded code mein model "gpt-5.6-luna" diya gaya tha; project mein wahi model name rakha gaya hai.
Agar aapke API account mein ye model available nahi hai, build ke baad API call par model error aa sakta hai.
