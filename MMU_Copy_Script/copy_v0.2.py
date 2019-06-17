# This code will create separate destination directory of 'year' and create MPO directory inside it.

import os

source="/opt/image/"
destination="/opt/image_new/"
year="2017"

mpolist = os.listdir(source)

# List of MPO who have image of xxxx year #
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    list_year = [s for s in dtime if year in s]
    # MPO who do not have image of xxxx year #
    if list_year == []:
        continue
    # Make directory of those MPO at destination #
    if list_year != []:
        os.system('mkdir ' + destination + year + '/' + mpo)
        print('Creating directory for MPO ' + mpo)
    # Copy directory of images of those MPO at destination #
    if list_year != []:
        for j in list_year:
            os.system('cp -fr ' + source + mpo + '/' + j + ' ' + destination + year + '/' + mpo + '/')
            print('Copying ' + j + ' for MPO ' + mpo)


