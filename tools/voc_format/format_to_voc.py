import os

import string

dirName = r"D:\datasets\KITTI_VOC\JPEGImages\\"#最后要加双斜杠，不然会报错

li=os.listdir(dirName)

for filename in li:

    newname = filename

    newname = newname.split(".")

    if newname[-1]=="png":

        newname[-1]="jpg"

        newname = str.join(".",newname)#这里要用str.join

        filename = dirName+filename

        newname = dirName+newname

        os.rename(filename,newname)

        print(newname,"updated successfully")