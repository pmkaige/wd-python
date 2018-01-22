#!/usr/bin/python
# -*- coding: utf-8 -*-
#author:闻到 http://wendao123.cn
#抓取斗图啦http://www.doutula.com的表情包，并按文件夹存储


import requests
from bs4 import BeautifulSoup
import os,re
# import hashlib
url = 'http://www.doutula.com/article/list/?page={page}'

for page in range(1,544):
    urls = url.format(page=page)
    response = requests.get(url=urls)
    print('正在抓取》》》',urls)
    doc = BeautifulSoup(response.text,'lxml')
    list_group_item = doc.find_all('a',class_='list-group-item random_list')
    for group_item in list_group_item:
        title = group_item.find(class_='random_title').text
        img_urls = group_item.find_all(class_='lazy image_dtb img-responsive')
        for img_url in img_urls:
            alt = img_url.get('alt')
            #去除非法字符
            # alt = re.sub('[\/:*?"<>|、.]','-',alt)
            # alt = hashlib.md5(bytes(alt, encoding='utf-8'))
            true_img_url = img_url.get('data-backup')[:-4]
            hz = true_img_url[-4:]
            # print(alt,true_img_url,hz)
            img_response = requests.get(true_img_url)
            try:
                path = './斗图/'+title
                # print(path)
                # 去除首位空格
                path = path.strip()
                # 去除尾部 \ 符号
                path = path.rstrip("\\")
                # 判断路径是否存在
                isExists = os.path.exists(path)
                # 判断结果
                if not isExists:
                    # 如果不存在则创建目录
                    # 创建目录操作函数
                    os.makedirs(path)
                    print('>>正在创建目录',title)
            except:
                pass
            try:
                with open(path+'/'+alt+hz,'wb') as f:
                    f.write(img_response.content)
            except:
                pass
            print('正在抓取',true_img_url)