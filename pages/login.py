from base.base import Info, Base
from base.config import Settings


class Com2usLogin:
    # 打开软件
    info = Info()
    # 初始化登录坐标点
    login = Settings('login')
    login_activity_x = login.login_activity_x
    login_activity_y = login.login_activity_y

    mail_x = login.mail_x
    mail_y = login.mail_y

    price_x = login.price_x
    price_y = login.price_y
    # 初始化平台信息
    cap = {'platformName': 'Android',
           'platformVersion': info.get_platform_version(),
           'deviceName': info.get_device_name()}

    def com2us_login(self, apk_path):
        """
        :return:
        """
        apk_info = self.info.get_package_and_activity(apk_path)
        # 初始化活动页面以及登录主页面
        login = Base.get_img(r'..\images\login\login.png')
        login2 = Base.get_img(r'..\images\login\login2.png')
        # 打开app
        driver = Base(self.cap)
        driver.open_app(*apk_info)
        driver.implicitly_wait(50)
        # 第一次截图
        template = Base.get_screen()
        Base.get_rand_time(3, 4)
        # 每30截一次图,直到进入登入界面，停止截图
        while Base.match(login, template) < 0.9:
            template = Base.get_screen()
            Base.get_rand_time(10, 20)
            print(Base.match(login2, template))
            if Base.match(login2, template) < 0.9:
                continue
            else:
                print('开始关闭活动页面')
                click = Base.get_rand_xy(self.login_activity_x, self.login_activity_y)
                Base.click(*click)
        Base.get_rand_time(1, 2)
        Base.click(*Base.get_rand_xy([460, 470], [430, 460]))
        print('进入主界面')
        print('关闭邮箱')
        Base.get_rand_time(1, 2)
        Base.click(*Base.get_rand_xy(self.mail_x, self.mail_y))
        print('关闭限时优惠')
        Base.get_rand_time(1, 2)
        Base.click(*Base.get_rand_xy(self.price_x, self.price_y))

if __name__ == '__main__':
    path = r'..\apk\smon_603.apk'
    Com2usLogin().com2us_login(path)
