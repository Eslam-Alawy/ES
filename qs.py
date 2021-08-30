import os
def clear():
    os.system('reset')
clear()
kam = input("How Many Videos You Will Finish Today :\n")
howmany = int(kam)
str = howmany + ".mp4"
str2 = howmany + "_.mp4"
os.system('ffmpeg -i {0} -ss 5 -vcodec copy -acodec copy {1}'.format(str,str2))
os.system('rm -f {0}'.format(str))
os.system('mv {0} {1}'.format(str2,str))
os.system('python3 qs.py')