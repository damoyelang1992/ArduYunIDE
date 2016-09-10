#!/usr/bin/python
import hashlib

class encode:
    def md5(self,str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()