# This code will not create any destination directory of 'year'.
# Create MPO directory inside destination only if it doesn't exist already.
# This will copy only the additional date-month-year directories inside the MPO directories.
# This is the FINAL requirement for us !!!

#! /usr/bin/python

import os

source="/opt/image/"
destination="/opt/image_new/"
year="2017"

mpolist = os.listdir(source)

# List of MPO who have image of xxxx year #
for mpo in mpolist:
    dtime = os.listdir(source + mpo)
    destmpo = os.listdir(destination)
    list_year = [s for s in dtime if year in s]
    # MPO who do not have image of xxxx year #
    if list_year == []:
        continue
    # Make directory of MPO at destination #
    if mpo not in destmpo:
        os.system('mkdir ' + destination + mpo)
        print('Creating directory for MPO ' + mpo)
    # Copy directory of images of those MPO at destination #
    if list_year != []:
        for j in list_year:
            os.system('cp -fr ' + source + mpo + '/' + j + ' ' + destination + mpo + '/')
            print('Copying ' + j + ' for MPO ' + mpo)
