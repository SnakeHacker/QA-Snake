#coding:utf8

import time,os

fr = open('./corpus/3760questions.txt','r')
fw = open('./corpus/shishenme.txt','a')

line = fr.readline()

while line:
    if line.__contains__("是什么")or line.__contains__("什么是"):
        print line
        fw.write(line)
    line = fr.readline()

fr.close()
fw.close()

