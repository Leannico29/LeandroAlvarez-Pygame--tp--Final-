import pygame as pg
import random
from models.constantes import *
from defs_auxiliares import *
from models.player.player import Player
from models.bullet.Bullet import Bullet
from models.enemy.enemy import Enemy
from models.plataformas.piso import plataforma



screen = pg.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pg.init()
pg.display.set_caption("Let's destroy Missigno")
back_img = pg.image.load('models\\backgrounds\\fondo.jpeg') 
back_img =  pg.transform.scale(back_img,(ANCHO_VENTANA, LARGO_VENTANA))
shoots_flag = True
clock = pg.time.Clock()
font = pg.font.Font(None, 37)
game = True
puntos = 0
sapardo = Player(0, 0, frame_rate=120, speed_walk=20, speed_run=30)
missigno = Enemy(250, 0, frame_rate=120, speed_walk=20)
surfaces = pg.sprite.Group()
enemy_group = pg.sprite.Group()
enemy_group.add(missigno)

piso = plataforma(0, LARGO_VENTANA - 70, ANCHO_VENTANA, LARGO_VENTANA)
plataform_1 = plataforma(0, 455, 75, 75)
plataform_2 = plataforma(200, 255, 400, 50)
plataform_3 = plataforma(75, 455, 75, 75)
plataform_4 = plataforma(525,455,75,75)
plataform_5 = plataforma(525,380,75,75)
plataform_6 = plataforma(525,305,75,75)
plataformas = [
    piso, plataform_1, plataform_2, 
    plataform_3,plataform_4,plataform_5,
    plataform_6
    ]
cooler_disparo = 0
enemigo_vivo = True
personaje_vivo = True
while game:

    lista_eventos = pg.event.get()
    lista_teclas_presionadas = pg.key.get_pressed()
    for event in lista_eventos:
        match event.type:
            case pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    sapardo.jump()
            case pg.QUIT:
                print('Adios')
                game = False
                
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        sapardo.walk('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        sapardo.walk('Left')
    if lista_teclas_presionadas[pg.K_RIGHT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_LEFT]:
        sapardo.run('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        sapardo.run('Left')
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        sapardo.stay()
    if lista_teclas_presionadas[pg.K_q] and cooler_disparo == 0:
        sapardo.shoot()
        cooler_disparo += 45


    

    if cooler_disparo > 0:
        cooler_disparo -= 1

    delta_ms = clock.tick(FPS)
    screen.blit(back_img, back_img.get_rect())
    
    for plataforma in plataformas:
            plataforma.draw(screen)
    
    for bullet in sapardo.bullet_group:
        hit_enemies = pg.sprite.spritecollide(bullet, enemy_group, True)
        for enemy in hit_enemies:
            enemy.hit_by_bullet()
            enemigo_vivo = False

    # Check if the player collides with any enemy
    if pg.sprite.spritecollideany(sapardo, enemy_group):
    # If a collision is detected, kill the player
        #sapardo.kill()
        personaje_vivo = False

    #############################################################
    if personaje_vivo:
        sapardo.draw(screen)
        sapardo.update(delta_ms,plataformas )
        sapardo.handle_ground_collision(plataformas)
        sapardo.handle_collisions(plataformas)
        sapardo.bullet_group.update(delta_ms, surfaces)
        sapardo.bullet_group.draw(screen)
    #############################################################
    if enemigo_vivo:
        missigno.update(delta_ms, plataformas)
        missigno.handle_collisions(plataformas)
        missigno.handle_ground_collision(plataformas)
        missigno.draw(screen)
        enemy_group.update(delta_ms,plataformas)
    #############################################################
    pg.display.update()

pg.quit()