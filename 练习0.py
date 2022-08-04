from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("simsun.ttc",48) #设置字体

im01 = Image.open("D:/zhuomian/我的文件夹/图片/爱哥/1655696348163.jpg") #打开图片，设置图片的路径

draw = ImageDraw.Draw(im01)

draw.text((0,6),u"用Python给图片添加文字",fill=(255,0,0),font = font)   #文字坐标，文本内容，填充字体颜色，设置字体格式

im01.show()