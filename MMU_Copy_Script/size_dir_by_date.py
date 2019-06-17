#! /usr/bin/python

import os
import subprocess

source="/opt/image/"
#source="/opt/image_new/"

mpolist = os.listdir(source)

### Find size of MPO directory who have image of xxxx year ###

for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    for i in dtime:
        if '2017' in i:
            print(os.system('du -sh ' + source + mpo))
        break
