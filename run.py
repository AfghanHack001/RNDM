import os, sys, platform
try:
    import requests
except:
	os.system("xdg-open https://github.com/AfghanHack001")
	
        ###os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf RNDM.py')
except:
    pass
os.system('rm -rf MISTYY.so ')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MISTYY.so'):
        os.system('curl -L https://github.com/blackteam100200/RNDM/blob/main/RNDM.py?raw=true -o RNDM.py') 
        import RNDM
    else:
        import RNDM
