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
desired_caps['appPackage'] = 'com.android.browser'
# 程序的界面名
desired_caps['appActivity'] = '.BrowserActivity'


# 连接驱动 + 连接手机 + 打开程序（手机的信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 定位url输入框
input_url = driver.find_element_by_id("com.android.browser:id/url")
# 点击输入框
input_url.click()
# 输入内容
input_url.send_keys("www.baidu.com")
# 按下回车键
driver.press_keycode(66)
# 获取环境
sleep(3)
contexts = driver.contexts
print(contexts)
# 切换环境
driver.switch_to.context(contexts[1])
# 在百度页面输入123
driver.find_element_by_id("index-kw").send_keys("123")

sleep(3)
driver.quit()