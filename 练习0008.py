#第 0008 题： 一个HTML文件，找出里面的正文。
from bs4 import BeautifulSoup

f =open("D:/zhuomian/我的文件夹/学习/python/猫雷粉丝数可视化.html","r")

html_txt = f.read()

soup = BeautifulSoup(html_txt, "html.parser")

print(soup.find_all("body"))