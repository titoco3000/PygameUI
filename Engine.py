# import the pygame module, so you can use it
import pygame


class Vector(object):

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    # operators

    def __add__(self, o):
        return Vector(self.x+o.x, self.y+o.y)

    def __sub__(self, o):
        return Vector(self.x-o.x, self.y-o.y)

    def __mul__(self, o):
        return Vector(self.x*o, self.y*o)

    def __truediv__(self, o):
        return Vector(self.x/o, self.y/o)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def to_int(self):
        return Vector(int(self.x), int(self.y))

    def to_tuple(self):
        return self.x, self.y


class StartApp:
    def __init__(self, start_size, start_point, background_color=(0,0,0)):
        self.widgets = []
        self.sprites = []
        self.scaleFactor = 1.0
        self.size = start_size
        self.baseSize = start_size
        self.background_color=background_color

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("minimal program")

        # create a surface on screen that has the specified size
        self.screen = pygame.display.set_mode(start_size.to_tuple(), pygame.RESIZABLE)

        # call the start point
        start_point(self)


        # define a variable to control the main loop
        running = True

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.size = Vector(event.w, event.h)
                    self.scaleFactor = min(self.size.x / self.baseSize.x, self.size.y / self.baseSize.y)
                    print("ScaleFactor is "+ str(self.scaleFactor))
                    self.clear()
                    self.update()
                    pygame.display.flip()
                elif event.type == pygame.MOUSEBUTTONUP:
                    print(Vector( event.pos[0]*self.baseSize.x/self.size.x, event.pos[1]*self.baseSize.y/self.size.y))

    def update(self):
        for child in self.widgets:
            self.sprites += child.update(self)

    def add(self, w):
        self.widgets.append(w)

    def clear(self):
        print("clearing")
        self.screen.fill(self.background_color)
        self.sprites = []



class Widget:
    def __init__(self, position, size, behaviors=[]):
        self.position = position
        self.size = size
        self.behaviors = behaviors

    def update(self, painter):
        print("Updating widget")
        sprites = []
        for behavior in self.behaviors:
            sprites.append(behavior.update(self, painter))
        return sprites



class MonoBehavior:
    def update(selfself, widget, painter):
        pass

# tools
def clamp(n, smallest, largest): return max(smallest, min(n, largest))
