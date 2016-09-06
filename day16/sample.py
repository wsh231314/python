'''
Created on Sep 6, 2016

@author: shawn.shaohua.wang
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from urllib import request


# =============================================================
# 找一个网页，例如https://www.python.org/events/python-events/，
# 用浏览器查看源码并复制，然后尝试解析一下HTML，
# 输出Python官网发布的会议时间、名称和地点。
# Author: linuxforshine
# Email: linuxfor@163.com
# Date: 08/27/2016
class MyHTMLParser(HTMLParser):             # <h1>Python</h1>
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.__base_index = {'title': 'event-title', 'location': 'event-location'}
        self.__events = [{}]            # 初始化带一个空字段元素的列表，用于events的存储
        self.__tag = ''                 # tag name
        self.__attrs = {}               # attrs
        self.__data = ''                # text
        self.__index = 0                # 来指示每个event的索引位置
        self.__has_event = False        # 用于标记一个event的开始
        self.__is_location = False      # 用于标记一个event-location的开始，主要用户span含有a标签的特殊处理

    def get_events(self):              # 提供外接访问的接口，返回解析后的数据
        return self.__events

    def error(self, message):
        pass

    def check_attr(self, attr):
        if self.__attrs is not None:
            for k, v in self.__attrs.items():       # 检查是否含有class键，并且值是否为指定值
                if k == 'class' and v == self.__base_index[attr]:
                    return True
        return False

    def reset_flag(self):                          # 复位控制标志
        if self.__is_location is True:
            self.__is_location = False
            self.__has_event = False

    # Note: attrs = [('http-equiv', 'content-type'), ('content', 'text/html; charset=UTF-8')]
    def handle_starttag(self, tag, attrs):  # <h1>
        self.__tag = tag
        self.__attrs = {}                # 每次清空，只存储当前的属性
        for attr in attrs:              # 将列表转换成字典 list -> dict
            self.__attrs[attr[0]] = attr[1]

        if self.__has_event is False:   # 形成类似的自锁功能
            if self.__tag == 'h3' and self.check_attr('title'):
                self.__has_event = True
        else:                           # self.__has_event = True
            if self.__tag == 'span' and self.check_attr('location'):
                self.__is_location = True

    def handle_data(self, data):            # Python
        data = data.strip()                   # 去掉字符串中头部和尾部的多余空白符
        if self.__has_event is True and self.__tag == 'time':
            self.__events[self.__index]['time'] = data
        if self.__is_location is True and self.__tag == 'a':
            self.__events[self.__index]['location'] = self.__data + data
        self.__data = data

    def handle_endtag(self, tag):           # </h1>
        if self.__has_event is False:        # 若event还没被设置则直接退出
            return

        if tag == 'a' and self.__is_location is False:
            self.__events[self.__index]['title'] = self.__data      # IndexError: list index out of range
        elif tag == 'time':
            pass
            # 由于<time>结束标签前还有一个标签，导致下面取到的是<span>的值
            # 故将time的取值移到handle_data事件处理当中
            # self.__events[self.__index]['time'] = self.__data
        elif tag == 'span':
            self.reset_flag()               # 自身引用需要调用self实例对象来引用
            if self.check_attr('location'):
                self.__events[self.__index]['location'] = self.__data
                self.__events.append({})    # 先占位，然后使用索引来进一步修改    ???触发条件
                self.__index += 1           # 完成一个event记录，将索引指向下一条


# 支持解析方式：
# 从网络上直接读取的HTML
# 或者使用本地已经下载好的HTML (默认使用本地HTML)
def get_html_data(mode='local'):
    if mode == 'local':
        with open('./python-events.html', 'r', encoding='utf-8') as f:  # 注意要指定编码方式utf-8
            return f.read()
    elif mode == 'url':
        req = request.Request('https://www.python.org/events/python-events/')
        with request.urlopen(req) as f:
            return f.read().decode('utf-8')


# 使用自定义的HTMLParser来解析HTML
def parse_html(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.get_events()


if __name__ == '__main__':
    events = parse_html(get_html_data('url'))     # 默认不带参数则使用本地已下载的HTML
    print('events numbers = ', len(events))
    print(events)


# 将python输出的数据用文本编辑工具将里面的单引号全部替换成双引号，
# 然后就可以使用JSON在线格式化工具进行格式化了。
# http://c.runoob.com/front-end/53
