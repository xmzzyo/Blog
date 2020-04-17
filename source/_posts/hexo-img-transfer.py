# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hexo-img-transfer
   Description :
   Author :       xmz
   date：          2020/4/11
-------------------------------------------------
   Change Activity:
                   2020/4/11:
-------------------------------------------------
"""
import os
import re
import shutil

__author__ = 'xmz'

folder = './'
img_folder = '../../../img/'

md_files = []
img_files = []

for fpathe, dirs, fs in os.walk(folder):
    for f in fs:
        filename = os.path.join(fpathe, f)
        if filename.endswith("md"):
            md_files.append(filename)

for fpathe, dirs, fs in os.walk(img_folder):
    for f in fs:
        filename = os.path.join(fpathe, f)
        if filename.endswith("png") or filename.endswith("jpg"):
            img_files.append(filename)


def copy_img(md_name, imgs):
    for i in imgs:
        for ai in img_files:
            if i in ai:
                if not os.path.exists(md_name):
                    os.makedirs(md_name)
                shutil.copy(ai, md_name)


def rw_md(fn, content):
    with open(fn, "w", encoding='utf8') as f:
        f.writelines(content)


for md in md_files:
    md_n = md.split("/")[-1]
    md_n = md_n.replace(".md", "")
    print(md_n)
    with open(md, 'r', encoding='utf8') as f:
        lines = f.readlines()
        img_path = []
        for i, l in enumerate(lines):
            if re.match(".*https://raw.githubusercontent.com.*", l):
                urls = re.findall("https://raw.githubusercontent.com.*\.[a-z]{2}g", l)
                for url in urls:
                    img = re.findall("[0-9]+\.[a-z]{2}g", url)[0]
                    lines[i] = l.replace(url, f"{md_n}/{img}")
        rw_md(md_n + ".md", lines)
        # img_path.append(img[0])
        # print(img_path)
        # copy_img(md_n, img_path)
