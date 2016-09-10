#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
class getdir:
    '''
    get file dir or current absdir
    '''
    def getinodir(self,inoname):
        inofiledir = self.get_abspsth() + "/static/" + inoname + "/src/sketch.ino"
        return inofiledir
        
    def getinodir1(self,inoname):
        inofiledir = self.get_abspsth() + "/static/" + inoname + "/src"
        return inofiledir
    
    def get_abspsth(self):
        ABSPATH=os.path.abspath(sys.argv[0])
        ABSPATH=os.path.dirname(ABSPATH)
        return ABSPATH
    
    def gethexdir(self,inoname):
        hexfiledir = "/static/" + inoname + "/.build/uno/firmware.hex"
	return hexfiledir

class upload:
    '''
    restore upload code to file or upload file ti static
    if the file end with .ino put int in inoproject/src/ then rename it sketch.ino
    '''
    def writecodetofile(self,inodir,data):
        with open(inodir,"wb") as f:
            f.write(data)
            
    def checkfilename(self,filename):
        ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'ino'])
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
