# QA-Snake
![Eric](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/QA/resources/Eric-Logo.png)
# QA-Snake是什么?
目前QA-Snake是一个基于多搜索引擎的自动问答机器人（Eric）
开发历程戳这里：http://www.snakehacker.me/411

# Eric有哪些功能？

* 问答
* 闲聊
* 运价查询（后期要做）

# 使用方法
   测试环境为windows7 + Python2.7(Anaconda2)
   需要额外安装的Python包有：
   * pip install jieba
   * pip install aiml
   * pip install lxml
   * pip install beautifulsoup4
   ##### 下载整个工程，直接运行QA-Snake/QA/MainProgram.py
   ##### 或者 打开dist目录，下载 并安装 QASnake-0.1.0.tar.gz
      pip install QASnake-0.1.0.tar.gz  
   ##### 新建一个.py文件  
      import QA.qa as qa  
      if __name__ == '__main__':    
        qa.qa()  
   
   目前只支持命令行模式和Socket模式，后期会提供更多的接口。

# 演示
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/SnakeQADemo01.png)
![Demo02](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/SnakeQADemo02.png)
![Demo03](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/SnakeQADemo03.png)
# 用Django写的一个网站进行展示
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/qa02.png)
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/qa03.png)
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/qa04.png)
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/qa05.png)
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/qa06.png)
![Demo01](https://raw.githubusercontent.com/SnakeHacker/QA-Snake/master/demo/qa07.png)


## 有问题欢迎反馈
在使用中有任何问题，欢迎反馈给我，我会尽我最大的能力去更正。
可以用以下联系方式跟我交流：

* 邮件(mingjizhou#foxmail.com, 把#换成@)
* QQ: 616976756
* blog: snakehacker.me


## 关于作者
Snake,研究方向：自然语言处理、深度学习。
