import os
os.system('echo transfer 37 mkv to mp4')
i = 0
while i < 37:
 os.system('ffmpeg -i {0}.mkv -codec copy {0}.mp4'.format(i))
 os.system('rm -f {0}.mkv'.format(i))
 i+=1
os.system('echo END')
