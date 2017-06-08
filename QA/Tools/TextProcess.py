#coding:utf8

import jieba
import jieba.posseg as pseg
import os,sys

'''
initialize jieba Segment
'''
def jieba_initialize():
    jieba.load_userdict(os.path.dirname(os.path.split(os.path.realpath(__file__))[0])+'/resources/QAattrdic.txt')
    jieba.initialize()


'''
Segment words by jieba
'''
def wordSegment(text):
    text = text.strip()
    seg_list = jieba.cut(text)
    result = " ".join(seg_list)
    return result


'''
POS Tagging
'''
def postag(text):
    words = pseg.cut(text)
    # for w in words:
    #     print w.word, w.flag
    return words


'''
proecss xiaohuangji corpus
'''
def xiaohuangji_textprocess(fr_path,fw_path):
    fr = open(fr_path,'r')
    fw = open(fw_path,'a')
    line = fr.readline()
    i = 0

    while line:
        if line[0] == 'E':
            question = fr.readline()[2:].strip()
            answer = fr.readline()[2:]
            print question
            print answer
            if len(question)<20 and len(answer)<30:
                i +=1
                qa_pair = question+":::"+answer
                fw.write(qa_pair)
        line = fr.readline()

    fw.close()
    fr.close()
    print 'Finished'

'''
q:::a text processing
'''
def tp2(fr_path,fw_path):
    fr = open(fr_path,'r')
    fw = open(fw_path,'a')
    line = fr.readline()
    while line:
        flag = 0
        words = pseg.cut(line)
        for w in words:
            print w.word, w.flag
            if w.flag == 'nr':
                flag = 1
        if flag == 0:
            fw.write(line)
        line = fr.readline()

    fw.close()
    fr.close()
    print 'Finished'



'''
Load baike attributi name
'''
def load_baikeattr_name(attrdic):
    fr = open(attrdic,'r')
    attr = []
    line = fr.readline()
    while line:
        attr.append(line.strip())
        line = fr.readline()
    fr.close()
    return  attr

'''
Synonyms Analysis,return word in baike attr
word 原始词
synsdic 同义词典
attr 属性
'''
def load_synonyms_word_inattr(word,synsdic,attr):
    fr = open(synsdic,'r')
    tar_word = ''
    line = fr.readline().strip()
    while line:
        words = line.split(" ")
        if word in words:
            for w in words:
                if w in attr:
                  tar_word = w
                  break
        if tar_word != '':
            break
        line = fr.readline()
    fr.close()
    if tar_word == '':
        tar_word = 'Empty'
    return  tar_word

if __name__ == '__main__':
    pass
    # tp2('./corpus/xiaohuangji50w_clean2.txt','./corpus/xiaohuangji50w_clean3.txt')
    # postag("华中科技大学校长是谁？")
