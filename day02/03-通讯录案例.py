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
desired_caps['appPackage'] = 'com.android.contacts'

# 程序的界面名
desired_caps['appActivity'] = '.activities.PeopleActivity'

# 不重置应用
desired_caps['noReset'] = True

# 支持中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接驱动 + 连接手机 + 打开程序（手机的信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 点击加号
sleep(2)
driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()

# 输入姓氏
driver.find_element_by_xpath("//*[@text='姓氏']").send_keys('zs')

# 输入手机号
sleep(2)
driver.find_element_by_xpath("//*[@text='电话']").send_keys("13333333333")

# 点击保存
sleep(2)
driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()

sleep(2)
driver.quit()
