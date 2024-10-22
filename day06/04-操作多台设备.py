# 导包
from threading import Thread
from time import sleep

from appium import webdriver

def do(port,device):
    # 启动参数
    desired_caps = dict()

    # 手机的平台类型
    desired_caps['platformName'] = 'Android'

    # 手机的系统版本
    desired_caps['platformVersion'] = '9'

    # 手机的名字
    desired_caps['deviceName'] = 'Android'

    # 程序的包名
    desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
    # 程序的界面名
    desired_caps['appActivity'] = '.activities.NavigationActivity'

    # 手机名
    desired_caps["udid"]  = device

    # 连接驱动 + 连接手机 + 打开程序（手机的信息）
    driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub" % port, desired_caps)

    sleep(3)
    driver.quit()

data = [("4723","emulator-5554"),("4725","emulator-5556")]
for i in data:
    Thread(target=do,args=i).start()