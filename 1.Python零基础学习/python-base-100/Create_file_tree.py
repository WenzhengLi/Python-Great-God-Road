#!/usr/bin/python
# -*- coding: UTF-8 -*-
for x in range(1, 101):
    try:
        fh = open(str(x)+'-answer.py', "w")
        try:
            fh.write("")
        finally:
            print("关闭文件")
            fh.close()
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
