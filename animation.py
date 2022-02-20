import pygame

# défnir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses à faire à la crétaion de l'entité
    def __init__(self, name, size=(100, 155)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(name)
        self.animation = False

    # définir une méthode pour démarer l'animation
    def start_animation(self):
        self.animation = True

    # définir une méthode pour animer le sprite
    def animate(self,loop=False):

        # vérifier si l'animation est active
        if self.animation:

            #passer à l'image suivante
            self.current_image += 1

            # vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

                #vérifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # désactivation de l'animation
                    self.animation = False

            # modifier l'image de l'animation précedente par l'image suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# définir une fonction pour charger les image d'un sprite
def load_animation_images(name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"assets/{name}/{name}"

    # boucler sur chaque image dans ce dossier
    for numero in range(1,15):
        image_path = path + str(numero) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images

# définir un dictionnaire qui va contenir les images chargées de chaques images
animations = {
    'mummy':load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'boss' : load_animation_images('boss')
}