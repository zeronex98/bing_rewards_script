import json
import random
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

def OpenUrl(url):
    # 访问网址
    driver.get(url)
    with open('cookies.txt', 'r') as f: #由于webdriver启动时类似无痕模式，使用带cookie的方式登录微软账号
        cookies_list = json.load(f)
        for cookie in cookies_list:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)

def run():
    OpenUrl('https://cn.bing.com/search?q='+str(random_number))

if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless")  #设置后台运行，无窗口化
    mobile_emulation = {'deviceName': 'iPhone 6'}   #添加移动端
    options.add_experimental_option("mobileEmulation", mobile_emulation)    #使用移动端模拟器打开
    driver = webdriver.Edge('/Users/XXXX/Downloads/edgedriver_mac64/msedgedriver', options=options)
    for i in range(30):
        random_number = random.randint(1, 100)
        run()
        print('第', i + 1, '次完成')
        time.sleep(2)
    driver.quit()
    print('Mission Complete')
