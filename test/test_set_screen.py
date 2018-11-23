import subprocess

def set_screen():
    cmd = "printf"
    param = " '\e[8;10;100t' "
    subprocess.call([cmd, param])
    print()

def set_screen_poz():
    cmd = "printf '\e[2t' && sleep 3 && printf '\e[1t'"
    #param = '\e[2t' && sleep 3 && printf '\e[1t'
    subprocess.call([cmd])
    print()

if __name__ == "__main__":
    set_screen()
    set_screen_poz()