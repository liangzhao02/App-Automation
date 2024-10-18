# 导包
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
driver.implicitly_wait(2)
# 创建TouchAction子对象
action = TouchAction(driver)

driver.find_element_by_xpath("//*[@text='安全性和位置信息']").click()
driver.find_element_by_xpath("//*[@text='屏幕锁定']").click()
driver.find_element_by_xpath("//*[@text='图案']").click()

action.press(x=175, y=610).move_to(x=540, y=610).move_to(x=176, y=973).move_to(x=538, y=975).release().perform()


# sleep(2)
# driver.quit()