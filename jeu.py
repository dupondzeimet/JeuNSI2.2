# importer la librairie pygame pour avoir accès aux différents fonctions
import pygame

# acccéder aux différents contenus des classes des autres fichiers

from son import SoundManager
from monstre import Monster, Mummy, Boss
from joueur import Player
from joueur2 import Player2
from comet_event import CometFallEvent

# classe qui va representer le jeu et qui contiendra les différents "paramètres" du jeu

class Game:

    def __init__(self):
        # definir si le jeu a commencé ou non
        # définir les variables qui mettront à jour les différents modes
        self.attempt_fall = False
        #self.meteor_fall = False
        self.is_playing_solo = False
        self.ist_playing_1v1 = False
        self.jump = False
        #generer les joueurs
        self.all_players = pygame.sprite.Group()
        self.all_players_2 = pygame.sprite.Group()
        self.player = Player(self)
        self.player2 = Player2(self)
        self.all_players.add(self.player)
        self.all_players_2.add(self.player2)
        # generer la classe de la pluie de comet, CometFallEvent
        self.comet_event = CometFallEvent(self)
        # créer le groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        # gérer le son
        self.sound_manager = SoundManager()
        # mettre le score à 0
        self.police = pygame.font.SysFont("monospace", 25)
        self.score = 0
        # créer le dictionnaire qui va récupérer les touches presser
        self.pressed = {}

    # faire la fonction qui va lancer le mode solo
    def start_solo(self):
        self.is_playing_solo = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Boss)

    # faire la fonction qui va lancer le mode 1vs1
    def start_1v1(self):
        self.ist_playing_1v1 = True

    # fonction qui va ajouter le score
    def add_score(self, points=10):
        self.score += points

    # remettre le jeu a neuf , retirer les monstres, remettre le joueur full vie , remettre le jeu en attente
    def game_over_solo(self):

        self.all_monsters = pygame.sprite.Group()

        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reinitialiser_percent()
        self.is_playing_solo = False

        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    def game_over_1vs1(self):

        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player2.all_projectiles2 = pygame.sprite.Group()
        self.player.rect.x = 200
        self.player.rect.y = 520
        self.player2.rect.x = 1300
        self.player2.rect.y = 520
        self.player.health = self.player.max_health
        self.player2.health = self.player2.max_health
        self.comet_event.reinitialiser_percent()
        self.ist_playing_1v1 = False



    def update_solo(self, screen):

        # afficher le score sur l'écran
        police = pygame.font.SysFont("monospace", 25)
        score_text = self.police.render(f"Score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20,20))

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'évènement
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recuperer les cometes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()


        # appliquer l'ensemble des images du goupe de projectiles
        self.player.all_projectiles.draw(screen)


        # appliquer l'ensemnle des images du groupe de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de mon groupe de comets
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur veut aller à gauche ou à droite et eviter de le faire sortir de la fenêtre
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def update_1v1 (self, screen):
        # appliquer l'image du joueur 1
        screen.blit(self.player.image, self.player.rect)

        #appliquer l'image du joueur 2
        screen.blit(self.player2.image, self.player2.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre de vie du joueur 2
        self.player2.update_health_bar_p2(screen)


        # actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectiles du joueur 1
        for projectile in self.player.all_projectiles:
            projectile.move()

        #récupérer les projectiles du joueur 2
        for projectile2 in self.player2.all_projectiles2:
            projectile2.move_p2()



        # appliquer l'ensemble des images du goupe de projectiles
        self.player.all_projectiles.draw(screen)
        self.player2.all_projectiles2.draw(screen)








        # verifier si le joueur veut aller à gauche ou à droite et eviter de le faire sortir de la fenêtre
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

        # verifier si le joueur 2 veut aller à gauche ou à droite et eviter de le faire sortir de la fenêtre
        if self.pressed.get(pygame.K_RIGHT) and self.player2.rect.x + self.player2.rect.width < screen.get_width():
            self.player2.move_right_p2()
        elif self.pressed.get(pygame.K_LEFT) and self.player2.rect.x > 0:
            self.player2.move_left_p2()

        # détecter si la touche 'z' est enclenchée pour faire sauter le joueur 1 dans le mode 1vs1
        if self.pressed.get(pygame.K_z) and self.player.rect.y > 430:
            self.player.move_up()

        # détecter si la touche 's' est enclenchée pour faire descendre le joueur 1 dans le mode 1vs1
        if self.pressed.get(pygame.K_s) and self.player.rect.y < 520:
            self.player.move_down()

        # détecter si la touche 'flèche du haut' est enclenchée pour faire sauter le joueur 2 dans le mode 1vs1
        if self.pressed.get(pygame.K_UP) and self.player2.rect.y > 430:
            self.player2.move_up()

        # détecter si la touche 'flèche du bas' est enclenchée pour faire descendre le joueur 2 dans le mode 1vs1
        if self.pressed.get(pygame.K_DOWN) and self.player2.rect.y < 520:
            self.player2.move_down()

    # définir la fonction qui va gérer la notion de collision
    def check_collision (self, sprite, group):
        """
        fonction : Vérifie si un object est en collision avec un autre
        entrée : element graphique à comparer avec un autre groupe
        sortie : renvoi le résultat d'une comparaison de collision
        """
        # 4 éléments : compare si le sprite rentre en collision avec le groupe de sprite,
        # sans tuer le monstre lors de la collision, masque de collision
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    #définir la fonction qui va faire apparaitre les différents monstres aux moments voulus
    def spawn_monster(self, monster_class_name):
        monster = Mummy(self)
        self.all_monsters.add(monster_class_name.__call__(self))