import os

def uninstall():
    os.system("sudo rm -rf /tLang")
    os.system("sudo rm -rf /usr/share/applications/tlang.desktop")
    os.system("rm -rf /home/$USER/.local/share/applications/tlang.desktop")

a = input("Are you sure you want to uninstall? Y/N")
if a == "N":
    print("")
if a == "Y":
    print("ok removing files")
    uninstall()

