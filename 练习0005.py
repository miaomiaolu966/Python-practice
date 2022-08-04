import os

from PIL import Image

dirs = os.listdir("D:/zhuomian/我的文件夹/图片/DOAX-VenusVacation01")

def change_ima(image):

    file = "D:/zhuomian/我的文件夹/图片/DOAX-VenusVacation01"+"/"+str(image)

    im =Image.open(file)

    im.thumbnail((1136, 640))
    
    im.save(file,'JPEG')

for i in range(0,len(dirs)):

    change_ima(dirs[i])
