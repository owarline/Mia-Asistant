import speech_recognition as sr
import pyttsx3,pywhatkit,wikipedia,datetime,keyboard,os
from pygame import mixer
import subprocess as sub
#titulo de la asistente
def imprimir_titulo():
    print("""
      __  __ ___    _         _    ____ ____ ___ _____  _    _   _ _____ 
     |  \/  |_ _|  / \       / \  / ___/ ___|_ _|_   _|/ \  | \ | |_   _|
     | |\/| || |  / _ \     / _ \ \___ \___ \| |  | | / _ \ |  \| | | |  
     | |  | || | / ___ \   / ___ \ ___) |__) | |  | |/ ___ \| |\  | | |  
     |_|  |_|___/_/   \_\ /_/   \_\____/____/___| |_/_/   \_\_| \_| |_|  
    """)
#cambio de nombre de el habla de la maquina
name="Mia"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
#funcion para que la maquina lea algo e voz alta
def talk(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("No te entendí, intenta de nuevo")
        if name in rec:
            rec = rec.replace(name, "")
        else:
            return rec
    return rec
def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)