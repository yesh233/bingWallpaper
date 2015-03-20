#!/bin/bash

PID=$(pgrep gnome-session)
#eval PID=($PID)

#export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/${PID[1]}/environ|cut -d= -f2-)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)


gsettings set org.gnome.desktop.background picture-uri "$1"