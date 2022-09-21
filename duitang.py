# 甘大帅 #
# 开发时间 2021/8/20 21:35
# -*- coding: utf-8 -*-
import os

import requests
import urllib.parse
import jsonpath
import json



# 判断是否存在文件夹
# def mkdir(path):
#     path=path.strip
#     #去除首位空格
#     path=path.rstrip(r"\\")
#     #去除尾部\符号
#     is_exist=os.path.exists(path)
#     if not is_exist:
#         os.makedirs(path)
#         print("创建成功")
#         return True
#     else:
#         print('目录已存在')
#         return False
# mkpath="D:\\图片\\堆糖图片\\"
# mkdir(mkpath)
print('好家伙')
url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start={}'
label = input("请输入想爬取的图片类型")
path=r"D:\图片\\"+label
if os.path.exists(path)==False:
    os.makedirs(path)
    print(path+"创建成功")
else:
    print(path+"该文件夹已经创建")
    pass

label = urllib.parse.quote(label)
print(label)
x=int(input("请输入开始页码"))
y=int(input("请输入结束页码"))


num = 0
label = urllib.parse.unquote(label)
for index in range(x, y, 24):
    print(index)
    u = url.format(label,index)
    print(u)
    we_data = requests.get(u).text  # 请求网站并访问网页源代码的文本形式
    html = json.loads(we_data)
    # 把json格式解码转换成python对象
    photo = jsonpath.jsonpath(html, "$..path")
    print(photo)


    for i in photo:
        a = requests.get(i)
        with open(r'D:\图片\\'+label+r'\{}.jpg'.format(num), 'wb') as f:
            f.write(a.content)
            print('第'+str(num)+'张图片下载成功')
        num += 1
