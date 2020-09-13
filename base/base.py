import os
import subprocess
import random
import time
import cv2
from appium import webdriver


class Base:
    def __init__(self, cap: dict, host='localhost', port=4723):
        if 'platformName' in cap:
            self.__driver = webdriver.Remote('http://%s:%d/wd/hub' % (host, port), cap)
        else:
            raise Exception('Base初始化失败')
        pass

    def open_app(self, package, activity):
        """
            启动app
            :param package:
            :param activity:
            :return:
            """
        self.__driver.start_activity(package, activity)
        pass

    def implicitly_wait(self, second):
        self.__driver.implicitly_wait(second)

    @staticmethod
    def get_screen():
        # 截屏口令
        cmd_get = 'adb shell screencap -p /sdcard/screen_img.png'
        # 发送图片口令
        cmd_send = r'adb pull sdcard/screen_img.png C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png'
        # 截屏和发送操作
        os.system(cmd_get)
        os.system(cmd_send)
        img = cv2.imread(r'C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png')
        return img

    @staticmethod
    def get_img(img_path):
        img = cv2.imread(img_path)
        return img

    @staticmethod
    def match(img1, template):
        """img1代表待匹配图像, img2代表模板"""
        res = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED)

        max_res = res.max()

        return max_res

    @staticmethod
    def get_rand_xy(x, y):
        """产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
        xc = random.randint(x[0], x[1])
        yc = random.randint(y[0], y[1])

        return xc, yc

    @staticmethod
    def get_rand_time(a, b):
        """产生a,b间的随机时间延迟"""
        time.sleep(random.uniform(a, b))

    @staticmethod
    def click(x, y):
        """输入两个二维列表，表示要点击的位置的x坐标，y坐标"""
        cmd_click = 'adb shell input tap {} {}'.format(x, y)
        os.system(cmd_click)


class ScreenShot:
    def __init__(self):
        # 查看连接的手机
        connect = subprocess.Popen("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = connect.communicate()   # 获取返回命令
        # 输出执行命令结果结果
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        print(stdout)
        print(stderr)

    # 在手机上截图
    def screen(self, cmd):
        screen_execute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screen_execute.communicate()
        # 输出执行命令结果结果
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        print(stdout)
        print(stderr)

    # 将截图保存到电脑
    def save_computer(self, cmd):
        screen_execute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screen_execute.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        # 输出执行命令结果结果
        print(stdout)
        print(stderr)


class Info:
    def __init__(self):
        """
        确保adb服务启动
        """
        cmd = 'tasklist |findstr adb.exe'
        result = os.popen(cmd)
        adb_info = result.buffer.read().decode(encoding='utf8')
        if 'adb.exe' not in adb_info:
            os.popen('adb start-server')

    def get_platform_version(self):
        """
        获取安卓版本号
        :return:
        """
        l = []
        cmd = 'adb shell getprop ro.build.version.release'
        text = os.popen(cmd)
        for i in text:
            l.append(i.strip())
        return l[0]

    def get_device_name(self):
        """
        获取设备
        :return:
        """
        l = []
        cmd = 'adb devices'
        text = os.popen(cmd)
        for i in text:
            if i.strip().endswith('device'):
                l.append(i.strip())
        return l[0]

    def get_package_and_activity(self, apk_path):
        """
        通过安装包获取包名和activity
        :param apk_path: 安装包路径
        :return: (package,activity)
        """
        cmd_package = 'aapt dumpsys badging %s|findstr package' % apk_path
        cmd_activity = 'aapt dumpsys badging %s|findstr activity' % apk_path
        info_package = os.popen(cmd_package)
        info_activity = os.popen(cmd_activity)
        package = info_package.buffer.read().decode(encoding='utf8').split("'")[1]
        activity = info_activity.buffer.read().decode(encoding='utf8').split("'")[1]
        return package, activity

# if __name__ == '__main__':
#     info = Info()
#     cap = {}
#     cap['platformName'] = 'Android'
#     cap['platformVersion'] = info.get_platform_version()
#     cap['deviceName'] = info.get_device_name()
#     apk_path = r'..\apk\smon_603.apk'
#     apk_info = info.get_package_and_activity(apk_path)
#     driver = Base(cap)
#     driver.open_app(*apk_info)
#     driver.implicitly_wait(50)
#     # # 命令1：在手机上截图step.png为图片名
#     # cmd1 = r"adb shell /system/bin/screencap -p /sdcard/login.png"
#     #
#     # # 命令2：将图片保存到电脑C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png为要保存到电脑的路径
#     # cmd2 = r"adb pull /sdcard/login.png C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png"
#     # screen = ScreenShot()
#     # screen.screen(cmd1)
#     # screen.save_computer(cmd2)
