#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,request,render_template
import ipencode,upload,os
from script import runscript
from werkzeug import secure_filename
from fileinput import filename

encode = ipencode.encode()
app = Flask(__name__)
dir = upload.getdir()
uploadfile = upload.upload()
cmd = runscript()

UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        if request.form['code']:
            ip = request.remote_addr
            inoname = encode.md5(ip)
            cmd.initproject(inoname)
            inodir = dir.getinodir(inoname)
            uploadfile.writecodetofile(inodir,request.form['code'])
            cmd.buildproject(inoname)
            hexdir = dir.gethexdir(inoname)
            return "Your project is building, your client plugin will automatic download \
                it when build success!</br> Click \
                <a href='hhttp://tickrobot.duapp.com/mblockly/blockly/apps/mixly/index.html'>Here</a> \
                to comeback.</br> or you can download the hex file <a href = " + hexdir + ">here</a>"
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
                ip = request.remote_addr
                inoname = encode.md5(ip)
                cmd.initproject(inoname)
                inodir = dir.getinodir1(inoname)
                f.save(os.path.join(inodir, 'sketch.ino'))
                cmd.buildproject(inoname)
                hexdir = str(dir.gethexdir(inoname))
                return "Your project is building, your client plugin will automatic download \
                it when build success!</br> Click \
                <a href='http://tickrobot.duapp.com/mblockly/blockly/apps/mixly/index.html'>Here</a> \
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
    app.run(host='0.0.0.0')

