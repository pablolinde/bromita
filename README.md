El programa esta pensado meramente para adquirir conocimiento sobre el funcionamiento del sistema operativo windows, 
en ningun momento se planea hacer un uso malintencionado del mismo ni el "virus" está diseñado para hacer daño a ningun usuario.

Quienes lo descargen serán responsables de lo que hagan con el.

El código en bromita.py crea una carpeta oculta en el directorio usuario donde instalará UpdaterService.exe, el ejecutable que ha de crearse
a partir del .py con el mismo nombre. Este otro código es la broma en sí misma, cada tres segundos mostrará una imagen por pantalla acompañada de un audio.
UpdaterService.exe se ejecutará únicamente tras cada inicio de sesión.
El programa se detendrá al crear un txt llamado byefrog en el directorio usuario. 
Para eliminarlo definitivamente hay que acceder al programador de tareas y borrar la tarea programada llamada UpdaterService, 
también buscar la carpeta oculta en el directorio usuario llamada ansel y eliminarla.

Para convertir los .py a ejecutables se recomienda seguir los siguientes pasos:
- Abrir un terminal e instalar el compilador nuikta si no se tiene ya descargado.
- Dirigirse al directorio donde se hayan los .py, la foto y el audio.
- Ejecuta: nuitka --standalone --onefile --windows-disable-console UpdaterService.py
- Ejecuta: nuitka --standalone --onefile --windows-uac-admin --windows-disable-console bromita.py --include-data-file=UpdaterService.exe=UpdaterService.exe --include-data-file=frog.jpg=frog.jpg --include-data-file=frog.mp3=frog.mp3
