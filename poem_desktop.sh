#!/bin/sh

PID=$(pgrep -u $LOGNAME gnome-session)
echo $PID >> /home/bingyu/Desktop/output.txt

export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

/home/bingyu/anaconda3/envs/geo/bin/python /home/bingyu/Documents/poem_desktop/poem_desktop.py 

gsettings set org.gnome.desktop.background picture-options "centered"
gsettings set org.gnome.desktop.background picture-uri "file:///home/bingyu/Documents/poem_desktop/poem.png"
