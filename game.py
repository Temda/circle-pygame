import pygame
import sys
import random
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,
    BG_COLOR, WHITE, CHARACTER_START_X, CHARACTER_START_Y,
    ZOMBIE_SPAWN_CHANCE, MAX_ZOMBIES
)
from assets import AssetManager
from entities import Character, PowerSword, Zombie

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        
        self.assets = AssetManager()
        self.character = Character(CHARACTER_START_X, CHARACTER_START_Y, self.assets)
        self.power_sword = PowerSword(self.assets)
        self.zombies = []
        self.running = True
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.kill_count = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()

    def _handle_keydown(self, key):
        if key == pygame.K_LEFT:
            self.character.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.character.move(1, 0)
        elif key == pygame.K_UP:
            self.character.move(0, -1)
        elif key == pygame.K_DOWN:
            self.character.move(0, 1)

    def _handle_keyup(self, key):
        pass

    def spawn_zombie(self):
        if len(self.zombies) < MAX_ZOMBIES and random.random() < ZOMBIE_SPAWN_CHANCE:

            side = random.randint(0, 3)
            if side == 0:  
                x = random.randint(0, SCREEN_WIDTH)
                y = -80
            elif side == 1:
                x = SCREEN_WIDTH
                y = random.randint(0, SCREEN_HEIGHT)
            elif side == 2:
                x = random.randint(0, SCREEN_WIDTH)
                y = SCREEN_HEIGHT
            else:  
                x = -80
                y = random.randint(0, SCREEN_HEIGHT)
            
            self.zombies.append(Zombie(x, y, self.assets))

    def update(self):
        if not self.character.is_alive:
            self.game_over = True
            return

        # Handle keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.character.move(1, 0)
        if keys[pygame.K_UP]:
            self.character.move(0, -1)
        if keys[pygame.K_DOWN]:
            self.character.move(0, 1)

        self.character.update()
        self.power_sword.update()

        # Spawn and update zombies
        self.spawn_zombie()
        
        for zombie in self.zombies[:]:
            zombie.update(self.character)
            
            if zombie.is_alive and self.character.check_sword_collision(zombie.rect):
                zombie.is_alive = False
                self.kill_count += 1
                self.character.score += 1

        self.zombies = [zombie for zombie in self.zombies if zombie.is_alive]

        if self.power_sword.active and self.character.rect.colliderect(self.power_sword.rect):
            self.character.score += 1
            self.power_sword.collect()
            self.assets.play_music()

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        self.power_sword.draw(self.screen)
        self.character.draw(self.screen)
        
        for zombie in self.zombies:
            zombie.draw(self.screen)
        
        score_text = self.assets.render_text(f"Score: {self.character.score}", WHITE)
        kill_text = self.assets.render_text(f"Kills: {self.kill_count}", WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(kill_text, (10, 50))

        if self.game_over:
            game_over_text = self.assets.render_text("GAME OVER - Press R to Restart", WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.update()

    def reset_game(self):
        self.character = Character(CHARACTER_START_X, CHARACTER_START_Y, self.assets)
        self.power_sword = PowerSword(self.assets)
        self.zombies = []
        self.game_over = False
        self.kill_count = 0

    def run(self):
        while self.running:
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit() 