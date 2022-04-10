#paquete que permite que la maquina hable
import pyttsx3
#titulo de la asistente
print("""
  __  __ ___    _         _    ____ ____ ___ _____  _    _   _ _____ 
 |  \/  |_ _|  / \       / \  / ___/ ___|_ _|_   _|/ \  | \ | |_   _|
 | |\/| || |  / _ \     / _ \ \___ \___ \| |  | | / _ \ |  \| | | |  
 | |  | || | / ___ \   / ___ \ ___) |__) | |  | |/ ___ \| |\  | | |  
 |_|  |_|___/_/   \_\ /_/   \_\____/____/___| |_/_/   \_\_| \_| |_|  
                                                                     
""")
#cambio de nombre de el habla de la maquina
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
#funcion para que la maquina lea algo e voz alta
def talk(text):
    engine.say(text)
    engine.runAndWait()
#opciones
print("""
1. prueba de voz
2. informacion del proyecto
""")
#variable que determina opciones
a=int(input("ingrese una opcion: "))
if a==1:
    print("prueba de voz")
    talk("prueba de voz")
elif a==2:
    talk('''Mia-Asistant un asistente virtual, proyecto escolar, primero medio, Chile.

Nuestra empresa: Nombre: inserte nombre Servicios: Nuestra empresa presta servicios de programacion general, de marketing y de diseño de interfaces. Direccion de la empresa: Alacena debajo de la Escalera, Privet Drive 4, Little Whinging, Surrey, Inglaterra Trabajadores: Consuelo "username" Leiva, Hugo "username" Solís, Gabriel "owarline" Parra.

Seccion de Marketing: Director (a) de la seccion: Consuelo "username" Leiva. Conocimientos: inserte conocimientos. Cargo dentro de la empresa: Directora de marketing, Directora creativa, Cara principal de la empresa, encargada del diseño de presentaciones.

Seccion Creativa: Director (a) de la seccion: Consuelo "username" Leiva. Conocimientos: inserte conocimientos. Cargo dentro de la empresa: Directora de marketing, Directora creativa, Cara principal de la empresa, encargada del diseño de presentaciones.

Seccion de la Visual: Director (a) de la seccion: Hugo "username" Solís. Conocimientos: inserte conocimientos. Cargo dentro de la empresa: Director de imagen empresarial, "Padre" de Mia.

Seccion de Programacion: Director (a) de la seccion: Gabriel "owarline" Parra. Conocimientos: Cuatro años de estudio autodidacta de lenguaje Batch, Dos años de estudio autodidacta de lenguaje Python, Certificado de la Pontifice Universidad Catolica de Chile; Python Basics. Cargo dentro de la empresa: Programador en jefe, encargado del repositorio.''')
else:
    talk("opcion desconocida")
    print("opcion desconocida")
print("gracias por usar")
#se cierra el programa