import pygame

# ajouter de l'aléatoire (pour les coordonnées d'apparition des monstres ...)
import random
#accéder aux différentes fonction du fichier animation
import animation

# créer une classe qui va gérer la notion de monstre sur le jeu
class Monster(animation.AnimateSprite):
# définir le constructeur
    def __init__(self, game, name, size, argument_inutile=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1400 + random.randint(0, 100)
        self.rect.y = 540 - argument_inutile
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 4)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        """
        fonction : infliger des dégats aux monstres grâce aux projectiles
        entrée : projectile qui rentre en collision et le monstre concernée
        sortie : le monstre subit des dégats
        """
        self.health -= amount

        # Verifier si son nouveau nombre de pv est < ou = à 0
        if self.health <= 0:
            # reapparaitre comme un nouveau monstre
            self.rect.x = 1400 + random.randint(0, 100)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter le nombre de points
            self.game.add_score(self.loot_amount)

        # vérifier si la barre d'évènement est chargée à son maximum
        if self.game.comet_event.is_full_loaded():
            #retirer du jeu
            self.game.all_monsters.remove(self)

            # appeler la methode pour déclancher la pluie de comètes
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats (au joueur)
            self.game.player.damage(self.attack)

# définir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy",(130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

# définir une classe pour l'alien
class Boss(Monster):

    def __init__(self, game):
        super().__init__(game, "boss",(200, 200), 70)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)