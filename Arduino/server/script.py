#!/usr/bin/python
import subprocess,time
from upload import getdir
#from Tix import Shell

class runscript:
    def process(self,cmd,param1,waitFlag):
        dir = getdir()
        p = subprocess.Popen([cmd, param1], bufsize=10000, stdout=subprocess.PIPE,cwd=dir.get_abspsth())
#        out,err = process.communicate()
        if waitFlag :
            while 1: 
                ret = subprocess.Popen.poll(p)
                if ret == 0: 
                    break 
                elif ret is None: 
                    time.sleep(0.1) 
                else: 
                    break 
#	else:
#		out,err = p.communicate()
            
#        if p.stdout:
#            p.stdout.close()
#        if p.stderr:
#            p.stderr.close()
    
    def initproject(self,param1):
        self.process("./static/script/init.sh", param1, waitFlag = True)
        
    def buildproject(self,param1):
        self.process("./static/script/build.sh", param1, waitFlag = True)
        
    def clearproject(self,param1):
        self.process("./static/script/clear.sh", param1, waitFlag = True)
