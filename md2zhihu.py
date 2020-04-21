# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     md2zhihu
   Description :
   Author :       xmz
   date：          2020/4/21
-------------------------------------------------
   Change Activity:
                   2020/4/21:
-------------------------------------------------
"""
__author__ = 'xmz'

import argparse
import functools
import re
from pathlib import Path

Jsdelivr_PREFIX = "https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/asset/"


# Deal with the formula and change them into Zhihu original format
def formula_ops(_lines):
    _lines = re.sub('((.*?)\$\$)(\s*)?([\s\S]*?)(\$\$)\n',
                    '\n<img src="https://www.zhihu.com/equation?tex=\\4" alt="\\4" class="ee_img tr_noresize" eeimg="1">\n',
                    _lines)
    _lines = re.sub('(\$)(?!\$)(.*?)(\$)',
                    ' <img src="https://www.zhihu.com/equation?tex=\\2" alt="\\2" class="ee_img tr_noresize" eeimg="1"> ',
                    _lines)
    return _lines


# The support function for image_ops. It will take in a matched object and make sure they are competible
def rename_image_ref(m, original=True):
    if original:
        image_ref_name = m.group(2)
    else:
        image_ref_name = m.group(1)
    image_ref_name = image_ref_name.replace("../asset/", "")
    if original:
        return "![" + m.group(1) + "](" + Jsdelivr_PREFIX + image_ref_name + ")"
    else:
        return '<img src="' + Jsdelivr_PREFIX + image_ref_name + '"'


# Search for the image links which appear in the markdown file. It can handle two types:
# ![]() and <img src="LINK" alt="CAPTION" style="zoom:40%;" />.
# The second type is mainly for those images which have been zoomed.
def image_ops(_lines):
    _lines = re.sub(r"\!\[(.*?)\]\((.*?)\)", functools.partial(rename_image_ref, original=True), _lines)
    _lines = re.sub(r'<img src="(.*?)"', functools.partial(rename_image_ref, original=False), _lines)
    return _lines


# Deal with table. Just add a extra \n to each original table line
def table_ops(_lines):
    return re.sub("\|\n", r"|\n\n", _lines)


# The main function for this program
def process_for_zhihu():
    with open(str(args.input), "r", encoding='utf8') as f:
        lines = f.read()
        lines = image_ops(lines)
        lines = formula_ops(lines)
        lines = table_ops(lines)
        with open(args.input.parent / (args.input.stem + "_for_zhihu.md"), "w+", encoding='utf8') as fw:
            fw.write(lines)


if __name__ == '__main__':
    # assert len(sys.argv) > 1, "Error: need filename as a argument"
    # filename = sys.argv[1]
    # with open(filename, 'r') as f:
    #     content = f.read()
    # with open(f"{filename}-zhihu", 'w') as f:
    #     f.write(content)
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')
    parser.add_argument(
        '--input',
        type=str,
        help='Path to the file you want to transfer.')

    args = parser.parse_args()
    if args.input is None:
        raise FileNotFoundError("Please input the file's path to start!")
    else:
        args.input = Path(args.input)
        process_for_zhihu()
