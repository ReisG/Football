import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, x_rec=50, y_rec=50):
        super().__init__()
