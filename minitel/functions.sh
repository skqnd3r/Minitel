#!/bin/bash

# PROCESS
function proc(){
     ps -o pid,comm,stat,%cpu,%mem,ppid --sort=$1\
    | tail -n +2
}

#simple
function safekill(){
    kill -9 $(pgrep $1)
}

#forcé
function hardkill(){
    pkill -9 $1
}

function run_proc(){
    $1 &
}




# RESEAUX
function network(){
    ip -j -s addr show
}

function route(){
    ip -j -d route show table all
}

function forwrd(){
    cat /proc/sys/net/ipv4/ip_forward
}

"$@"