# -*- coding:utf8 -*-
# 电脑 本身是ASII
# 单行注释
'''
这是段落注释
'''

#from selenium import webdriver
#dr = webdriver.Chrome()
#dr.get('https://www.baidu.com')
# dr = webdriver.Firefox()
#
# dr = webdriver.Edge()

#python 2.7 的写法
for a in range(1,10):
    for b in range(1,a+1):
        print "%d * %d = %d" %(b,a,a*b)," ",
    print "\n"
