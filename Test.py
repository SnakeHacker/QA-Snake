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



# sentence_classify("./corpus/questions/3760questions.txt","./corpus/questions/duoshao.txt","多少")
# gen_dic("./corpus/questions/3760questions.txt","./corpus/questions/ques_dic.txt")
dic = get_dic("./corpus/questions/ques_dic.txt")

fr = open("./corpus/questions/3760questions.txt","r")
# fw = open("./corpus/questions/one-hot.txt","a")

line = fr.readline()

list = []

i = 1
while line:
    # print "==="
    # print i
    i += 1
    temp_list = []

    text = line.strip()

    if "是谁" in text:
        print text
        list.append([0,1,0,0,0])
    elif "在哪里" in text:
        print text
        list.append([0,0,1,0,0])
    elif "是什么" in text:
        print text
        list.append([0,0,0,1,0])
    elif "多少" in text:
        print text
        list.append([0,0,0,0,1])
    else:
        print text
        list.append([1,0,0,0,0])

    '''
    seg_list = jieba.cut(text)
    onehots = ''

    for seg in seg_list:
        # print seg
        if seg == " ":
            onehot = 1734
            temp_list.append(onehot)
            print onehot
        else:
            onehot = int(dic[seg.encode("utf8")])
            temp_list.append(onehot)
            print onehot
        # print onehot

        # onehots += (onehot + " ")
    print "-----"
    print len(temp_list)
    t = np.array(temp_list)
    list.append(np.lib.pad(t,(0,23-len(temp_list)),'constant',constant_values=(0,0)))
    print onehots
    # fw.write(onehots + "\n")
    '''
    line = fr.readline()


fr.close()
# fw.close()

a = np.array(list)

print a

np.savetxt("./corpus/questions/one-hot-labels.txt",a, fmt="%d")

b = np.loadtxt("./corpus/questions/one-hot-labels.txt")
print b