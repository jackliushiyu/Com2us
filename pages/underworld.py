from base.base import Base
from base.config import Settings


class Underworld(Settings):
    # args = Settings('underworld')

    def underworld(self):
        template = Base.get_screen()
        img = Base.get_img(r'..\images\login\fight.png')
        while Base.match(img, template) < 0.9:
            Base.get_rand_time(2, 3)
            Base.get_screen()
        Base.click(*Base.get_rand_xy(self.fight_x, self.fight_y))
        pass


if __name__ == '__main__':
    Underworld('underworld').underworld()
