from tkinter import *
import gtts
import pyaudio
import speech_recognition as sr
r = sr.Recognizer()
t = 0

root = Tk()

root.title("speech recognition")
root.geometry("500x500")

####FUNCTIONS
def record():
    global t
    if t == 0:
        buttonvar.set("Stop Recording")
        t = 1
        print("Recording...")
        actionvar.set("Recording...")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            actionvar2.set("listening...")
            print("listening...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said: {}".format(text))
                actionvar3.set("You said: {}".format(text))
                tts = gtts.gTTS(text)
                tts.save("output.mp3")
            except:
                print("Sorry, I did not get that")
                actionvar3.set("Sorry, I did not get that")
                actionvar2.set("")
    else:
        t = 0
        buttonvar.set("Record")
        print("Stopped recording")
        actionvar.set("Stopped recording")
        actionvar2.set("")
        actionvar3.set("")

####BUTTONS
buttonvar = StringVar()
buttonvar.set("Lmao")
touch = Button(root, textvariable = buttonvar, command=record).pack()
actionvar = StringVar()
actionvar.set("")
actionvar2 = StringVar()
actionvar.set("")
actionvar3 = StringVar()
actionvar.set("")
action = Label(root, textvariable=actionvar).pack()
action2 = Label(root, textvariable=actionvar2).pack()
action3 = Label(root, textvariable=actionvar3).pack()
root.mainloop()