#----* coding:utf-8 *----
import re,hashlib
import requests
import traceback  

class getlocalip:
    '''
    Get local ip(public)
    '''    
    def visit(self,url):
        opener = requests.get(url,timeout=2).content
        if opener != None:
            return opener
    
    def getip(self):
        try:
            myip = self.visit("http://180.76.179.148:5000/myip")
        except:  
            traceback.print_exc()
            try:
                myip = self.visit("http://www.lsw1994.com/api/ip")
            except:  
                traceback.print_exc()
                myip = "So sorry!!!"
        print('Get your local(public) ip: ' + myip)
        return myip
    
    def iptomd5(self):
        '''
        encode public ip with md5
        '''
        md5 = hashlib.md5()   
        md5.update(self.getip().encode("utf8"))
        return md5.hexdigest()