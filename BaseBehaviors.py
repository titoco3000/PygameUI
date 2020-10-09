'''
Cada monobehavior deve conter um metodo update
'''
import pygame
import Engine


class Image(Engine.MonoBehavior):
    def __init__(self, adress, color=(255,255,255,255)):
        self.adress = adress
        self.color = color

    def update(self, widget, painter):
        # load the img
        image = pygame.image.load("images\\"+self.adress).convert_alpha()

        # resize
        image = pygame.transform.scale(image, (widget.size*painter.scaleFactor).to_int().to_tuple())

        # recolor
        color_image = pygame.Surface(image.get_size()).convert_alpha()
        color_image.fill(self.color)
        image.blit(color_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        return painter.screen.blit(image, (widget.position*painter.scaleFactor).to_tuple())




