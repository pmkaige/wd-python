#!/usr/bin/python
# -*- coding: utf-8 -*-
#闻到 http://wendao123.cn
#抓取https://bing.ioliu.cn/的历史必应壁纸


import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers  = {
    'User-Agent': ua.random
}
url = 'https://bing.ioliu.cn/?p={page}'
for page in range(1,59):
    urls = url.format(page=page)
    response = requests.get(urls,headers=headers)
    # print(response.text)
    res = BeautifulSoup(response.text,'lxml')
    img_url = res.find_all("img")
    print('>>>>>>'+urls)
    # print(img_url)
    for h in img_url:
        img_src = h.get('src')
        # str1 = '1920x1080.jpg'
        # img_final_url = img_src[:-11]
        # true_img_url = img_final_url+str1
        res = requests.get(img_src,headers=headers)
        with open(img_src[25:],'wb') as f:
            f.write(res.content)
        print('正在抓取'+img_src)