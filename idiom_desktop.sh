#!/bin/sh

# export DISPLAY=:0

/home/bingyu/anaconda3/envs/geo/bin/python /home/bingyu/Documents/poem_desktop/poem_desktop.py 

export DISPLAY=:0
export GSETTINGS_BACKEND=dconf

PID=$(pgrep -u bingyu gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

/usr/bin/gsettings set org.gnome.desktop.background picture-options "centered"
/usr/bin/gsettings set org.gnome.desktop.background picture-uri "file:///home/bingyu/Documents/idiom_desktop/poem.png"

