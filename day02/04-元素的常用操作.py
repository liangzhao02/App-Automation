# 导包
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

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

# 定位元素
# more = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")

# 获取大小 文本 位置
# print([(i.size,i.text,i.location) for i in more])

# 获取文本
# print([i.text for i in more])
#
# # 获取位置
# print([i.location for i in more])

# 获取已连接的设备的text resource-id class content-desc
deviced = driver.find_element_by_xpath("//*[@text='已连接的设备']")

print(deviced.get_attribute("text"))
print(deviced.get_attribute("name"))
print(deviced.get_attribute("resourceId"))
print(deviced.get_attribute("className"))
print(deviced.get_attribute("name"))