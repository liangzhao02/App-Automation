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
# 创建TouchAction类对象
action = TouchAction(driver)
# 调用轻敲方法
# action.tap(x=171, y=694).perform()
# action.tap(x=331, y=984, count=20).perform()
# # 按下
# action.press(x=171, y=694).perform()
#
# # 等待
# action.wait(3000).perform()
#
# # 抬起
# action.release().perform()

# 长按
# action.press(x=171, y=694).wait(3000).release().perform()

# 长按
action.long_press(x=171, y=694, duration=3000).release().perform()

sleep(3)
driver.quit()