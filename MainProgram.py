#coding:utf8
import aiml
import os
import TextProcess as T
import Tools as QAT
from QACrawler import baike

if __name__ == '__main__':

    #初始化jb分词器
    T.jieba_initialize()

    #切换到语料库所在工作目录
    mybot_path = './'
    os.chdir(mybot_path)

    mybot = aiml.Kernel()
    mybot.learn("./resources/std-startup.xml")
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
    while True:
        input_message = raw_input("Enter your message >> ")

        # 预判断
        if len(input_message) > 45:
            print mybot.respond("句子长度过长")
            continue
        elif input_message.strip() == '':
            print mybot.respond("无")
            continue


        message = T.wordSegment(input_message)
        print 'word Seg:'+ message
        print '词性：'
        T.postag(input_message)


        if message == 'q':
            exit()
        else:
            response = mybot.respond(message)

            if response[0] == '#':
                print response
                #加判断
                res = response.split(':')
                #实体
                entity = str(res[1]).replace(" ","")
                #属性
                attr = str(res[2]).replace(" ","")
                print entity+'<---->'+attr

                ans = baike.query(entity,attr)

                #答案处理
                if type(ans)==list:
                    pass
                    print 'Eric：' + QAT.ptranswer(ans,False)
                elif ans.decode('utf-8').__contains__(u'::找不到'):
                    ans = mybot.respond('找不到答案')
                    print 'Eric：' + ans

            else:
                print 'Eric：' + response
