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

def save_cookie():
    cookies=browser.get_cookies()
    print("开始保存cookie! ",cookies)
    pkCookies=pickle.dumps(cookies)
    with open('xuexi.cookie','wb+') as f:
        f.write(pkCookies)
        print("cookie已保存！")

def read_cookie():
    with open('xuexi.cookie','rb') as f:
        pkCookies=pickle.load(f)
        print("开始读取cookie! ",pkCookies)
        for item in pkCookies:
            if ('expiry' in item) and (item['expiry'] != (int(item['expiry']))):
                print("修改前：", item)
                item['expiry'] = int(item['expiry'])   #学习强国返回的expiry有小数，去掉
                print("修改后：", item)
                browser.add_cookie(item)
            else:
                print("未修改：",item)
                browser.add_cookie(item)

def login_sim():
    print("开始模拟登陆")
    browser.get(LOGIN_LINK)
    browser.maximize_window()
    browser.execute_script("var q=document.documentElement.scrollTop=1000")
    time.sleep(20)

if __name__ == '__main__':
    browser.get(HOME_PAGE)
    #time.sleep(5)
    browser.maximize_window()
    if(os.path.exists('xuexi.cookie')):
        print("cookie存在！")
        read_cookie()    #读cookie
        print("读完cookie，打开首页")
    else:
        print("cookie不存在，进入登录页面！")
        login_sim()     #模拟登录
        save_cookie()

    browser.get(HOME_PAGE)
    save_cookie()      #更新cookie
    time.sleep(10)
    print("删除cookie，打开首页")
    browser.delete_all_cookies()
    browser.get(HOME_PAGE)
    time.sleep(10)
    browser.quit()