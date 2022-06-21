import subprocess, curses, time, curses.panel
from useful import *

sort = ""

def show_process(stdscr,sort = "pid"):
    stdscr.clear()
    dict = process(sort)
    keys = [*dict[0]]
    row_len = lenlist(dict);
    proc = board_panel(dict, keys, row_len)
    more = ["1:sort"]
    move_center(stdscr,proc)
    print_down(stdscr,more)
    curses.panel.update_panels()
    stdscr.refresh()
    key = stdscr.getch()

    if key == 49:
        stdscr.clear()
        l_sort=["pid","comm","stat","%cpu","%mem","ppid"]
        invert=0
        key = 55
        while key == 55:
            stdscr.clear()
            if invert == 0:
                print_center(stdscr, "1:pid  2:nom  3:stat  4:%cpu  5:%mem  6:ppid  7:invert")
            else:
                print_center(stdscr, "1:pid  2:nom  3:stat  4:%cpu  5:%mem  6:ppid  7:normalize")
            key = stdscr.getch()
            if key == 55:
                if invert == 0:
                    invert = 1
                else:
                    invert = 0
        if 49 <= key <= 54:
            if invert == 0:
                show_process(stdscr,l_sort[key-49]) 
            else:
                show_process(stdscr,"-"+l_sort[key-49]) 
        else:
            return
    # add run
    else:
        return

def process(sort):
    str = subprocess.check_output(['./functions.sh', 'proc', sort]).decode("ascii")
    Process = []

    # clean infos
    str = str.split("\n")
    for item in str:
        if item == '':
            str.remove(item)
        else:
            item = item.split(" ")
            tmp = []
            for i in item:
                if len(i) != 0:
                    tmp.append(i)
            item = tmp

            # parsing infos
            # if real_proc(item[1]):
                # transform into key value
            obj = {}
            obj.update({'PID': item[0]})
            obj.update({'NAME': item[1]})
            obj.update({'STATUS': item[2]})
            obj.update({'%CPU': item[3]})
            obj.update({'%MEM': item[4]})
            obj.update({'PPID': item[5]})
            Process.append(obj)
    return Process

# # verif dictionnaire
# def real_proc(name):
#     out = {'ps', 'functions.sh', 'tail'}
#     for o in out:
#         if name == o:
#             return False
#     return True