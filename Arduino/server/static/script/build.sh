#!/bin/bash

cd ./static/$1

ino build
if [ 0 -eq $? ] 
then
hexfiledir="180.76.179.148:5000/static/$1/.build/uno/firmware.hex"
mosquitto_pub -h 180.76.179.148 -t $1 -m $hexfiledir 
else 
mosquitto_pub -h 180.76.179.148 -t $1 -m ‘Build failed,Looks like your code has a problem.’
fi

exit 0
