import time
import pygame
file=r"p.mp3"
pygame.mixer.init()
track=pygame.mixer.music.load(file)
pygame.mixer.music.play()



class Period:
    price = 0
    code = ""

    def __init__(self,code):
        self.code = code

