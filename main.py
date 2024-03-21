# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# import time
#
# # # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# # driver = webdriver.Chrome()
# # #
# # # # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# # # wd.get('https://www.baidu.com')
# # #
# # # # 程序运行完会自动关闭浏览器，就是很多人说的闪退
# # # # 这里加入等待用户输入，防止闪退
# # # input('等待回车键结束程序')
# # # 打开目标网页
# # driver.get('https://www.runoob.com/python3/python3-list.html')
#
# # # 网页截屏，保存图片
# # driver.save_screenshot('screenshot.png')
#
# # # 关闭浏览器
# # driver.quit()
#
#
#
#
# # 创建WebDriver对象
# driver = webdriver.Chrome()
#
# # 打开百度首页
# driver.get("http://www.baidu.com")
#
# # 找到搜索框元素，使用新的定位方法
# search_box = driver.find_element(By.ID, "kw")
#
# # 输入搜索内容
# search_box.send_keys("Python")
#
# # 模拟按下回车键进行搜索
# search_box.send_keys(Keys.RETURN)
#
# # 等待页面加载完成
# time.sleep(5) # 实际使用中可以考虑使用WebDriverWait进行更合适的等待
#
# # 打印当前页面标题，验证是否包含搜索关键词
# print(driver.title)
#
# # 关闭浏览器
# driver.quit()
print("Hello World")