#! /usr/bin/python

import os

source="/opt/image/"
destination="/opt/image_new/"
year="032017"

mpolist = os.listdir(source)

### Copy image of MPO who have image of xxxx year ###
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    list_year = [s for s in dtime if year in s]
    #print(list_year)
    if list_year != []:
        print(mpo)
        #print(list_year)
