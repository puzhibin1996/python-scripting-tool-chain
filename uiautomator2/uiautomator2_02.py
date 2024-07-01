import uiautomator2 as u2

d = u2.connect()

d(resourceId="com.miui.home:id/icon_icon", description="相册").click()
d.press("home")
d(resourceId="com.miui.home:id/icon_icon", description="微信").click()
d.press("back")
d(resourceId="com.miui.home:id/icon_icon", description="小米移动").click()
d.press("home")