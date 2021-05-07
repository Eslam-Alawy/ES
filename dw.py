import os 
def o():
 
 lin = input("URL CRUNCHYROLL Subtitle Downloader\n")
 os.system('youtube-dl --skip-download --all-subs --sub-format "ass"  "{0}"'.format(lin))
 
 
o()
y = input("again? y or n\n")
if y == "y":
 o()
 else:
 os.system('exit')
 