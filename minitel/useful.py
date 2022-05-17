import curses, curses.panel

def size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "Erreur"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2f G" % (G)
        else:
            return "%.2f M" % (M)
    else:
        return "%.2f kb" % (kb)



def lenlist(dict):
    i=0;
    board=[]

    while i != len(dict[0]):

        max_len = None
        for item in dict:

            v_item = list(item.values())
            k_item = list(item.keys())

            if (max_len == None):
                max_len = len(k_item[i])+6
            
            if max_len < len(v_item[i])+4:
                max_len = len(v_item[i])+4
            
            
        if (max_len % 2) != 0:
            max_len += 1
        
        if (len(k_item[i]) % 2 != 0):
            max_len +=1

        board.append(max_len)
        i+=1
    return board;



def panel_case(height ,length, y, x, strin,format):
    win = curses.newwin(height, length, y, x)
    
    step = 0
    l_str = len(strin)

    if format == 1:
        step = round((length-l_str)/2)
        win.box()
        win.addstr(1, step, strin)
    else:
        step = length-len(strin)-2
        win.addstr(0, step, strin)
    panel = curses.panel.new_panel(win)
    return panel

def board_panel(dict, keys, row_len):
    board = []
    stage = row_len[0]*-1

    i = 0
    while i!=len(keys):
        if i == 0:
            stage += row_len[i]
        else:
            stage += row_len[i-1]

        pan = panel_case(3, row_len[i],0 , stage ,keys[i],1)
        board.append(pan)
        i+=1

    j = 0
    for item in dict:
        i = 0
        values = list(item.values())
        stage = row_len[0]*-1

        while i!=len(item):
            if i == 0:
                stage += row_len[i]
            else:
                stage += row_len[i-1]

            pan = panel_case(2, row_len[i],3+j, stage ,values[i],0)
            board.append(pan)
            i+=1
        j+=1    
    return board



def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)

def print_down(stdscr, list):
    h, w = stdscr.getmaxyx()
    l_len=0
    for item in list:
        l_len += len(item)
    step = (w-(l_len+len(list)))//2
    text=""
    for i, item in enumerate(list):
        if i != 0:
            text+="  "+item
        else:
            text+=item
    stdscr.addstr(h-2, step, text)



def move_center(stdscr,obj):
    h, w = stdscr.getmaxyx()
    y_a,x_a=obj[0].window().getbegyx()
    y_b,x_b=obj[len(obj)-1].window().getbegyx()

    mv_y = h//2 - (y_b - y_a + 1)//2
    mv_x = w//2 - (x_b - x_a + 1)//2
    move_panel(obj,mv_y,mv_x)


def move_panel(obj, mv_y, mv_x):
    i=0
    while i != len(obj):
        y,x=obj[i].window().getbegyx()
        obj[i].move(mv_y+y,mv_x+x)
        i+=1