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

# 滑动屏幕 swipe()
# driver.swipe(179, 1134, 170, 266, 3000)
# 滑动屏幕 scroll()
save = driver.find_element_by_xpath("//*[@text='存储']")
network = driver.find_element_by_xpath("//*[@text='网络和互联网']")
# driver.scroll(save, network, 3000)
# 滑动元素 drag_and_drop
driver.drag_and_drop(save, network)
# sleep(3)
# driver.quit()