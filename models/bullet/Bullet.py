import pygame as pg
from models.auxiliar import SurfaceManager as sf
from models.constantes import LARGO_VENTANA, ANCHO_VENTANA

class Bullet(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, img_path=True):
        super().__init__()
        self.direction = direction
        self.bullet_image_r = sf.get_surface_from_spritesheet('models\\bullet\\bullet.png',1,1)
        self.bullet_image_l = sf.get_surface_from_spritesheet('models\\bullet\\bullet.png',1,1, flip=True)
        self.image = pg.image.load('models\\bullet\\bullet.png')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    
    def do_shoot(self, surfaces):
        if self.direction == 'True':
            self.bullet_image_l 
            self.rect.x += 10
            if self.rect.x >= ANCHO_VENTANA or (len(surfaces.sprites()) > 0 and self.rect.colliderect(surfaces.sprites()[0])):
                self.kill()
        elif self.direction == 'False':
            self.bullet_image_r
            self.rect.x -= 10
            if self.rect.x <= 0 or (len(surfaces.sprites()) > 0 and self.rect.colliderect(surfaces.sprites()[0])):
                self.kill()
                
    def update(self, delta_ms, surfaces):
        self.do_shoot(surfaces)