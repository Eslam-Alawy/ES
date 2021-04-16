import os
import sys
sys.path.append(os.path.abspath("/usr/local/lib/python2.7/dist-packages"))
from mega import Mega
mega = Mega()
m = mega.login('discinema_1@getnada.com','Lord7418529630') 
os.system('reset')  
kam = input("How Many will be uploaded :\n")
howmany = int(kam)
urlar = []
i = 0
while i < howmany:
    url = input("Of File {0} enter the name of it .txt :\n".format(i+1))
    urlar.append(url)
    i+=1

q = 0
j = len(urlar)

while q < j:
    os.system('echo "Uploading {0} -------"'.format(urlar[q]))
    file = m.upload('{0}'.format(urlar[q]))
    os.system('echo "{0} Uploaded Successfully ........"'.format(urlar[q]))
    q+=1