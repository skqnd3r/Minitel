#!/bin/bash
function install(){
    # INSTALL PYTHON3
    python3 -V > /dev/null 2>&1 && a=0 || a=1
    if [ "$a" == "0" ]; then
        version=$(python3 -V | cut -d " " -f 2 | tr -d ".")
        clear
    fi

    echo $version
    if [ $a == 1 ] && [ -z $version ]; then
        sudo apt-get install python3
    elif [ -n $version ] && [ $version -lt "373" ]; then
        sudo apt-get install --only-upgrade python3
    fi

    user=$(whoami)
    clear

    sudo chmod +x minitel/functions.sh
    cp installer.sh minitel
    sudo mv minitel/ /home/

    # CHANGE PATH FROM DATA '/home/minitel/'

    filename="/home/$user/.bashrc"
    text='\nalias minitel="python3 /home/minitel/main.py"'
    sudo echo -en $text >> $filename
    . ~/.bashrc

    sudo rm -rf ../group-977098*
    cd ~
}

function uninstall(){
    user=$(whoami)
    filename="/home/$user/.bashrc"
    search='alias minitel='
    sudo sed -i "/$search/d" $filename

    sudo rm -rf /home/minitel
    . ~/.bashrc
    cd ~
}

function asroot(){
    echo -n "Please enter root password :"
    read -es Password
    clear

    echo $Password | sudo -S su root -c true 2>/dev/null && a=0 || a=1

    if [ "$a" == "1" ]; then
        echo "Wrong password."
        sudo -K
    fi
}

function endroot(){
    sudo -K
}

# ADD ERROR HANDLER
if [ -z "$1" ]; then
    if [ ! -d minitel ]; then
        echo "Minitel is already installed"
        exit
    fi
    asroot
    install
    endroot
elif [ "$1" = "-u" ]; then
    if [ -d minitel ]; then
        echo "Minitel is not installed"
        exit
    fi
    asroot
    uninstall
    endroot
else
    echo -e "unknow \"$1\" option \nplease read README.md"
fi