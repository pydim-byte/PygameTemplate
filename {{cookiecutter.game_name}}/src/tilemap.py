import pygame,os
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.barrier import Barrier



class Tilemap:
    def __init__(self,level_num=1):
        self.all_sprites = pygame.sprite.Group()
        self.visible_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.skull = pygame.sprite.GroupSingle()
        self.hearts = pygame.sprite.Group()
        self.skull_eyes = pygame.sprite.Group()
        self.xmarks = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.barriers = []
        self.differences = []
        self.static_objects = []
        self.dynamic_objects = []

        if os.path.isfile(f'assets/tilemap/level_{level_num}.tmx'):
            self.tmx_data = load_pygame(f'assets/tilemap/level_{level_num}.tmx')
            self.get_tiles()

    def get_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'):
                for x,y,img in layer.tiles():
                    pos = pygame.Vector2(x * TILE_SIZE * TILE_SCALE, y * TILE_SIZE * TILE_SCALE)
                    self.visible_tiles.add(Tile(pos,img))

        for obj in self.tmx_data.objects:
            pos = pygame.Vector2(obj.x,obj.y)
            images = self.get_images(
                obj.properties['obj_type'],
                obj.properties['images_variation']
                )
            if obj.properties['obj_type'] == 'player':
                self.player.add(Player(pos,images))


    def get_images(self,obj_type,image_count):
        images = []
        for img in range(image_count):
            images.append(pygame.image.load(f'assets/images/{obj_type}/{img}.png').convert_alpha())
        return images