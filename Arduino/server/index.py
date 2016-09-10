#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,request,render_template
#import paho.mqtt.client as mqtt
import ipencode,upload,os
from script import runscript
from werkzeug import secure_filename
from fileinput import filename

encode = ipencode.encode()
app = Flask(__name__)
dir = upload.getdir()
uploadfile = upload.upload()
cmd = runscript()
#client = mqtt.Client()

UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#def on_connect(client, userdata, flags, rc):
#    client.subscribe("ino-blockly")

#def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))

#client.on_connect = on_connect
#client.on_message = on_message

@app.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        if request.form['code']:
#            client.connect("180.76.179.148", 1883, 60)
            ip = request.remote_addr
            inoname = encode.md5(ip)
            cmd.initproject(inoname)
            inodir = dir.getinodir(inoname)
            uploadfile.writecodetofile(inodir,request.form['code'])
            cmd.buildproject(inoname)
            hexdir = dir.gethexdir(inoname)
#            client.publish(inoname, '180.76.179.148:5000/static/' + inoname + '/.build/uno/firmware.hex')
#            client.disconnect()
            return "build success downloading form your client plugin!</br> Click <a href='http://ide.hiveduino.com/blockly/apps/mixly/index.html'>Here</a> to comeback.</br> or you can download the hex file <a href = " + hexdir + ">here</a>"
    else:
        return "Please <b>POST</b> data to this address!"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        f = request.files['file']
        if f and uploadfile.checkfilename(f.filename):
            filename = secure_filename(f.filename)
            if filename.rsplit('.', 1)[1] == 'ino':
#                client.connect("180.76.179.148", 1883, 60)
                ip = request.remote_addr
                inoname = encode.md5(ip)
                cmd.initproject(inoname)
                inodir = dir.getinodir1(inoname)
                f.save(os.path.join(inodir, 'sketch.ino'))
                cmd.buildproject(inoname)
                hexdir = str(dir.gethexdir(inoname))
#                client.publish(inoname, '180.76.179.148:5000/static/' + inoname + '/.build/uno/firmware.hex')
#                client.disconnect()
                return "build success downloading form your client plugin!</br> Click \
                <a href='http://ide.hiveduino.com/blockly/apps/mixly/index.html'>Here</a> \
                to comeback.</br> or you can download the hex file <a href = " + hexdir + ">here</a>"
            else:
                f.save(os.path.join(UPLOAD_FOLDER, filename))
                return 'upload File ' + filename + ' success!'
        else:
            return "Filename Forbidden! You are uploading a danger file!"

@app.route('/myip')
def get_client_ip():
    ip = request.remote_addr
    return ip

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

