import pyautogui
import time

'''
ESTE CODIGO SOLO FUNCIONA PARA FORMULARIOS DE GOOGLE DONDE SU ORDEN SEA OBLIGATORIAMENTE

#NOMBRE
#APELLIDO
#DNI
#RATING 1-5 
#COMENTARIOS
#ENVIAR

HAGAN TODOS LOS CAMBIOS NECESARIOS PARA QUE LES FUNCIONE A USTEDES

ES NECESARIO TENER DESCARGADA LA LIBRERIA DE PYAUTOGUI
https://pyautogui.readthedocs.io/en/latest/install.html
'''
# Entre las comillas ingrese su nombre
nombre = ""

# Entre las comillas ingrese su apellido o apellidos, separados por un espacio
apellido = ""

# Entre las comillas ingrese su DNI sin puntos ni espacios. Ej: 12345678
dni = ""

# Ingrese el link del formulario entre las comillas
url = ""

# Esta funcion le da un descanso de duracion = dur al codigo, es mas que nada para que deje cargar la pogina y no empiece a escribir antes de tiempo
def sleep (dur) :
    time.sleep(dur)

# Funcion que recorre y escribe el DNI
def escDNI () :
    for caracter in dni :
        pyautogui.press(caracter)

# Funcion que recorre y escribe el link y luego ingresa al mismo
def escURL () :
    for caracter in url :
        pyautogui.press(caracter)
    pyautogui.press('enter')

# Funcion que recorre y escribe la variable dada a cambio de valor, que son "nombre" y "apellido"
def escribir (valor) :

    # Guardamos el ultimo caracter usado, al llamarse la funcion, el ultimo caracter es "" (str vacio)
    lastCar = ""

        # Recorremos valor.  
    for caracter in valor :
        if caracter == " ":
            # En pyautogui para tocar el spacebar se usa 'space', asi que cuando detecta que el caracter es un " " usa 'space'.
            pyautogui.press('space') 

        if lastCar == " " or lastCar == "" :
            # si el ultimo caracter fue "" (str vacio) o " " (espacio), la siguiente letra sera en Mayuscula.
            pyautogui.keyDown('shift')
            pyautogui.press(caracter)
            pyautogui.keyUp('shift')

        else :
            # Si el ultimo caracter fue cualquier otro, simplemente lo escribe normal
            pyautogui.press(caracter)
        lastCar = caracter

def probar () :
    # sale de la terminal
    pyautogui.hotkey('alt', 'tab')

    # abre una pagina nueva
    pyautogui.hotkey('ctrl', 't')

    # descansa 0.2s
    sleep(0.2)

    # llama a escribir url ya que al abrir una pagina nueva hace focus a la barra de navegador
    escURL()

    # descansa 4s como para que cargue la pagina
    sleep(4)

    # aca empieza lo que pueden modificar, que en mi caso, son necesarios 3 tabs para llegar al primer input que es el de nombre
    pyautogui.press('tab', presses=3)

    
    escribir(nombre)

    pyautogui.press('tab')

    escribir(apellido)

    pyautogui.press('tab')

    escDNI()

    pyautogui.press('tab')

    #Marca como puntaje 5 
    pyautogui.press('right', presses=4)

    pyautogui.press('tab', presses=3)

    pyautogui.press('enter')

# Espera 3 segundos antes de empezar el codigo
sleep(3)

probar()