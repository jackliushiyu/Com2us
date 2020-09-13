import cv2
from base.base import Base, ScreenShot
from base.config import Settings


def dog():
    sets = Settings('kill')
    img = cv2.imread(r'images\\login\\again.png')
    times = 1
    max_times = 30
    while True:
        print('——————第 %d 次 次元觉醒 自动开始——————' % times)
        # 命令1：在手机上截图step.png为图片名
        cmd1 = r"adb shell /system/bin/screencap -p /sdcard/step.png"
        # 命令2：将图片保存到电脑C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png为要保存到电脑的路径
        cmd2 = r"adb pull /sdcard/step.png C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png"
        screen = ScreenShot()
        screen.screen(cmd1)
        screen.save_computer(cmd2)
        # 传入截图
        template = cv2.imread(r'images\\temp\\step.png')
        if Base.match(img, template) > 0.9:
            # 再来一次坐标
            again = Base.get_rand_xy(sets.again_x, sets.again_y)
            # 点击再来一次
            Base.click(*again)
            Base.get_rand_time(120, 180)
            Base.click(*Base.get_rand_xy(sets.start_x, sets.start_y))
            Base.get_rand_time(2, 4)
            Base.click(*Base.get_rand_xy([450, 490], [320, 340]))
            Base.get_rand_time(2, 4)
            Base.click(*Base.get_rand_xy(sets.prize_x, sets.prize_y))
            Base.get_rand_time(2, 4)
            Base.click(*Base.get_rand_xy(sets.activity_x, sets.activity_y))
            times += 1
        print('——————第 %d 次自动结束——————' % (times-1))
        if times > max_times:
            break


def experiences():
    """
    刷火山口
    :return:
    """
    sets = Settings('experience')
    img = cv2.imread(r'images\\login\\again2.png')
    times = 1
    max_times = 50
    while True:
        print('——————第 %d 次 经验副本 自动开始——————' % times)
        # 传入截图
        Base.get_rand_time(2, 4)
        template = Base.get_screen()
        if Base.match(img, template) > 0.9:
            # 再来一次坐标
            again = Base.get_rand_xy(sets.again_x, sets.again_y)
            # 点击再来一次
            Base.click(*again)
            Base.get_rand_time(60, 80)
            # 点击遮罩
            Base.click(*Base.get_rand_xy(sets.start_x, sets.start_y))
            Base.get_rand_time(2, 4)
            # 点击箱子
            Base.click(*Base.get_rand_xy([450, 490], [320, 340]))
            Base.get_rand_time(2, 4)
            # 点击确认按钮
            Base.click(*Base.get_rand_xy([440, 520], [430, 470]))
            Base.get_rand_time(2, 4)
            # 出售符文
            Base.click(*Base.get_rand_xy([350, 440], [420, 450]))
            Base.get_rand_time(2, 4)
            # 确认出售符文
            Base.click(*Base.get_rand_xy([340, 440], [310, 340]))
            Base.get_rand_time(2, 4)
            # 活动硬币点击
            Base.click(*Base.get_rand_xy(sets.activity_x, sets.activity_y))
            times += 1
        else:
            Base.get_rand_time(20, 30)
            # 点击遮罩
            Base.click(*Base.get_rand_xy(sets.start_x, sets.start_y))
            Base.get_rand_time(2, 4)
            # 点击箱子
            Base.click(*Base.get_rand_xy([450, 490], [320, 340]))
            Base.get_rand_time(2, 4)
            # 点击确认按钮
            Base.click(*Base.get_rand_xy([440, 520], [430, 470]))
            Base.get_rand_time(2, 4)
            # 出售符文
            Base.click(*Base.get_rand_xy([350, 440], [420, 450]))
            Base.get_rand_time(2, 4)
            # 确认出售符文
            Base.click(*Base.get_rand_xy([340, 440], [310, 340]))
            Base.get_rand_time(2, 4)
            # 活动硬币点击
            Base.click(*Base.get_rand_xy(sets.activity_x, sets.activity_y))
            times += 1
        print('——————第 %d 次自动结束——————' % (times - 1))
        if times > max_times:
            break


def tower():
    sets = Settings()
    img = cv2.imread(r'images\\baita\\tower.png')
    times = 1
    max_times = 74
    while True:
        print('——————第 %d 层塔 开始——————' % times)
        # 命令1：在手机上截图step.png为图片名
        cmd1 = r"adb shell /system/bin/screencap -p /sdcard/step.png"
        # 命令2：将图片保存到电脑C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png为要保存到电脑的路径
        cmd2 = r"adb pull /sdcard/step.png C:\Users\THINK\PycharmProjects\Com2us\images\temp\step.png"
        screen = ScreenShot()
        screen.screen(cmd1)
        screen.save_computer(cmd2)
        # 传入截图
        template = cv2.imread(r'images\\temp\\step.png')
        if Base.match(img, template) > 0.9:
            # 再来一次坐标
            again = Base.get_rand_xy(sets.again_x, sets.again_y)
            # 点击再来一次
            Base.click(*again)
            Base.get_rand_time(5, 6)
            # 点击开始战斗
            Base.click(*Base.get_rand_xy([750, 870], [360, 410]))
            Base.get_rand_time(120, 180)
            # 点击遮罩
            Base.click(*Base.get_rand_xy(sets.start_x, sets.start_y))
            Base.get_rand_time(2, 4)
            # 点击箱子
            Base.click(*Base.get_rand_xy([450, 490], [320, 340]))
            Base.get_rand_time(2, 4)
            # 点击确认
            Base.click(*Base.get_rand_xy([430, 530], [380, 430]))
            Base.get_rand_time(2, 4)
            times += 1
        print('——————第 %d 层塔 结束——————' % (times-1))
        if times > max_times:
            break


if __name__ == '__main__':
    dog()
    # experiences()
    # tower()
