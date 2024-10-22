# 导包
from time import sleep

from appium import webdriver

# 启动参数
desired_caps = dict()

# 手机的平台类型
desired_caps['platformName'] = 'Android'

# 手机的系统版本
desired_caps['platformVersion'] = '12'

# 手机的名字
desired_caps['deviceName'] = 'HUAWEI'

# 程序的包名
desired_caps['appPackage'] = 'com.android.settings'
# 程序的界面名
desired_caps['appActivity'] = '.Settings$HwSystemDashboardActivity'

# 不重置应用
desired_caps['noReset'] = True

# 支持中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 获取toast
desired_caps['automationName'] = 'Uiautomator2'

# 连接驱动 + 连接手机 + 打开程序（手机的信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


sleep(3)
driver.quit()