import pygame
from config import ASSETS, CHARACTER_SIZE, POWER_SWORD_SIZE, SWORD_SIZE, ZOMBIE_SIZE

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.font = None
        self._load_assets()

    def _load_assets(self):
        try:
            self.images['character'] = self._load_image(ASSETS['character'], CHARACTER_SIZE)
            self.images['power_sword'] = self._load_image(ASSETS['power_sword'], POWER_SWORD_SIZE)
            self.images['sword'] = self._load_image(ASSETS['sword'], SWORD_SIZE)
            self.images['sword_update'] = self._load_image(ASSETS['sword_update'], SWORD_SIZE)
            self.images['zombie'] = self._load_image(ASSETS['zombie'], ZOMBIE_SIZE)

            pygame.mixer.music.load(ASSETS['music'])
            pygame.mixer.music.set_volume(0.2)

            self.font = pygame.font.Font('freesansbold.ttf', 32)
        except Exception as e:
            print(f"Error loading assets: {e}")

            self._create_placeholder_images()

    def _create_placeholder_images(self):

        if 'character' not in self.images:
            self.images['character'] = self._create_placeholder(CHARACTER_SIZE, (0, 255, 0))
        

        if 'power_sword' not in self.images:
            self.images['power_sword'] = self._create_placeholder(POWER_SWORD_SIZE, (255, 255, 0))
        
        if 'sword' not in self.images:
            self.images['sword'] = self._create_placeholder(SWORD_SIZE, (0, 0, 255))
        

        if 'sword_update' not in self.images:
            self.images['sword_update'] = self._create_placeholder(SWORD_SIZE, (255, 0, 255))
        
        if 'zombie' not in self.images:
            self.images['zombie'] = self._create_placeholder(ZOMBIE_SIZE, (255, 0, 0))

    def _create_placeholder(self, size, color):
        surface = pygame.Surface(size, pygame.SRCALPHA)
        surface.fill(color)
        return surface

    def _load_image(self, path, size):
        try:
            image = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(image, size)
        except pygame.error as e:
            print(f"Error loading image {path}: {e}")
            return self._create_placeholder(size, (255, 0, 0))

    def get_image(self, name):
        return self.images.get(name)

    def play_music(self):
        pygame.mixer.music.play()

    def render_text(self, text, color):
        return self.font.render(text, True, color) 