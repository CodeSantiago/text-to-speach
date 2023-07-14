import pyttsx3

read = open(r'example.txt')

read_text = read.readlines()

engine = pyttsx3.init()

for i in read_text:
    engine.say(i)
    engine.runAndWait()