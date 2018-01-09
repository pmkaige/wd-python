# -*- coding: utf-8 -*-
#闻到 http://wendao123.cn
#利用python生成字符画
from PIL import Image

codeLib = '''@B%8&WM#*oahkbdpqwmasdfghjklzzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"'''#生成字符画所需的字符集
count = len(codeLib)

def transform(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数"L"表示黑白模式
    codePic = ''
    for h in range(0,image_file.size[1]):  #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]#建立灰度与字符集的映射
        codePic = codePic+'\r\n'
    return codePic

fp = open('zfh.jpg','rb')
image_file = Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.25), int(image_file.size[1]*0.125)))#调整图片大小
print(u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)

tmp = open('tmp.txt','w')
tmp.write(transform(image_file))
tmp.close()