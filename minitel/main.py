import curses, curses.panel, time
from useful import *
from export import exportdata
from info_general import show_info
from process import show_process
from network import show_network
from data import Global

# print_menu constament appeler ??
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(Global.menu):
        x = w//2 - len(row)//2
        y = h//2 - len(Global.menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def main(stdscr):
    # Minitel titles
    stdscr.addstr(0, 0, "Welcome to the best minitel ever !")

    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for current row
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    # specify the current selected row
    current_row = 0

    # print the menu

    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        # Keyboard control with the arrow pad
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        if key == curses.KEY_DOWN and current_row < len(Global.menu)-1:
            current_row += 1
        
        # Home menu with a function for each category
        if current_row == 0 and key in [10, 13]:
            show_info(stdscr)
            stdscr.getch()

        if current_row == 1 and key in [10, 13]:
            show_network(stdscr)
            stdscr.refresh()

        if current_row == 2 and key in [10, 13]:
            show_process(stdscr)
            stdscr.refresh()
            # stdscr.getch()

        if current_row == 3 and key in [10, 13]:
            exportdata(stdscr)
            stdscr.refresh()
            stdscr.getch()

        print_menu(stdscr, current_row)

            # if user selected last row, exit the program
        if current_row == len(Global.menu)-1 and key in [10, 13]:
            break

curses.wrapper(main)