import json,tarfile,time,subprocess

from process import process
from info_general import info
from network import network
from useful import print_center

def exportdata(stdscr):
    stdscr.clear()
    print_center(stdscr, "Processing...")
    stdscr.refresh()

    l_file = [["info.json",info()],["network.json",network()],["process.json",process('pid')]]

    
    # .json
    for item in l_file:
        with open(item[0],'w') as f:
            json.dump(item[1], f, indent=2)

    # ISO
    utc = time.strftime("%z")
    date = time.strftime("%Y-%m-%dT%X")+utc[:3]+":"+utc[3:]
    
    # tar
    filename=(f"{date}.minitel.tar.gz")
    file_obj=tarfile.open(filename, "w:gz")
    for item in l_file:
        file_obj.add(item[0])
    file_obj.close()

    # clean
    commands = ["mv *.tar.gz ../"]
    for item in l_file:
        commands.append("rm ./"+ item[0])
    for command in commands:
        subprocess.run(command, shell=True)
    
    time.sleep(1.5)
    stdscr.clear()
    print_center(stdscr, "Done")
    stdscr.refresh()
    time.sleep(1)
    return