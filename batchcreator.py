import getpass, os
# USER_NAME = getpass.getuser()
filepath = r"Put file path here"

def add_to_startup(file_path=filepath):
    if file_path == filepath:
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\maste\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    with open(bat_path + '\\' + "avastart.bat", "w+") as bat_file:
        bat_file.write(r'start "" '+filepath)
add_to_startup()

