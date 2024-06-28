import uiautomator2 as u2
import pytest
import time


@pytest.fixture(scope="module")
def device():
    # 连接到设备
    d = u2.connect()  # 如果有多个设备，可以使用设备序列号连接：u2.connect('设备序列号')
    d.app_start('com.pas.webcam')  # 启动应用
    yield d
    d.app_stop('com.pas.webcam')  # 停止应用


@pytest.fixture(autouse=True)
def setup_and_teardown(device):
    # 在每个测试前执行
    device.app_start('com.pas.webcam')
    yield
    # 在每个测试后执行
    device.app_stop('com.pas.webcam')

def test_list_01(device):
    text_01='//*[@text="本地广播"]'
    text_01_click=device.xpath(text_01)
    # assert icon.exists,"IP摄像头 Icon图标不存在"
    assert text_01_click.exists,"本地广播不存在"
    text_01_click.click()
    time.sleep(2)
    # 截图
    device.screenshot("test_list_01.png")


def test_list_02(device):
    text_01='//*[@content-desc="返回"]'
    test_01_click=device.xpath(text_01)
    assert test_01_click.exists,"返回按钮不存在"
    test_01_click.click()
    time.sleep(2)
    device.screenshot("test_list_02.png")
