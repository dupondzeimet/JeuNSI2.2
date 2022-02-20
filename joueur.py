import pygame
from projectile import Projectile
# permèttre de récupérer les fonctionnalités définies dans le fichier animation
import animation
from son import SoundManager


# créer une classe qui va représenter le joueur 1
class Player(animation.AnimateSprite):

    def __init__(self, game):
        """
        fonction : charger les caractéristiques par défaut du premier joueur
        entrée : caractéristiques du joueur
        sortie : le joueur obtiendra les caractéristiques entrées
        """
        # initalise les fonction __inits__ et Sprite
        super().__init__('player')
        #accéder au fichier game
        self.game = game
        self.sound_manager = SoundManager()
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 3
        self.jump_high = 8
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        """
        fonction : charge l'image représentant le personnage du joueur
        entrée : donner l'arborescence de l'image voulu
        sortie : le personnage est associé à l'image entrée
        """
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 520


    # fonction qui va retirer le bon nombre de pv au joueur et qui va mettre fin à la partie si le joueur n'a plus de vie
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else :
            # si le joueur n'a plus de pts de vie
            if self.game.is_playing_solo:
                self.game.game_over_solo()
            elif self.game.ist_playing_1v1:
                self.game.game_over_1vs1()
                self.sound_manager.play('win_p2')


    # permet d'actualiser l'animation d'un sprite à l'aide de la fonction "animate" du ficher animation
    def update_animation(self):
        self.animate()

    # créer la barre de vie du joueur
    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y + -10, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y + -10, self.health, 7])


    def launch_projectile(self):
        # créer une nouvelle instance de la classe projectile
        if self.rect.y <530 and self.rect.y > 510:
            self.all_projectiles.add(Projectile(self))

            # ajouter le son
            self.game.sound_manager.play('tir')

    # mettre en place le mouvement du joueur
    def move_right(self):
        """
        fonction : permet au personnage de se déplacer à droite
        entrée : touche de déplacement
        sortie : la personnage se déplace en fonction de la touche pressée
        """
        # si le joueur n'est pas en colission avec un monstre ou le joueur 2
        if self.game.is_playing_solo:
            if not self.game.check_collision(self, self.game.all_monsters):
                self.rect.x += self.velocity
                # démarrer l'animation du joueur
                self.start_animation()
        if self.game.ist_playing_1v1:
            if not self.game.check_collision(self, self.game.all_players_2):
                self.rect.x += self.velocity
                self.start_animation()

    def move_left(self):
        """
        fonction : permet au personnage de se déplacer à gauche
        entrée : touche de déplacement
        sortie : la personnage se déplace en fonction de la touche pressée
        """
        self.rect.x -= self.velocity
        # démarrer l'animation du joueur
        self.start_animation()

    def start_jump(self):
        self.game.jump = True

    def move_up(self):
        self.rect.y -= self.jump_high

    def move_down(self):
        self.rect.y += self.jump_high