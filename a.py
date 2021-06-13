from array import *
import os
import sys
sys.path.append(os.path.abspath("/usr/local/lib/python2.7/dist-packages"))
from mega import Mega
mega = Mega()
m = mega.login('discinema_2@getnada.com','Lord7418529630')
def clear():
    os.system('reset')
urlar = []
vidnamear = []
vidsub = []
vidnameoutar = []
def men():
    f = open("links.txt","r")
    file = f.read()
    f.close()
    line1 = file.split("\n")
    args = []
    for x in line1:
        args.append(x)
    
    length = len(args)
    con_ter = 0
    index_of_it = 0
    f_s = input("Links Starts from :\n")
    while con_ter < length:
        if args[con_ter] == f_s:
            in_co = con_ter +1
            f_s_int = int(f_s)+ 1
            f_s_nxt = str(f_s_int)
            while in_co < length:
                if args[in_co] == f_s_nxt:
                    break
                else:
                    urlar.append(args[in_co])
                in_co+=1
        con_ter+=1

kam = input("How Many Videos You Will Finish Today :\n")
howmany = int(kam)
#howmany = 2
start_from = input("Your start from :\n")
in_start = int(start_from)
end_of = in_start + howmany -1
i = 0

while i < howmany:
    url = input("Of VID {0}: Crunchyorll URL:\n".format(i+1))
    urlar.append(url)
    
    if in_start <= end_of:
        vidnamear.append(str(in_start)+".mp4")
        vidsub.append(str(in_start)+".ass")
        vidnameoutar.append("[DisCinema.com]_AOT_EP"+str(in_start)+".mp4")
    
    clear()
    in_start+=1
    i+=1
    

    

def doitnow():
    k = 0
    while k < howmany:
     os.system('youtube-dl -f best --console-title --newline --no-warnings --no-part -o "{1}" --user-agent "Mozilla / 5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko / 20100101 Firefox / 65.0" -v --newline {0}'.format(urlar[k],vidnamear[k]))
     os.system('ffmpeg -i {0} -i logo.png  -filter_complex "overlay=5:5:format=auto,format=yuv420p,ass={1}" {2}'.format(vidnamear[k],vidsub[k],vidnameoutar[k]))
     #os.system('touch {0}.py'.format(vidnameoutar[k]))
     #os.system('printf "import sys\nimport os\nsys.path.append(os.path.abspath(\'/usr/local/lib/python2.7/dist-packages\'))\nfrom mega import Mega\nmega = Mega()\nm = mega.login(\'discinema_1@getnada.com\',\'Lord7418529630\')\nfile = m.upload(\'{0}\')\nos.system(\'rm {0}.py && rm {0} && rm {1} && rm {2}\')" > {0}.py'.format(vidnameoutar[k],vidsub[k],vidnamear[k]))
     #os.system('xfce4-terminal -x sh -c "python3 {0}.py; bash"'.format(vidnameoutar[k]))
     k+=1


def uploadit():
    k=0
    while k < howmany:
     os.system('echo -e "\e[5m\e[95mUploading {0} ..."'.format(vidnameoutar[k]))
     #os.system('python3 {0}.py'.format(vidnameoutar[k]))
     file = m.upload('{0}'.format(vidnameoutar[k]))
     os.system('echo -e "\e[92m{0} Uploaded Successfully."'.format(vidnameoutar[k]))
     os.system('rm -f {0} && rm -f {1} && rm -f {2}'.format(vidnameoutar[k],vidsub[k],vidnamear[k]))
     k+=1 
    
    
doitnow()
uploadit()
