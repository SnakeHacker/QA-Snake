#coding:utf8

import jieba
import numpy as np


'''
分句
'''
def sentence_classify(corpus,target_path,keyword):
    fr = open(corpus,"r")
    fw = open(target_path,"a")
    line = fr.readline()
    while line:
        # print line
        if line.__contains__(keyword):
            print line
            fw.write(line)
        line = fr.readline()

    fw.close()
    fr.close()


'''
生成字典
'''
def gen_dic(corpus,target_path):
    fr = open(corpus,"r")
    fw = open(target_path,"a")

    line = fr.readline()

    dic = {}

    while line:

        line = line.strip()
        seg_list = jieba.cut(line)
        for s in seg_list:
            if s in dic.keys():
                dic[s] +=1
            else:
                dic[s] = 1
        # result = " ".join(seg_list)
        # print result

        line = fr.readline()

    i = 0
    for d in dic:
        # print d
        # print "======="
        fw.write(d.encode("utf-8")+"#=#"+str(i)+"\n")
        i += 1

    fr.close()
    fw.close()

'''
获取字典
'''
def get_dic(dic_path):
    fr = open(dic_path)
    line = fr.readline()
    dic = {}
    while line:
        d = line.strip().split("#=#")
        # print d[0]
        # print d[1]
        dic [d[0]] = d[1]
        line = fr.readline()

    fr.close()
    return dic


'''
get_onehot 获取训练集的onehot编码
dic_path 字典路径
corpus_path 语料路径
x_path 训练集的onehot编码
y_path 标签的onehot编码
'''
def get_onehot(dic_path, corpus_path, x_path, y_path):

    dic = get_dic(dic_path)
    fr = open(corpus_path,"r")
    list = []
    list_labels = []

    i = 1
    who = 0
    where = 0
    what = 0
    howmuch = 0
    other = 0

    line = fr.readline()
    while line:
        # print "==="
        # print i
        i += 1

        text = line.strip()

        if "是谁" in text:
            print text
            list_labels.append([0,1,0,0,0])
            who += 1
        elif "在哪里" in text:
            print text
            list_labels.append([0,0,1,0,0])
            where += 1
        elif "是什么" in text:
            print text
            list_labels.append([0,0,0,1,0])
            what += 1
        elif "多少" in text:
            print text
            list_labels.append([0,0,0,0,1])
            howmuch += 1
        else:
            print text
            list_labels.append([1,0,0,0,0])
            other += 1

        temp_list = []
        seg_list = jieba.cut(text)
        onehots = ''
        for seg in seg_list:
            if seg == " ":
                onehot = 1734
                temp_list.append(onehot)
            else:
                onehot = int(dic[seg.encode("utf8")])
                temp_list.append(onehot)

        t = np.array(temp_list)
        list.append(np.lib.pad(t,(0,23-len(temp_list)),'constant',constant_values=(0,0)))
        print onehots

        line = fr.readline()

    print "where"+str(where)
    print "howmuch"+str(howmuch)
    print "what"+str(what)
    print "howucht"+str(howmuch)
    print "other"+str(other)

    fr.close()

    X = np.array(list)
    Y = np.array(list_labels)

    print X
    print Y
    np.savetxt(x_path,X, fmt="%d")
    np.savetxt(y_path,Y, fmt="%d")
'''
    a = np.loadtxt("./corpus/questions/one-hot2.txt")
    b = np.loadtxt("./corpus/questions/one-hot-labels2.txt")
    print a
    print b
'''


# sentence_classify("./corpus/questions/3760questions.txt","./corpus/questions/duoshao.txt","多少")
# gen_dic("./corpus/questions/3760questions.txt","./corpus/questions/ques_dic.txt")

get_onehot("./corpus/questions/ques_dic.txt",
           "./corpus/questions/3760questions.txt",
           "./corpus/questions/one-hot2.txt",
           "./corpus/questions/one-hot-labels2.txt")