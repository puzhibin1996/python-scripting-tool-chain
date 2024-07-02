import time

import uiautomator2 as u2
# 链接设备

d = u2.connect('192.168.0.200')

# 启动抖音极速版
d.app_start('com.ss.android.ugc.aweme.lite')

# 等待应用启动
d(text="首页").wait(timeout=10)

# 刷视频

def swipe_videos(num_swipes=10):
    for _in in range(num_swipes):
        d.swipe_ext("up",scale=0.8)
        time.sleep(2)# 等待视频加载

# 点赞视频
def like_video():
    d.click(0.5,0.8)# 点赞按钮位置

# 收藏视频
def favorite_video():
    d.click(0.5,0.7)# 收藏按钮位置





# 执行测试

swipe_videos(5)
like_video()
favorite_video()

# 验证测试
if d(text = "发送成功").exists(timeout=5.0):
    print("评论发布成功")
else:
    print("培训发布失败")

d.app_start("com.ss.android.ugc.aweme.lite")