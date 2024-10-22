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
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
# 程序的界面名
desired_caps['appActivity'] = '.activities.NavigationActivity'

# 获取toast
desired_caps['automationName'] = 'Uiautomator2'

# 连接驱动 + 连接手机 + 打开程序（手机的信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(1)
sleep(3)
driver.press_keycode(4)
print(driver.find_element_by_xpath("//*[@text='再次点击即可退出。']").text)

sleep(3)
driver.quit()