import os

source="D:/image_new/"
destination="/opt/image_new/"
year = "2017"

mpolist = os.listdir(source)

### Find list of MPO who have image of xxxx year ###
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    for i in dtime:
        if year in i:
            print(mpo)

### Find size of MPO directory who have image of xxxx year ###
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    for i in dtime:
        if year in i:
            print(os.system('du -sh ' + source + mpo))
        break

### Copy image of MPO who have image of xxxx year ###
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
#for mpo in mpolist:
#    dtime = os.listdir(source + mpo)
#    for i in dtime:
#        destmpo = os.listdir(destination + year)
#        if [year in i] and [mpo in destmpo]:
#            #os.system('cp -fr ' + source + mpo + '/' + i + ' ' + destination + year + '/' + mpo + '/')
#            print('copyng ... ' + i)
#        elif [year in i] and [mpo not in destmpo]:
#            os.system('mkdir ' + destination + year + '/' + mpo)
#            #os.system('cp -fr ' + source + mpo + '/' + i + ' ' + destination + year + '/' + mpo + '/')
#            print('copyng ... ' + i)
#        else:
#            continue
    for i in dtime:
        destmpo = os.listdir(destination + year)
        if year in i:
            if mpo in destmpo:
                os.system('cp -fr ' + source + mpo + '/' + i + ' ' + destination + year + '/' + mpo + '/')
                print('Copying ... ' + i)
            elif mpo not in destmpo:
                os.system('mkdir ' + destination + year + '/' + mpo)
                os.system('cp -fr ' + source + mpo + '/' + i + ' ' + destination + year + '/' + mpo + '/')
                print('Copying ... ' + i)
        else:
            continue
