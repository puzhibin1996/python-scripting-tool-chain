import time

import uiautomator2 as u2

d = u2.connect()

# print(d.info)

# d.app_start("com.miui.home:id/icon_icon")

# d.current_ime()
# print(d.current_ime())
# d.debug =True
print(d.info)
# d.app_install('D:\\BaiduSyncdisk_2024\\BaiduSyncdisk\\puzhibin\\GitHub_Project\\Python-Scripting-Tools\\python_scripting_tool_chain\\appium\\jiangongjisuanqi4.00.21w.apk')
#
# d.app_uninstall('com.glodon.constructioncalculators')
# time.sleep(40)
# c='//android.widget.ImageView[@content-desc="Play 商店"]'
# element = d.xpath(c)
# element.click()

# a='//android.widget.ImageView[@content-desc="IP摄像头"]'
# a1=d.xpath(a)
# a1.click()
#
# b='//*[@text="本地广播"]'
# b1=d.xpath(b)
# b1.click()
#
# fanhui='//*[@content-desc="返回"]'
# fanhui=d.xpath(fanhui)
# fanhui.click()
# time.sleep(2)


apps = d.app_list_running()
for app in apps:
    # 如果 app 是字符串形式，需要进行处理
    if isinstance(app, str):
        package_name = app  # 假设 app 是包名字符串
        print(f"包名: {package_name}")
        d.app_stop(package_name)
        # time.sleep(1)
        d.app_stop(package_name)
        # time.sleep(1)
    else:
        package_name = app['package']
        app_name = app['label']
        print(f"应用名: {app_name}, 包名: {package_name}")
