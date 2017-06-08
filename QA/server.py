#coding:utf8

import aiml
import os

from QA.QACrawler import baike
from QA.Tools import Html_Tools as QAT
from QA.Tools import TextProcess as T
from QACrawler import search_summary

if __name__ == '__main__':

    #初始化jb分词器
    T.jieba_initialize()

    #切换到语料库所在工作目录
    mybot_path = './'
    os.chdir(mybot_path)

    mybot = aiml.Kernel()
    mybot.learn(os.path.split(os.path.realpath(__file__))[0]+"/resources/std-startup.xml")
    mybot.learn(os.path.split(os.path.realpath(__file__))[0] + "/resources/Common conversation.aiml")
    mybot.learn(os.path.split(os.path.realpath(__file__))[0] + "/resources/bye.aiml")
    mybot.learn(os.path.split(os.path.realpath(__file__))[0] + "/resources/tools.aiml")
    mybot.learn(os.path.split(os.path.realpath(__file__))[0] + "/resources/bad.aiml")
    mybot.learn(os.path.split(os.path.realpath(__file__))[0] + "/resources/funny.aiml")
    mybot.learn(os.path.split(os.path.realpath(__file__))[0] + "/resources/OrdinaryQuestion.aiml")
    mybot.respond('Load Doc Snake')
    #载入百科属性列表

    print '''
.----------------.  .-----------------. .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | ____  _____  | || |      __      | || |  ___  ____   | || |  _________   | |
| |   /  ___  |  | || ||_   \|_   _| | || |     /  \     | || | |_  ||_  _|  | || | |_   ___  |  | |
| |  |  (__ \_|  | || |  |   \ | |   | || |    / /\ \    | || |   | |_/ /    | || |   | |_  \_|  | |
| |   '.___`-.   | || |  | |\ \| |   | || |   / /__\ \   | || |   |  __'.    | || |   |  _|  _   | |
| |  |`\____) |  | || | _| |_\   |_  | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  _| |___/ |  | |
| |  |_______.'  | || ||_____|\____| | || ||____|  |____|| || | |____||____| | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
 Eric：你好，我是Eric。╭(╯^╰)╮
    '''
    from socket import socket, AF_INET, SOCK_STREAM

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('192.168.1.103',50008))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()
        data = conn.recv(4096)
        input_message = data

        print "input_message====="
        print input_message
        print "=========="


        reply = ''

        if len(input_message) > 60:
            print mybot.respond("句子长度过长")
            reply = mybot.respond("句子长度过长")
            conn.send(reply)
            continue
        elif input_message.strip() == '无':
            print mybot.respond("无")
            reply = mybot.respond("无")
            conn.send(reply)
            continue

        print input_message
        message = T.wordSegment(input_message)
        # 去标点
        print 'word Seg:'+ message
        print '词性：'
        words = T.postag(input_message)

        if message == 'q':
            exit()
        else:
            response = mybot.respond(message)

            print "======="
            print response
            print "======="

            if response == "":
                ans = mybot.respond('找不到答案')
                print 'Eric：' + ans
                reply = mybot.respond('找不到答案')
                conn.send(reply)

            # 百科搜索
            elif response[0] == '#':
                # 匹配百科
                if response.__contains__("searchbaike"):
                    print "searchbaike"
                    print response
                    res = response.split(':')
                    #实体
                    entity = str(res[1]).replace(" ","")
                    #属性
                    attr = str(res[2]).replace(" ","")
                    print entity+'<---->'+attr

                    ans = baike.query(entity, attr)
                    # 如果命中答案
                    if type(ans) == list:
                        print 'Eric：' + QAT.ptranswer(ans,False)
                        reply = QAT.ptranswer(ans,False)
                        conn.send(reply)
                        continue
                    elif ans.decode('utf-8').__contains__(u'::找不到'):
                        #百度摘要+Bing摘要
                        print "通用搜索"
                        ans = search_summary.kwquery(input_message)

                # 匹配不到模版，通用查询
                elif response.__contains__("NoMatchingTemplate"):
                    print "NoMatchingTemplate"
                    ans = search_summary.kwquery(input_message)


                if len(ans) == 0:
                    ans = mybot.respond('找不到答案')
                    print 'Eric：' + ans
                    reply = ans
                    conn.send(reply)

                elif len(ans) >1:
                    print "不确定候选答案"
                    print 'Eric: '
                    for a in ans:
                        print a.encode("utf8")
                        reply += a.encode("utf8")+'\n'
                    conn.send(reply)
                else:
                    print 'Eric：' + ans[0].encode("utf8")
                    reply = ans[0].encode("utf8")
                    conn.send(reply)

            # 匹配模版
            else:
                print 'Eric：' + response
                reply = response
                conn.send(reply)
