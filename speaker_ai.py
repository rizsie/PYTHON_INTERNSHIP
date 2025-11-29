import pyttsx3

engine = pyttsx3.init()
for i in range(10):
    engine.say(" hey rizsie....." \
    "how are you doing ")
    engine.runAndWait()