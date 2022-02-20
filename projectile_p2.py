import pygame

# definir la classe qui va gerer le projectile du joueur
class Projectile_p2(pygame.sprite.Sprite):

    # definir les caractéristiques du projectile
    def __init__(self, player2):
        super().__init__()
        self.velocity = 5

        self.player2 = player2
        self.image = pygame.image.load('assets/projectile.png')
        """	
        fonction : associer une image telechargée au projectile
        entrée : donnée l'arborescence de l'image voulu en tant que projectile
        sortie : l'image demandée est définie en tant que projectile
        """

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player2.rect.x
        self.rect.y = player2.rect.y + 70
        self.origin_image = self.image
        self.angle = 0

    def rotate_p2(self):
        """
        fonction : faire tourner le projectile
        entrée : le projectile, l'angle de rotation
        sortie : le projectile tourne en fonction de l'angle de rotation entrée
        """
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # fonction qui va supprimer le projectile (cette fonction sera appeler lorsque le projectile sort de l'écran
    # ou lorsqu'il rentre en colision avec le joueur1)

    def remove_p2(self):
        self.player2.all_projectiles2.remove(self)

    # fonction qui va gérer le déplacement du projectile
    def move_p2(self):
        self.rect.x -= self.velocity
        self.rotate_p2()

        # verifier si le projectile entre en collision avec le joueur 1
        for player in self.player2.game.check_collision(self, self.player2.game.all_players):
            # supprimer le projectile
            self.remove_p2()
            # infliger des degats
            player.damage(self.player2.attack)

        # verifier si le projectile n'est plus présent sur l'écran

        if self.rect.x < 0:
            #supprimer le projectile (en dehors de l'écran)
            self.remove()