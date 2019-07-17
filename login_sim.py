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
    pkCookies=pickle.dumps(cookies)
    with open('xuexi.cookie','wb+') as f:
        f.write(jsonCookies)

if __name__ == '__main__':
    print("开始模拟登陆")
    browser.get(LOGIN_LINK)
    browser.maximize_window()
    browser.execute_script("var q=document.documentElement.scrollTop=1000")
    time.sleep(10)
    cookies = browser.get_cookies()
    browser.get
    print("带cookies首页",cookies)
    browser.get(HOME_PAGE)
    time.sleep(10)

    print("删除cookie，打开首页")
    browser.delete_all_cookies()
    browser.get(HOME_PAGE)
    time.sleep(10)

    print("添加cookies")
    for item in cookies:
        if('expiry' in item):
            print("修改前：",item)
            item['expiry'] = int(item['expiry'])
            print("修改后",item)
            browser.add_cookie(item)
        else:
            print(item)
            browser.add_cookie(item)

    print("再次带cookie首页", cookies)
    browser.get(HOME_PAGE)
    time.sleep(10)
    browser.quit()

    