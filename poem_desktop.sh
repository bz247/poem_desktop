#!/usr/bin/env bash

# PID=$(pgrep -u $LOGNAME gnome-session)
# echo $PID >> /home/bingyu/Desktop/output.txt

# export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

/Users/bingyu/anaconda3/envs/cities/bin/python /Users/bingyu/poem_desktop/poem_desktop.py 

osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/bingyu/poem_desktop/poem.png"';
killall Dock;
