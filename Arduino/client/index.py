#----* coding:utf-8 *----
from getip import getlocalip
import paho.mqtt.client as mqtt
from download import file
import subprocess,os,sys
import listserial
# from PyQt5.QtWidgets import *

downloader = file()
client = mqtt.Client()

def get_topic():
    ipc = getlocalip()
    md5ip = ipc.iptomd5()
#     print md5ip
    return md5ip

def get_abspsth():
    ABSPATH=os.path.abspath(sys.argv[0])
    ABSPATH=os.path.dirname(ABSPATH)
#     print ABSPATH
    return ABSPATH

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    topic = get_topic()
    print("Connected server with result code "+str(rc))
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Build success!")
    message = str(msg.payload)
    print("You can download Hex file from :http://",message)
    if -1 != message.find('firmware.hex') :
        if os.path.exists('firmware.hex'):
            os.remove('firmware.hex')
        downloader.download_file2('http://' + str(msg.payload))
        serialport = listserial.serial_ports()
        print('find serialport ' + str(serialport))
        '''There detect all serial port then return a list, i take a wrong way to choose the first serialport
        TODO　design a ui to choose serialport then recoerd it in configure file'''
        if len(serialport):
            command = 'avrdude -c arduino -p m328p -P ' + serialport[0] + ' -b 115200 -U flash:w:"firmware.hex":a'
            p1 = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True,cwd=get_abspsth())
            output, error = p1.communicate()
            print (output,error)
        else:
            print("没有发现串口设备，请检查您的Arduino是否正确插入，或者驱动是否正确安装!")
            print("Please check your Arduino serial port!")

client.on_connect = on_connect
client.on_message = on_message
try:
    client.connect("180.76.179.148", 1883, 60)
except:
    print("连接网络失败，请检查您的网络连接！")
    print("Connect Filed, Please check your network!")
client.loop_forever()