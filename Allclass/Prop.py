from setting.settings import *
from Allclass.BallGroup import *


class Prop:
    def __init__(self, type, pos):
        self.type = type
        self.type1 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_two.png"))
        self.type2 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_double.png"))
        self.type3 = image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/prop_blood.png"))
        if self.type == 1:
            self.image = self.type1
        elif self.type == 2:
            self.image = self.type2
        elif self.type == 3:
            self.image = self.type3
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)
        nle.play()

    def move(self, bx, ballg, blood):
        self.rect = self.rect.move((0, pv))

        #道具事件
        if Rect(bx - 40, 500, 80, 15).colliderect(self):
            if self.type == 1:
                bom.play()
                ballg.add_demo(tuple(math.Vector2(1, 1).normalize()*bv), pos=(bx-4, 500-16))
                ballg.add_demo(tuple(math.Vector2(-1, 1).normalize() * bv), pos=(bx - 4, 500 - 16))
            elif self.type == 2:
                super.play()
                add = []
                for ball in ballg.balls:
                    v1 = math.Vector2(ball.speed).rotate(45).normalize()*bv
                    add.append(ballg.demo(tuple(v1), ball.rect[:2]))
                    v2 = math.Vector2(ball.speed).rotate(-45).normalize() * bv
                    add.append(ballg.demo(tuple(v2), ball.rect[:2]))
                ballg.adds(add)
            elif self.type == 3:
                bon.play()
                blood.num += 1
