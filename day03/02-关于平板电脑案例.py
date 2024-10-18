"""
要求
1.滑动的时候不能使用过短时间滑动多一些
2.也不能数滑动几次
3.像人一样去找
"""
# 导包
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

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

# 方式一
# while True:
#     # 定位当前页面所有元素
#     eles = driver.find_elements_by_id("android:id/title")
#     # 存储的是有没有找到指定元素 默认是没找到
#     is_find = False
#     # 循环
#     for ele in eles:
#         # 判断每个元素的文本是不是关于平板电脑
#         if ele.text == "关于平板电脑":
#             # 找到了指定的元素 进行点击
#             ele.click()
#             # 将变量设置为找到了
#             is_find = True
#             # 停止for循环
#             break
#     else:
#         driver.swipe(200,1200,200,600,3000)
#     # 判断是否找了元素，要停止while循环
#     if is_find:
#         break
# 方式二
while True:
    try:
        # 找关于平板电脑 找了点击
        driver.find_element_by_xpath("//*[@text='关于平板电脑']").click()
        # 停止循环
        break
    except NoSuchElementException:
        # 找不到滑动屏幕
        driver.swipe(200, 1200, 200, 850, 3000)



sleep(2)
driver.quit()