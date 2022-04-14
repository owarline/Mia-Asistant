import requerimientos as rq
import speech_recognition as sr
import pyttsx3,pywhatkit,wikipedia,datetime,keyboard,os
from pygame import mixer
import subprocess as sub
print(rq.imprimir_titulo())
name="Mia"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
#funcion para que la maquina lea algo e voz alta
def run_chica():
    while True:
        try:
            rec = rq.listen()
        except UnboundLocalError:
            print("No te entendí, intenta de nuevo")
            continue
        if "reproduce" in rec:
            music = rec.replace("reproduce", "")
            print("Reproduciendo " + music)
            rq.talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
        elif "busca" in rec:
            search = rec.replace("busca", "")
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 5)
            print(search + ":" + wiki)
            rq.talk(wiki)
        elif "gracias" in rec:
            rq.talk("De nada, adios")
            break
if __name__ == "__main__":
    run_chica()