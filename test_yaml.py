#!/bin/env python
#-*- coding=utf-8 -*-

import yaml

data = """
f5:
# 蓝汛f5信息
- ip: 192.168.0.1
  dc: lx
  credentials:
    username: huzichun
    password: huzichun!@#
  role: master

# 世纪互联f5信息
- ip: 192.168.0.2
  dc: sjhl
  credentials:
    username: huzichun
    password: huzichun!@#
  role: slave

# 移动f5信息
- ip: 192.168.0.3
  dc: yd
  credentials:
    username: huzichun
    password: huzichun!@#
  role: master
"""

print yaml.dump(yaml.load(data)) 

f = file('f5.yaml', 'w')
yaml.dump(yaml.load(data), f)
f.close()

f = file('f5.yaml', 'r')
infos = yaml.load(f)
#print infos
for info in infos["f5"]:
    if info["ip"] == "192.168.0.2":
        print info["credentials"]["username"], info["credentials"]["password"]

f.close()















































