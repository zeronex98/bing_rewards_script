from selenium import webdriver
import time
import json

# 填写webdriver的保存目录
driver = webdriver.Edge('/Users/XXXX/Downloads/edgedriver_mac64/msedgedriver')

# 打开bing搜索中国区首页
driver.get('https://cn.bing.com/')

# 程序打开网页后20秒内 “手动登陆账户”
time.sleep(60)

with open('cookies.txt','w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()

