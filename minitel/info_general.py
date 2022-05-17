from re import M
import shutil , subprocess
from useful import *

def show_info(stdscr):
    stdscr.clear()
    menu_general_info = info()

    height, weight = stdscr.getmaxyx()
    for idx, row in enumerate(menu_general_info):
        x = weight//2 - len(row)//2
        y = height//2 - len(menu_general_info)//2 + idx
        stdscr.addstr(y,x,row)
    stdscr.refresh()

def info():
    #all commande and info stock in vlr
    a = subprocess.check_output(['hostnamectl | grep "Operating"'], shell=True).decode("ascii")
    b = subprocess.check_output(['cat /etc/os-release | grep "VERSION="'], shell=True).decode("ascii")
    c = subprocess.check_output(['hostnamectl | grep "Kernel"'], shell=True).decode("ascii")
    d = subprocess.check_output(['uname -r'], shell=True).decode("ascii")
    e = subprocess.check_output(['ulimit -n'], shell=True).decode("ascii")
    f = subprocess.check_output(['uptime -s'], shell=True).decode("ascii")
    g = subprocess.check_output(['lscpu | grep "Model name"'], shell=True).decode("ascii")
    h = subprocess.check_output(['cat /proc/meminfo | grep "MemTotal"'], shell=True).decode("ascii")
    i = subprocess.check_output(['cat /proc/meminfo | grep "MemFree"'], shell=True).decode("ascii")
    j = subprocess.check_output(['cat /proc/meminfo | grep "MemAvailable"'], shell=True).decode("ascii")
    disque = shutil.disk_usage('/')
    disque_total = size(disque[0])
    disque_used = size(disque[1])
    disque_free = size(disque[2])

    #vlr in dict for be len
    menu_general_info = [a,b,c,d,e,f,g,h,i,j,disque_total,disque_used,disque_free]
    return menu_general_info;