import pygame

# definir la classe qui va gerer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    # definir les caractéristiques du projectile
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image= pygame.image.load('assets/projectile.png')
        """	
        fonction : associer une image telechargée au projectile
        entrée : donnée l'arborescence de l'image voulu en tant que projectile
        sortie : l'image demandée est définie en tant que projectile
        """

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 90
        self.rect.y = player.rect.y + 70
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        """
        fonction : faire tourner le projectile
        entrée : le projectile, l'angle de rotation
        sortie : le projectile tourne en fonction de l'angle de rotation entrée
        """
        self.angle -= 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # fonction qui va supprimer le projectile (cette fonction sera appeler lorsque le projectile sort de l'écran
    # ou lorsqu'il rentre en collision avec un monstre
    def remove(self):
        self.player.all_projectiles.remove(self)

    # fonction qui va gérer le déplacement du projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger des degats
            monster.damage(self.player.attack)

        # vérifier si le projectile entre en collision avec le joueur 2
        for player2 in self.player.game.check_collision(self, self.player.game.all_players_2):
            # supprimer le projectile
            self.remove()
            # influger les dégats au joueur 2
            player2.damage_p2(self.player.attack)

        # verifier si le projectile n'est plus présent sur l'écran

        if self.rect.x > 1500 :
            #supprimer le projectile (en dehors de l'écran)
            self.remove()