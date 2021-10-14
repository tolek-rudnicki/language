import os

def inst():
    os.system("cd /")
    os.system("sudo mkdir /tLang")
    os.system("cd /tLang")
    os.system("sudo git clone https://github.com/tolek-rudnicki/language.git /tLang")
    os.system("cd /bin")
    os.system("echo \"python3 /tLang/shell.py\" >> /bin/tlang")
    os.system("chmod 755 /bin/tlang")
    os.system("echo \"[Desktop Entry]\nName=tlang\nComment = a interactive shell\nExec=/bin/tlang\nType=Application\nTerminal=true\" > /home/$USER/.local/share/applications/tlang.desktop")
    os.system("sudo mv ~/.local/share/applications/tlang.desktop /usr/share/applications/")
    os.system("echo \"[Desktop Entry]\nName=tlang\nComment = a interactive shell\nExec=/bin/tlang\nType=Application\nTerminal=true\" > /home/$USER/.local/share/applications/tlang.desktop")

    


a = input("This script is only for linux that has github installed! press Y to proceede and N to cancle")
if a == 'N':
    print("cancelling!")
else:
    if a == "Y":
        print("Ok proceeding")
        inst()
