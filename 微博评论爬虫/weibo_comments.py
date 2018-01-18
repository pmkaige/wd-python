#!/usr/bin/python
# -*- coding: utf-8 -*-
#@author: 闻到
#@blog : http://wendao123.cn
#description : 抓取微博移动端评论

import requests
from fake_useragent import UserAgent
import re
import time
import json
import csv
import random

def get_comments(id,pages,write):
    url = 'https://m.weibo.cn/api/comments/show?id={id}&page={page}'.format(id='4197457778578674',page='1')
    # ua = UserAgent()
    headers = {
        # 'User-Agent': 'ua.random'
    'authority': 'm.weibo.cn',
    'method': 'GET',
    'path': '/ api / comments / show?id = 4197457778578674 & page = {page}'.format(page='1'),
    'scheme': 'https',
    'accept': 'application / json, text / plain, * / *',
    'accept - encoding': 'gzip, deflate, br',
    'accept - language': 'zh - CN, zh;',
    'cookie': '_T_WM = f73a00a07c7d352051b32c4177ec3ee1;ALF = 1518858449;SCF = AtqqNd7i8OZP - _fCWPPofbXgPc1jr1F1MUwYAhZp73A1BpnId45yz3jvi2l_zqmhUW_ou_IAiBPLMAK988HKSeM.;SUB = _2A253ZBOCDeRhGeNL7VQR8CvNyzSIHXVUpr3KrDV6PUJbktBeLRj7kW1NSOYfAAmdKNim_FKSjjQE77gURwu_H7b5;SUBP = 0033WrSXqPxfM725Ws9jqgMF55529P9D9W5JYiEGprZ0IT5zwpjSUHwN5JpX5K - hUgL.Fo - fSoq7eh - pehn2dJLoIpqLxKBLBonLBoBLxKqLB.2LB - 8bdsvr;SUHB = 05iKydoyI6AoyE;SSOLoginState = 1516266450;H5_INDEX_TITLE = % E4 % B8 % B4 % E6 % BA % AAblog;H5_INDEX = 2;M_WEIBOCN_PARAMS = featurecode % 3D20000320 % 26lfid % 3D10320310 % 26luicode % 3D20000174 % 26fid % 3D102803 % 26uicode % 3D10000011',
    'referer': 'https: // m.weibo.cn / status / 4197457778578674',
    'user - agent': 'Mozilla / 5.0(Windows NT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.132Safari / 537.36',
    'x - requested -with':'XMLHttpRequest'
    }
    try:
        for page in range(1,pages):
            url = url.format(id=id,page=page)
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                res = json.loads(response.text)
                # print(res['data']['data'])
                if res['data']['data']:
                    for detail in res['data']['data']:
                        # print(detail)
                        id = detail['user']['id']
                        screen_name = detail['user']['screen_name']
                        source = detail['source']
                        text = detail['text']
                        #点赞数
                        like_counts = detail['like_counts']
                        w_doc = (id,screen_name,source,text,like_counts)
                        writer.writerow(w_doc)
                        print(w_doc)
            else:
                break
    except:
        print('抓取完毕！')
        # break
        # st = random.randint(1,5)
        # timesleep = time.sleep(st)
        # print('休眠'+str(st))



if __name__ == '__main__':
    time_start = time.time()
    print('开始抓取，当前时间'+time.strftime('%Y-%m-%d',time.localtime(time_start)))
    with open('3315.csv','a+',encoding='utf-8',newline='') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(('id','screen_name','source','text','like_counts'))
        get_comments(id='4197457778578674',pages=1000,write=writer)
    time_end = time.time()
    print('抓取完成，当前时间' + time.strftime('%Y-%m-%d',time.localtime(time_end)))
    times = time_end - time_start
    print('此次采集共花费'+str(times)+'s')