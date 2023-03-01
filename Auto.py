import os
import threading
import subprocess
import time
import datetime
from random import randint


# 支持多个手机同时执行上滑操作刷视频
class myThread(threading.Thread):
    def __init__(self, did):
        threading.Thread.__init__(self)
        self.did = did

    def run(self):
        swipePhone(self.did)


# 执行shell命令
def ShellExecute(shellString):
    print(shellString, end=':::' + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S') + '\n')
    subprocess.Popen(shellString, shell=True, stdout=subprocess.PIPE)


# 执行shell命令并拿到返回数据
def getShellExecuteReturn(shellString):
    print(shellString)
    sub = subprocess.Popen(shellString, shell=True, stdout=subprocess.PIPE)
    string = sub.stdout.read()
    results = string.decode().split('\n')
    results1 = []
    for re in results:
        if re is not None and re != '':
            results1.append(re)
    return results1


# 获取手机屏幕尺寸 x和y
def getFull(did):
    screensize = os.popen('adb -s ' + did + ' shell wm size')
    output = screensize.read()
    screensize = output.replace('\n', '')
    screensize = screensize.split(' ')[2]
    screensize = screensize.split('x')
    return screensize


# 滑动屏幕
def swipePhone(did):
    # device_info = os.popen(f"adb devices")
    # print(device_info.read())
    # output_date = os.popen(f"adb connect {adb_name}")
    # print(output_date.read())
    shellString = 'adb -s ' + did + ' shell am start com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity '
    ShellExecute(shellString)
    time.sleep(2)
    # touch_info = os.popen(f"adb shell input tap 119 487")
    # print(touch_info.read())
    full = getFull(did)
    start_x = str(int(full[0]) / 2)
    end_x = str(int(full[0]) / 2)
    start_y = str(int(full[1]) / 10 * 8)
    end_y = str(int(full[1]) / 10)
    print("进入循环操作...")
    while True:
        shellString = 'adb -s ' + did + ' shell input swipe ' + start_x + ' ' + start_y + ' ' + end_x + ' ' + end_y
        ShellExecute(shellString)
        t4 = randint(1, 6)  # 随机看视频时间，防封
        print('等待' + str(t4) + '秒进入下一个视频')
        time.sleep(t4)


adb_name = input('请输入模拟器的编号:')
didList = adb_name.split(',')
for i in didList:
    thread = myThread(i)
    thread.start()
