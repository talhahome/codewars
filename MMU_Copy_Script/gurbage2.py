#! /usr/bin/python

import os

source="/opt/image/"
destination="/opt/image_new/"
year="2017"

mpolist = os.listdir(source)
count = 0

### Copy image of MPO who have image of xxxx year ###
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    for i in dtime:
        #destmpo = os.listdir(destination + year)
        if year in i:
            count += 1
            #if mpo in destmpo:
                #os.system('cp -fr ' + source + mpo + '/' + i + ' ' + destination + year + '/' + mpo + '/')
                #print('Copying ... ' + i)
                #continue
            #elif mpo not in destmpo:
                #os.system('mkdir ' + destination + year + '/' + mpo)
                #os.system('cp -fr ' + source + mpo + '/' + i + ' ' + destination + year + '/' + mpo + '/')
                #print('Create Dir & Copying ... ' + i)
        #else:
            #continue

print("Total: " + str(count))
