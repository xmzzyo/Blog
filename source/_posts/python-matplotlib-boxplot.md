---
title: python matplotlib boxplot
tags: []
thumbnail: ''
mathjax: true
date: 2018-09-23 20:19:15
categories:
	- Python
description:
---

```python
import codecs

import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 17 projects
data = xlrd.open_workbook('projects.xlsx')
table = data.sheets()[0]
data_list = []

for i in range(1, table.nrows):
    data = table.row_values(i)[4:]
    j = 0
    while j < len(data):
        f1 = 2 * data[j] * data[j + 1] / (data[j] + data[j + 1])
        data.insert(j + 2, f1)
        j += 3
    print(len(data))
    data_list.append(data)

data_list = np.array(data_list)
# plt.style.use("ggplot")
# rcParams['boxplot.meanline'] = "x"
precision = []
recall = []
f1_list = []
measurements = ["Precision", "Recall", "F1"]
prf = []
colors = ["#FFC0CB", "#7B68EE", "#778899", "#00FFFF", "#00FF7F", "#20B2AA", "#FFFF00", "#DEB887", "#8B4513", "#FF4500",
          "#800000"]

for i in range(0, len(data_list[0]), 3):
    s = [data_list[:, i], data_list[:, i + 1], data_list[:, i + 2]]
    prf.append(s)

prf = np.array(prf)
bps = []
for i in range(prf.shape[0]):
    s = np.transpose(prf[i])
    offset = (i - 6) * 0.8
    bp = plt.boxplot(
        s,
        positions=np.array(range(s.shape[1])) * 11.0 + offset,
        patch_artist=True,
        notch=False,
        sym="rs",
        vert=True,
        whis=1.5,
        showmeans=True,
        #meanline=True,
        showfliers=False)
    bps.append(bp)
    for patch in bp['boxes']:
        patch.set_facecolor(colors[i])

# for i in range(len(colors) - 1):
#     plt.plot([], c=colors[i], label="Top " + str(i + 1))
# plt.plot([], c=colors[-1], label="ALL")
# plt.legend(loc='right', bbox_to_anchor=(1.01, 0.65), ncol=1, fancybox=False, shadow=False, frameon=False)
labels = ["Top %d" %i for i in range(1, 11)]
labels.append("ALL")
plt.legend([b["boxes"][0] for b in bps], labels, loc='right', bbox_to_anchor=(1.01, 0.65), frameon=False)

plt.xticks(range(0, len(measurements) * 11, 11), measurements)
plt.xlim(-7, len(measurements) * 11)
plt.savefig("prf")
plt.show()
```

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/python-matplotlib-boxplot/84805992.jpg)