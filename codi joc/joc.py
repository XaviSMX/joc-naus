
import time
from pygame.locals import *
import pygame


guanyador = 0
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)


# pantalles:
# pantalla1=menú
# pantalla2=credits
# pantalla3=joc
# pantalla4=game_over
pantalla_actual=1

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()
pygame.init()
menu_music = pygame.mixer.Sound('assets/Musica_menú.mp3')
menu_music.play()

# vides jugador 1:
vides_imatge1 = pygame.image.load("assets/vida_jugador1.png")

# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 5
vides_jugador1 = 3
# vides jugador 2:
vides_imatge2 = pygame.image.load("assets/vida_jugador2.png")

player_rect2 = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 5
vides_jugador2 = 3
# Jugador 2:
player_image2 = pygame.image.load('assets/naue.png')

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(RED) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 7
temps_entre_bales = 500 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2



pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def mostrar_menu():
    # Mostrar imatge de fons del menú
    imprimir_pantalla_fons('assets/fons_menu.jpg')
    font1 = pygame.font.SysFont(None, 100)
    font2 = pygame.font.SysFont(None, 80)
    img1 = font1.render("Space Warships", True, GREEN)
    img2 = font2.render("1. Jugar", True, WHITE)
    img3 = font2.render("2. Crèdits", True, WHITE)
    img4 = font2.render("3. Sortir", True, WHITE)
    pantalla.blit(img1, (150, 30))
    pantalla.blit(img2, (250, 130))
    pantalla.blit(img3, (250, 230))
    pantalla.blit(img4, (250, 330))



def mostrar_credits():
        # Mostrar credits
        imprimir_pantalla_fons('assets/fons_menu.jpg')
        font1 = pygame.font.SysFont(None, 100)
        font2 = pygame.font.SysFont(None, 65)
        img1 = font1.render("Space Warships", True, GREEN)
        img5 = font2.render("Programacó:", True, WHITE)
        img6 = font2.render("Xavi Balaña", True, RED)
        img7 = font2.render("Gràfics:", True, WHITE)
        img8 = font2.render("Xavi Balaña", True, RED)
        img9 = font2.render("Música: ", True, WHITE)
        img10 = font2.render("Akira Toriyama", True, RED)
        img11 = font2.render("Sons:", True, WHITE)
        img12 = font2.render("Freesound.org", True, RED)
        pantalla.blit(img1, (150, 30))
        pantalla.blit(img5, (150, 130))
        pantalla.blit(img6, (200, 180))
        pantalla.blit(img7, (150, 240))
        pantalla.blit(img8, (200, 290))
        pantalla.blit(img9, (150, 340))
        pantalla.blit(img10, (200, 390))
        pantalla.blit(img11, (150, 440))
        pantalla.blit(img12, (200, 490))
so1_music = pygame.mixer.Sound('assets/so_nau_1.mp3')

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Pantalla de game over
        if pantalla_actual == 4:

            # Restauro viedes dels jugadors
            vides_jugador2 = 3
            vides_jugador1 = 3
            # Elimino les bales del joc
            for i in bales_jugador1:
                bales_jugador1.remove(i)
            for i in bales_jugador2:
                bales_jugador2.remove(i)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    menu_music.play()
                    pantalla_actual = 1
        # Pantalla de crèdits
        elif pantalla_actual ==2:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1
        # pantalla menu
        elif pantalla_actual ==1:
            if event.type == KEYDOWN:
                if event.key == K_1:
                    menu_music.stop()
                    game_music = pygame.mixer.Sound('assets/Musica_joc.mp3')
                    game_music.play()
                    pantalla_actual = 3
                if event.key == K_2:
                    pantalla_actual = 2
                if event.key == K_3:
                    pygame.quit()
        # controlar trets de les naus
        elif pantalla_actual==3:
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    so1_music.play()
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time



                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time
                    so2_music = pygame.mixer.Sound('assets/so_nau_2.mp3')
                    so2_music.play()


    # Mostrar Pantalla Menú:
    if pantalla_actual ==1:
        mostrar_menu()

    # Mostrar Pantalla Crèdits:
    elif pantalla_actual ==2:
        mostrar_credits()

    # Mostrar Pantalla de Game Over:
    if pantalla_actual == 4:
        imprimir_pantalla_fons('assets/game_over.png')
        font = pygame.font.SysFont(None,100)
        text = "Player " + str(guanyador) + " Wins!"
        img = font.render(text, True,WHITE)
        pantalla.blit(img,(170,450))
    # Mostrar Pantalla del Joc:
    if pantalla_actual == 3:




        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)  # eliminem la bala
                vides_jugador2 = vides_jugador2 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vides_jugador1 = vides_jugador1 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        # dibuixar vides jugador 1:
        if vides_jugador1 >=3:
            pantalla.blit(vides_imatge1,(700,560))
        if vides_jugador1 >= 2:
            pantalla.blit(vides_imatge1, (720, 560))
        if vides_jugador1 >= 1:
            pantalla.blit(vides_imatge1, (740, 560))

        # dibuixar vides jugador 2:
        if vides_jugador2 >= 3:
            pantalla.blit(vides_imatge2, (80, 20))
        if vides_jugador2 >= 2:
            pantalla.blit(vides_imatge2, (60, 20))
        if vides_jugador2 >= 1:
            pantalla.blit(vides_imatge2, (40, 20))

        if vides_jugador1 <= 0 or vides_jugador2 <= 0:
            pantalla_actual=4
            game_music.stop()
            go_music = pygame.mixer.Sound('assets/game_over_sound.mp3')
            go_music.play()
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2


    pygame.display.update()
    clock.tick(fps)
