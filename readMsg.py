from appium import webdriver
import re
import time

from selenium.webdriver.common.by import By


def write(path, text):
    f = open(path, mode='w', encoding='utf-8')
    f.write(text)
    f.close()


def configMsgRead():
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '11',  # 手机安卓版本
        'deviceName': '172.16.20.169:8888',  # 设备名，安卓手机可以随意填写
        'appPackage': 'com.android.mms',  # 启动APP Package名称
        'appActivity': '.ui.MmsTabActivity',  # 启动Activity名称
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    ele = driver.find_elements(By.ID, "com.android.mms:id/subject")
    print(ele)
    pattern = re.compile(r'(?<=您的验证码为：)\d+\.?\d*')
    code = re.findall(pattern, ele.text)
    print(code)
    string_code = "".join(code)
    print(string_code)
    write('D:/电话.txt', string_code)
    time.sleep(3000)
    print("quit")
    driver.quit()


configMsgRead()
