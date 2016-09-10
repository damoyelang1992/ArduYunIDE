#!/bin/bash

#this is a script to creat a ino directory and init it
#then flask will trans in the program
#Finally ino will build it and flask will redirect to firmware.hex to download it

rm -rf ./static/$1
 
mkdir ./static/$1

cd ./static/$1

ino init
#ino build
