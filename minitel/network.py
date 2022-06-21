import subprocess, curses, curses.panel, json
from useful import *

def show_network(stdscr, elem = "interfaces"):
    stdscr.clear()
    l_elem=["interfaces","routes","forwarding"]
    more = ["1:interfaces","2:routes","3:forwarding"]
    res = network()
    
    dict = res[elem]
    keys = [*dict[0]]
    row_len = lenlist(dict);
    netw = board_panel(dict, keys, row_len)
    move_center(stdscr,netw)

    print_down(stdscr,more)

    curses.panel.update_panels()
    stdscr.refresh()
    key = stdscr.getch()

    if 49 <= key <= 51:
        hidepanel(netw)
        stdscr.clear()
        show_network(stdscr,l_elem[key-49])
    else:
        stdscr.clear()
        return

def network():
    board={};
    board.update({"interfaces" : interfaces()})
    board.update({"routes" : routes()})
    board.update({"forwarding" : forward()})
    return board;


def interfaces():
    res = subprocess.check_output(['./functions.sh', 'network']).decode("ascii");
    list = [];
    loop = [["tx","rx"],["bytes","packets"]];
    info = json.loads(res);
    
    for item in info:
        obj = {}
        obj.update({'Name': item["ifname"]});
        obj.update({'Type': item["link_type"]});

        # ip
        ip = "None";
        if(item["addr_info"] != []):
            ip = item["addr_info"][0]["local"];
        obj.update({'IP': ip});

        # TRANSMIS / RECU

        # byte / packet
        for i in loop[0]:
            for i_e,e in enumerate(loop[1]):
                if(i_e == 0):
                    i_byte = item["stats64"][i][e]
                    if(i_byte != 0):
                        i_byte = size(i_byte);
                    else:
                        i_byte=str(i_byte)
                    obj.update({'Bytes': i_byte});
                else:    
                    obj.update({'Packets': str(item["stats64"][i][e])});
        list.append(obj)

    return list;

def routes():
    res = subprocess.check_output(['./functions.sh', 'route']).decode("ascii")
    info = json.loads(res);

    list = [];
    for item in info:
        obj = {};
        obj.update({'Type': item["type"]})

        if (item["dst"].isalpha()):
            obj.update({'Destination': item["gateway"]+" "+item["dst"]})
        else:
            obj.update({'Destination': item["dst"]})

        obj.update({'Dev': item["dev"]})
        obj.update({'Table': item["table"]})
        obj.update({'Protocole': item["protocol"]})
        obj.update({'Scope': item["scope"]})
        list.append(obj)
    return list;

def forward():
    res = subprocess.check_output(['./functions.sh', 'forwrd']).decode("ascii")
    if (res != 0):
        res = "FALSE"
    else:
        res = "TRUE"

    obj=[{'Forward': res}];
    return obj;

def hidepanel(list):
    for item in list:
        item.hide()
    return
        