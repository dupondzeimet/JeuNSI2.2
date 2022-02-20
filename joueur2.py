import pygame
from projectile_p2 import Projectile_p2
import animation
import joueur
from son import SoundManager

# créer une classe qui va représenter le joueur
class Player2(animation.AnimateSprite):

    def __init__(self, game):
        """
        fonction : charger les caractéristiques par défaut du premier joueur
        entrée : caractéristiques du joueur
        sortie : le joueur obtiendra les caractéristiques entrées
        """
        # initalise les fonction __inits__ et Sprite
        super().__init__('player2')
        self.game = game
        self.sound_manager = SoundManager()
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 3
        self.jump_high = 8
        self.all_projectiles2 = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player2.png")
        """
        fonction : charge l'image représentant le personnage du joueur
        entrée : donner l'arborescence de l'image voulu
        sortie : le personnage est associé à l'image entrée
        """
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 520


    # créer la barre de vie du joueur
    def update_health_bar_p2(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y + -10, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y + -10, self.health, 7])

    def move_right_p2(self):
        """
        fonction : permet au personnage de se déplacer à droite
        entrée : touche de déplacement
        sortie : la personnage se déplace en fonction de la touche pressée
        """
        self.rect.x += self.velocity



    def move_left_p2(self):
        """
        fonction : permet au personnage de se déplacer à gauche
        entrée : touche de déplacement
        sortie : la personnage se déplace en fonction de la touche pressée
        """
        if self.game.ist_playing_1v1:
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.x -= self.velocity


    def launch_projectile_p2(self):
        # créer une nouvelle instance de la classe projectile_p2
        if self.rect.y < 530 and self.rect.y > 510:
            self.all_projectiles2.add(Projectile_p2(self))


            # ajouter le son
            self.game.sound_manager.play('tir')


    # fonction qui va retirer le bon nombre de pv au joueur et qui va mettre fin à la partie si le joueur n'a plus de vie
    def damage_p2(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de pts de vie
            if self.game.ist_playing_1v1:
                self.game.game_over_1vs1()
            self.sound_manager.play('win_p1')


    def move_up(self):
        self.rect.y -= self.jump_high

    def move_down(self):
        self.rect.y += self.jump_high