#----* coding:utf-8 *----
import requests
# import StringIO
import urllib 

class file(object):
    def download_file1(self,url):
        print (url)
        local_filename = url.split('/')[-1]
        if local_filename == "firmware.hex":
            r = requests.get(url, stream=True)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        f.close()

    def download_file2(self,url):
#         print ("downloading with urllib")
        urllib.urlretrieve(url, "firmware.hex")
        
#     def download_file3(self,url):
#         try:
#             req = requests.get(url,timeout=20)
#             file_name ='firmware.hex'
#             file = req.content
#             f= StringIO.StringIO(file)
#             f= open(file_name,'wb')
#             f.write(file)
#             f.close()
#             print(req.status_code)
#         except Exception as error:
#             #traceback.print_exc()
#             print(str(error))