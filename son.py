import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click':pygame.mixer.Sound('assets/sounds/click.ogg'),
            'game_over': pygame.mixer.Sound('assets/sounds/game_over.ogg'),
            'meteorite': pygame.mixer.Sound('assets/sounds/meteorite.ogg'),
            'tir': pygame.mixer.Sound('assets/sounds/tir.ogg'),
            'win_p1': pygame.mixer.Sound('assets/sounds/win_p1.ogg'),
            'win_p2': pygame.mixer.Sound('assets/sounds/win_p2.ogg')
        }

    def play(self, name):
        self.sounds[name].play()