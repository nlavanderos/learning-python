import subprocess

elementosWifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
#All User Profile
elementosWifi = [i.split(":")[1][1:-1] for i in elementosWifi if "Perfil de todos los usuarios" in i]
print(elementosWifi)
for i in elementosWifi:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
        #Key Content
        results = [b.split(":")[1][1:-1] for b in results if "Contenido de la clave" in b]
        try:
            #Texto apegado a la izquierda (<) y se rellena con espacios en blancos(cantidad)
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))