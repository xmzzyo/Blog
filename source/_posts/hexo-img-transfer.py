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

folder = './source/_posts/'
img_folder = '../../../img/'




def get_all_md():
	md_files = []
	for fpathe, dirs, fs in os.walk(folder):
	    for f in fs:
	        filename = os.path.join(fpathe, f)
	        if filename.endswith("md"):
	            md_files.append(filename)
	return md_files

def get_all_pic():
	img_files = []	
	for fpathe, dirs, fs in os.walk(img_folder):
	    for f in fs:
	        filename = os.path.join(fpathe, f)
	        if filename.endswith("png") or filename.endswith("jpg"):
	            img_files.append(filename)
	return img_files


def copy_img(md_name, imgs):
    for i in imgs:
        for ai in img_files:
            if i in ai:
                if not os.path.exists(md_name):
                    os.makedirs(md_name)
                shutil.copy(ai, md_name)


def rw_md(fn, content):
	print(f"write to {fn}")
	with open(fn, "w", encoding='utf8') as f:
		f.writelines(content)



        # img_path.append(img[0])
        # print(img_path)
        # copy_img(md_n, img_path)

# https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/
def convert_jsdeliver_url():
	js_deliver = "https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/"
	md_files = get_all_md()
	for md in md_files:
	    md_n = md.split("/")[-1]
	    md_n = md_n.replace(".md", "")
	    print(md_n)
	    with open(md, 'r', encoding='utf8') as f:
	        lines = f.readlines()
	        img_path = []
	        for i, l in enumerate(lines):
	        	if re.match(".*!\\[\\]\\(.+\\)*", l) or re.match(".*src=\".+", l):
	        		# print("match")
	        		urls = re.findall(f"({md_n}/[a-z-0-9]+\\.[jp][np]g)", l)
	        		for url in urls:
	        			# print(url)
	        			l = l.replace(url, f"{js_deliver}{url}")
	        			# print(f"{js_deliver}{url}")
	        		lines[i] = l
	    rw_md(folder + md_n + ".md", lines)

if __name__ == "__main__":
	convert_jsdeliver_url()