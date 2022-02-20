import pygame
import random


#créer une classe pour gerer la boule de feu celeste tah silvain durif

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # définir l'image de la comete
        self.image = pygame.image.load('assets/comet.png')
        self.image = pygame.transform.scale(self.image, (75, 100))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(4,8)
        self.rect.x = random.randint(0, 1500)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        """
        fonction : supprimer la comète
        entrée : la comète voulant être supprimée
        sortie : la comète est supprimée
        """
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de comètes est de 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre à 0
            self.comet_event.reinitialiser_percent
            #apparaitre les monstres
            self.comet_event.game.start_solo()

    def fall(self):
        self.rect.y += self.velocity

        # elle ne tombe pas sur la sol
        if self.rect.y >= 500:
            #retirer la boule de feu
            self.remove()

            # vérifier si il n'y a plus de boules de feu
            if len(self.comet_event.all_comets) == 0:
                #remettre la jauge au debut
                self.comet_event.reinitialiser_percent()
                self.comet_event.fall_mode = False


        # vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #retirer la boule de feu
            self.remove()
            # subir les degats
            self.comet_event.game.player.damage(20)