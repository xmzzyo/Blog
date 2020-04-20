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

folder = './public/'
img_folder = '../../../img/'

img_files = []


def all_posts():
    md_files = []
    for fpathe, dirs, fs in os.walk(folder):
        for f in fs:
            filename = os.path.join(fpathe, f)
            if filename.endswith("index.html") and "20" in filename and "archive" not in filename:
                # print(filename)
                md_files.append(filename)
    return md_files


def all_images():
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


def replace_url():
    js_deliver = "https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/"
    md_files = all_posts()
    for md in md_files:
        print(md)
        # md_n = md.split("/")[-1]
        # md_n = md_n.replace(".md", "")
        # print(md_n)
        with open(md, 'r', encoding='utf8') as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                if re.match(".*<img\\ssrc=\"(.+?)\".*", l):
                    urls = re.findall("<img\\ssrc=\"(.+?)\"", l)
                    for url in urls:
                        if "touxiang" not in url:
                            l = l.replace(url, js_deliver+url)
                    lines[i] = l
            rw_md(md, lines)
        # img_path.append(img[0])
        # print(img_path)
        # copy_img(md_n, img_path)


if __name__ == "__main__":
    replace_url()
