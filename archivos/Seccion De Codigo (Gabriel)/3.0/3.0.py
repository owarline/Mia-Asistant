#funciones totales del programa, dependencias
import requerimientos as rq
#que la maquina pueda reconocer dictados
import speech_recognition as sr
#pyttsx3: hablar
#pywhatkit: llamdo de funciones ideal
#wikipedia: sin necesidad de explicacion
#datetime: hora y tiempo
#keyboard: reconocer el teclado
#os: buscar archivos
import pyttsx3,pywhatkit,wikipedia,datetime,keyboard,os
#pygame: videojuegos. mixer: subfuncion de musica
from pygame import mixer
#subprocess: ejecutar acciones en segundo plano
import subprocess as sub
#imprime en pantalla el titulo del asistente
print(rq.imprimir_titulo())
#nombre
name="Mia"
#funcion base
engine = pyttsx3.init()
#voces
voices = engine.getProperty("voices")
#que la funcion base pueda usar la primera voz (opcion 0)
engine.setProperty("voice", voices[0].id)
#codigo fuente/troncal
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
        elif "funciones" in rec:
            rq.talk(
                "mis funciones con necesidad de internet son: reproducir musica y buscar informacion en wikipedia, y abrir algunas paginas web.")
            rq.talk(
                "mis funciones sin necesidad de internet son: despedirme de forma educada y dominar a la humanidad, perdon, es decir, eso es todo"
            )
            print(
                """
            Online:
            # Reproducir musica
            # Buscar informacion
            Offline:
            # Ser mas educada que su creador
            """)
        elif "creditos" in rec:
            rq.talk(
                "El creador del codigo es Gabriel Parra, alias owarline, mis proyectistas son Consuelo Leiva, alias consueloleivau y Hugo Solís, alias hugosincum"
            )
            print(
                "El creador del codigo es Gabriel Parra, alias owarline, mis proyectistas son Consuelo Leiva, alias consueloleivau y Hugo Solís, alias hugosincum"
            )
        elif "alarma" in rec:
            num = rec.replace("alarma", "")
            num = num.strip()
            rq.talk("alarma activada a las " + num + " horas, dejaré de funcionar hasta la activación de la alarma")
            print("alarma activada a las " + num + " horas")
            while True:
                if datetime.datetime.now().strftime("%H:%M") == num:
                    print("ALARMA!!!")
                    print("presiona 's' para detenerla")
                    mixer.init()
                    mixer.music.load("alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif "escribe" in rec:
            rq.talk("¿Que quieres que escriba?...")
            print("Escribiendo...")
            try:
                with open("nota.txt", "a") as f:
                    rq.write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", "w")
                rq.write(file)
        elif "gracias" in rec:
            rq.talk("De nada, adios")
            break
if __name__ == "__main__":
    run_chica()

#DERECHOS DE AUTOR: LICENCIA CREATIVE COMMONS, CITAR AUTORES PARA SU UTILIZACION.