"""
要求
1.滑动的时候不能使用过短时间滑动多一些
2.也不能数滑动几次
3.像人一样去找
"""
# 导包
from time import sleep

from appium import webdriver

# 启动参数
desired_caps = dict()

# 手机的平台类型
desired_caps['platformName'] = 'Android'

# 手机的系统版本
desired_caps['platformVersion'] = '9'

# 手机的名字
desired_caps['deviceName'] = 'Android'

# 程序的包名
desired_caps['appPackage'] = 'com.android.settings'
# 程序的界面名
desired_caps['appActivity'] = '.Settings'

# 连接驱动 + 连接手机 + 打开程序（手机的信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

sleep(2)
driver.swipe(234,1256,211,264, 5000)

driver.find_element_by_xpath("//*[@text='关于平板电脑']").click()