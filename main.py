import pygame
import math



from jeu import Game
pygame.init()

# définir une horloge
clock = pygame.time.Clock()
FPS = 100

# générer la fenetre du jeu
pygame.display.set_caption("Projet Nsi")
""" 
fonction : définir un titre à la fenêtre du jeu
entrée : titre voulu
sortie : la fenêtre est nommée par le titre entrée
"""
screen = pygame.display.set_mode((1500, 720))
"""
fonction : définir la taille de l'écran en pixels
entrée :  donner dabord la largeur de l'écran et puis la hauteur de l'écran voulu
sortie : écran comportant une largeur et une hauteur correspondant aux valeurs entrées
"""



# importer et charger l'arrière plan
background = pygame.image.load('assets/fonds.png')
"""	
fonction : associer une image telechargée à l'arrière plan du jeu
entrée : donnée l'arborescence de l'image voulu en arrière plan
sortie : l'image demandée est définie en arrière plan dans les dimensions de la fonction screen
"""

#importer et charger la bannière

baragouin = pygame.image.load('assets/baragouin.png')
baragouin = pygame.transform.scale(baragouin,(350,350))
baragouin_rect = baragouin.get_rect()
baragouin_rect.x = 575
baragouin_rect.y = 100


# importer le bouton mode solo

msolo_button = pygame.image.load('assets/Mode Solo.png')
msolo_button = pygame.transform.scale(msolo_button, (400, 150))
msolo_button_rect = msolo_button.get_rect()
msolo_button_rect.x=screen.get_width() /7
msolo_button_rect.y= screen.get_height() / 1.60

# importer le bouton mode 1 vs 1

m1vs1_button = pygame.image.load('assets/Mode_1v1.png')
m1vs1_button = pygame.transform.scale(m1vs1_button, (400,150))
m1vs1_button_rect = msolo_button.get_rect()
m1vs1_button_rect.x = screen.get_width() / 1.75
m1vs1_button_rect.y = screen.get_height() / 1.60




#charger le jeu
game = Game()



running = True
"""
fonction : définit si le jeu est en cours d'execution ou pas
entrée : booléen True si la fenêtre est en cours d'exécution et False si non
sortie : la fenêtre s'ouvre ou non en fonction de l'entrée
"""

# boucle tant que la variable running = True
while running:
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))
    """
    fonction : injecte une image dans un endroit spécifique de la fenêtre
    entrée : largeur et hauteur de l'image en pixels de l'arrière plan
    sortie : application de l'arrière plan sur la surface de la fenêtre
    """

    #Savoir si c'est le mode solo ou le mode 1vs1 qui doit être lancé
    # verifier si notre jeu solo a commencé ou non
    if game.is_playing_solo:
        # déclancher les instructions de la partie solo et afficher sur l'écran le contenu du mode solo
        game.update_solo(screen)
    # vérifier si notre jeu 1v1 a commencé ou non
    elif game.ist_playing_1v1:
        # déclancher les instructions de la partie 1v1 et afficher sur l'écran le contenu du mode 1vs1
        game.update_1v1(screen)

    #verifier si le jeu n'a pas commencé
    else:
        #ajouter l'ecran d'acceuil
        screen.blit(msolo_button,msolo_button_rect)
        screen.blit(m1vs1_button, m1vs1_button_rect)
        screen.blit(baragouin, baragouin_rect)




    # mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'évènement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecter si un joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche 'espace' est enclenchée pour lancer le projectile du joueur 1
            if event.key == pygame.K_SPACE:
                if game.is_playing_solo:
                    game.player.launch_projectile()
                if game.ist_playing_1v1:
                    game.player.launch_projectile()

            # détecter si la touche M est enclenchée pour lancer le projectile du joueur 2
            if event.key == pygame.K_m:
                game.player2.launch_projectile_p2()


            # détecter si la touche 2 est enclenchée pour lancer la partie 1v1
            if event.key == pygame.K_2:
                game.start_1v1()
                # jouer le son
                game.sound_manager.play('click')

            # détecter si la touche 1 est enclenchée pour lancer la partie solo
            if event.key == pygame.K_1:
                game.start_solo()
                # jouer le son
                game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérifier si la souris est en collusion avec le bouton jouer
            if msolo_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start_solo()
                # jouer le son
                game.sound_manager.play('click')

        if event.type == pygame.MOUSEBUTTONDOWN:
            # vérifier si la souris est en collusion avec le bouton jouer
            if m1vs1_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start_1v1()
                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de FPS sur mon horloge
    clock.tick(FPS)