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

# 支持中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接驱动 + 连接手机 + 打开程序（手机的信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 点击放大镜
sleep(2)
driver.find_element_by_id("com.android.settings:id/search_action_bar_title").click()


# 定位搜索框
input_keys = driver.find_element_by_id("android:id/search_src_text")

# 输入345678
sleep(2)
input_keys.send_keys("345678")

# 清空
sleep(2)
input_keys.clear()

# 输入910JQKA
input_keys.send_keys("910JQKA")
sleep(2)

# 清空
input_keys.clear()
sleep(2)

# 输入要不起
input_keys.send_keys("要不起")

sleep(2)
driver.quit()