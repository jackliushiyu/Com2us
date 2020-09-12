import os
import subprocess
import random
import time
import cv2


class Base:
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


# 截取手机屏幕并保存到电脑
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
if __name__ == '__main__':
    Base.get_screen()
#     # # 命令1：在手机上截图step.png为图片名
#     # cmd1 = r"adb shell /system/bin/screencap -p /sdcard/login.png"
#     #
#     # # 命令2：将图片保存到电脑C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png为要保存到电脑的路径
#     # cmd2 = r"adb pull /sdcard/login.png C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png"
#     # screen = ScreenShot()
#     # screen.screen(cmd1)
#     # screen.save_computer(cmd2)
