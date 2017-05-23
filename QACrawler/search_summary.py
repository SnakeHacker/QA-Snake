#coding:utf8

import Tools as To
import TextProcess as T
import time

'''
对百度、Bing 的搜索摘要进行答案的检索
'''

def kwquery(query):
    #分词 去停用词 抽取关键词
    keywords = []
    words = T.postag(query)
    for k in words:
        # 只保留名词
        if k.flag.__contains__("n"):
            # print k.flag
            # print k.word
            keywords.append(k.word)

    answer = []
    text = ''
    # 找到百科的答案就置1
    flag = 0

    # 抓取百度前10条的摘要
    soup_baidu = To.get_html_baidu('https://www.baidu.com/s?wd='+query)
    # print soup_baidu.get_text()

    for i in range(1,10):
        if soup_baidu == None:
            break
        results = soup_baidu.find(id=i)
        if results == None:
            print "百度摘要找不到答案"
            break
        # print '============='
        # print results.attrs
        # print type(results.attrs)
        # print results['class']
        #判断是否有mu,如果第一个是百度知识图谱的 就直接命中答案
        if results.attrs.has_key('mu') and i == 1:
            # print results.attrs["mu"]
            r = results.find(class_='op_exactqa_s_answer')

            # print r
            if r == None:
                print "百度知识图谱找不到答案"
                continue
            else:
                # print r.get_text()
                print "百度知识图谱找到答案"
                answer.append(r.get_text())
                flag = 1
                break
        text += results.get_text()

    if flag == 1:
        return answer


    #获取bing的摘要
    soup_bing = To.get_html_bing('https://www.bing.com/search?q='+query)
    # 判断是否在Bing的知识图谱中
    bingbaike = soup_bing.find(class_="b_xlText b_emphText")

    if bingbaike != None:
        print "Bing知识图谱找到答案"
        flag = 1
        answer.append(bingbaike.get_text())
        # print "====="
        # print answer
        # print "====="
        return answer
    else:
        results = soup_bing.find(id="b_results")
        text += results.get_text()

    # print text


    # 如果再两家搜索引擎的知识图谱中都没找到答案，那么就分析摘要
    if flag == 0:
        #分句
        cutlist = [u"。",u"?",u".", u"_", u"-",u":",u"！",u"？"]
        temp = ''
        sentences = []
        for i in range(0,len(text)):
            if text[i] in cutlist:
                if temp == '':
                    continue
                else:
                    # print temp
                    sentences.append(temp)
                temp = ''
            else:
                temp += text[i]

        # 找到含有关键词的句子,去除无关的句子
        key_sentences = {}
        for s in sentences:
            for k in keywords:
                if k in s:
                    key_sentences[s]=1


        # 根据问题制定规则

        # 识别人名
        target_list = {}
        for ks in key_sentences:
            # print ks
            words = T.postag(ks)
            for w in words:
                # print "====="
                # print w.word
                if w.flag == ("nr"):
                    if target_list.has_key(w.word):
                        target_list[w.word] += 1
                    else:
                        target_list[w.word] = 1

        # 找出最大词频
        sorted_lists = sorted(target_list.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
        # print len(target_list)
        #去除问句中的关键词
        sorted_lists2 = []
        # 候选队列
        for i, st in enumerate(sorted_lists):
            # print st[0]
            if st[0] in keywords:
                continue
            else:
                sorted_lists2.append(st)

        print "返回前n个词频"
        answer = []
        for i,st in enumerate(sorted_lists2):
            # print st[0]
            # print st[1]
            if i< 3:
                answer.append(st[0])
        # print answer

    return answer


if __name__ == '__main__':
    pass
    query = "上海海洋大学的校长是?"
    ans = kwquery(query)
    print "~~~~~~~"
    for a in ans:
        print a
    print "~~~~~~~"
