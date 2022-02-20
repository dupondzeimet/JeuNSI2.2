import pygame
from comets import Comet

# créer une classe pour gérer l'évenement

class CometFallEvent:

    #lors du chargement  --> créer un compteur
    def __init__(self, game):
        self.percent =0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

    # définir un groupe de sprite pour stoquer les cometes
        self.all_comets = pygame.sprite.Group()


    def add_percent(self):
        """
        fonction : ajoute du pourcentage
        entrée : pourcentage actuel
        sortie : pourcentage ajoutée au pourcentage initial
        """
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reinitialiser_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # faire apparaitre plusieurs boules de feu
        for i in range(1, 30):
            # faire apparaitre une première boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenement est totalement chargée

        if self.is_full_loaded() and len(self.game.all_monsters) ==0:
            self.meteor_fall()
            self.fall_mode = True #activer l'evenement

    def update_bar(self, surface):

        #ajouter du poucentage à la barre
        self.add_percent()


        #La barrre noire (ap)
        pygame.draw.rect(surface, (0,0,0), [
            0, #axe des x
            surface.get_height() -20, #axe des y
            surface.get_width(), # longueur de la fenetre
            10 # epaisseur de la barre
        ])

        #La barre rouge
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height() -20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])