# _*_ coding: utf-8 _*_

from selenium import webdriver
import time
import pickle
import os

HOME_PAGE = 'https://www.xuexi.cn/'
LOGIN_LINK = 'https://pc.xuexi.cn/points/login.html'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(executable_path=r'D:\Anaconda3\envs\tensorflow-gpu\Lib\site-packages\selenium\webdriver\chromedriver.exe',options=options)

def login_simulation():
    # 方式二：自己扫码登录
    print("开始模拟登陆")
    browser.get(LOGIN_LINK)
    browser.maximize_window()
    browser.execute_script("var q=document.documentElement.scrollTop=1000")
    time.sleep(10)
    browser.get(HOME_PAGE)
    time.sleep(2)
    print("成功登录完毕\n")

def save_cookie():
    cookie_list = browser.get_cookies()
    print(cookie_list)
    cookie_dict = {}
    for cookie in cookie_list:
        # 写入文件
        f = open(cookie['name'] + '.xuexi', 'wb+')
        pickle.dump(cookie, f)
        f.close()
        if ('name' in cookie) and ('value' in cookie):
            cookie_dict[cookie['name']] = cookie['value']
    return cookie_dict

def read_cookie():
    cookie_dict = {}
    for parent, dirnames, filenames in os.walk('./'):
        for filename in filenames:
            if filename.endswith('.xuexi'):
                #print(filename)
                with open( filename, 'rb') as f:
                    d = pickle.load(f)
                    print(filename,":",d)
                    #cookie_dict[d['name']] = d['value']
                    if ('name' in d) and ('value' in d) and ('expiry' in d):
                        expiry_date = int(d['expiry'])
                        if expiry_date > (int)(time.time()):
                            cookie_dict[d['name']] = d['value']
                        else:
                            return {}
    print("读取cookie成功！")
    return cookie_dict

def login_cookie():
    # 方式二：自己扫码登录
    cookies = read_cookie()
    print("添加cookie：",cookies)
    for item in cookies:
        print(item)
        browser.add_cookie(item)
    print("开始带cookies登陆")
    #browser.get(LOGIN_LINK)
    #browser.maximize_window()
    #browser.execute_script("var q=document.documentElement.scrollTop=1000")
    #time.sleep(10)
    browser.get(HOME_PAGE)
    browser.maximize_window()
    time.sleep(20)
    print("成功登录完毕\n")

if __name__ == '__main__':
    #login_simulation()  # 模拟登录
    #time.sleep(2)
    #get_cookie()
    #browser.quit()
    #login_cookie()  #带cookie登录
    #browser.quit()






