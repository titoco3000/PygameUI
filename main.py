from Engine import *
import BaseBehaviors

painter = None


def tela_inicial(a):
    global painter
    painter = a
    painter.add(Widget(Vector(0, 0), Vector(300, 300), [
        BaseBehaviors.Image("Circle.png", color=(16, 196, 0,255))
    ]))


if __name__ == "__main__":
    StartApp(Vector(300, 300), tela_inicial)





