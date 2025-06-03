import pygame
import math
import random
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, CHARACTER_SIZE,
    CHARACTER_SPEED, POWER_SWORD_SIZE, POWER_SWORD_SPAWN_CHANCE,
    SWORD_ORBIT_RADIUS, SWORD_ROTATION_SPEED,
    ZOMBIE_SIZE, ZOMBIE_SPEED, ZOMBIE_DETECTION_RADIUS
)

class Character:
    def __init__(self, x, y, assets):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.8
        self.deceleration = 0.4
        self.max_speed = CHARACTER_SPEED
        self.score = 0
        self.assets = assets
        self.rect = pygame.Rect(x, y, CHARACTER_SIZE[0], CHARACTER_SIZE[1])
        self.facing_right = True
        self.rotation_angle = 0
        self.mass = 1.0
        self.friction = 0.92
        self.force_x = 0
        self.force_y = 0
        self.is_alive = True
        self.sword_rects = []

    def update(self):
        if not self.is_alive:
            return

        # Update velocity using force and mass (F = ma)
        self.velocity_x += self.force_x / self.mass
        self.velocity_y += self.force_y / self.mass

        # Apply friction
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction

        # Handle horizontal movement and facing direction
        if abs(self.velocity_x) > 0.1:
            self.facing_right = self.velocity_x > 0

        # Apply maximum speed limit
        speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if speed > self.max_speed:
            self.velocity_x = (self.velocity_x / speed) * self.max_speed
            self.velocity_y = (self.velocity_y / speed) * self.max_speed

        # Update position using velocity
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Keep character within screen bounds with bounce effect
        if self.x < 0:
            self.x = 0
            self.velocity_x *= -0.5
        elif self.x > SCREEN_WIDTH - CHARACTER_SIZE[0]:
            self.x = SCREEN_WIDTH - CHARACTER_SIZE[0]
            self.velocity_x *= -0.5

        if self.y < 0:
            self.y = 0
            self.velocity_y *= -0.5
        elif self.y > SCREEN_HEIGHT - CHARACTER_SIZE[1]:
            self.y = SCREEN_HEIGHT - CHARACTER_SIZE[1]
            self.velocity_y *= -0.5
        
        self.rect.x = self.x
        self.rect.y = self.y

        self.rotation_angle = (self.rotation_angle + SWORD_ROTATION_SPEED) % 360

        self.update_sword_hitboxes()

        self.force_x = 0
        self.force_y = 0

    def update_sword_hitboxes(self):
        self.sword_rects = []
        if self.score > 0:
            for i in range(self.score):
                angle = (i * (360 / self.score) + self.rotation_angle) % 360
                sword_img = self.assets.get_image('sword_update' if self.score > 10 else 'sword')
                
                sword_x = (self.x + CHARACTER_SIZE[0]/2 + 
                          (SWORD_ORBIT_RADIUS * math.cos(math.radians(angle))) - 
                          sword_img.get_width()/2)
                sword_y = (self.y + CHARACTER_SIZE[1]/2 + 
                          (SWORD_ORBIT_RADIUS * math.sin(math.radians(angle))) - 
                          sword_img.get_height()/2)
                
                sword_rect = pygame.Rect(sword_x, sword_y, sword_img.get_width(), sword_img.get_height())
                self.sword_rects.append(sword_rect)

    def move(self, direction_x, direction_y):
        if not self.is_alive:
            return
        
        if direction_x != 0:
            self.force_x = direction_x * self.acceleration * self.mass
        
        if direction_y != 0:
            self.force_y = direction_y * self.acceleration * self.mass

    def check_sword_collision(self, zombie_rect):
        if not self.is_alive or self.score == 0:
            return False
        
        for sword_rect in self.sword_rects:
            if sword_rect.colliderect(zombie_rect):
                return True
        return False

    def draw(self, screen):
        if not self.is_alive:
            return

        character_img = self.assets.get_image('character')
        if not self.facing_right:
            character_img = pygame.transform.flip(character_img, True, False)
        screen.blit(character_img, (self.x, self.y))

        if self.score > 0:
            for i in range(self.score):
                angle = (i * (360 / self.score) + self.rotation_angle) % 360
                sword_img = self.assets.get_image('sword_update' if self.score > 10 else 'sword')
                if not self.facing_right:
                    sword_img = pygame.transform.flip(sword_img, True, False)
                
                sword_x = (self.x + CHARACTER_SIZE[0]/2 + 
                          (SWORD_ORBIT_RADIUS * math.cos(math.radians(angle))) - 
                          sword_img.get_width()/2)
                sword_y = (self.y + CHARACTER_SIZE[1]/2 + 
                          (SWORD_ORBIT_RADIUS * math.sin(math.radians(angle))) - 
                          sword_img.get_height()/2)
                
                rotated_sword = pygame.transform.rotate(sword_img, -angle)
                screen.blit(rotated_sword, (sword_x, sword_y))

class Zombie:
    def __init__(self, x, y, assets):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = ZOMBIE_SPEED
        self.assets = assets
        self.rect = pygame.Rect(x, y, ZOMBIE_SIZE[0], ZOMBIE_SIZE[1])
        self.facing_right = True
        self.is_alive = True

    def update(self, player):
        if not self.is_alive or not player.is_alive:
            return

        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < ZOMBIE_DETECTION_RADIUS:
            if distance > 0:
                self.velocity_x = (dx / distance) * self.speed
                self.velocity_y = (dy / distance) * self.speed
            else:
                self.velocity_x = 0
                self.velocity_y = 0

            self.facing_right = self.velocity_x > 0

            self.x += self.velocity_x
            self.y += self.velocity_y
            self.rect.x = self.x
            self.rect.y = self.y

            if self.rect.colliderect(player.rect):
                player.is_alive = False

    def draw(self, screen):
        if not self.is_alive:
            return
        zombie_img = self.assets.get_image('zombie')
        if not self.facing_right:
            zombie_img = pygame.transform.flip(zombie_img, True, False)
        screen.blit(zombie_img, (self.x, self.y))

class PowerSword:
    def __init__(self, assets):
        self.assets = assets
        self.active = False
        self.x = -100
        self.y = -100
        self.rect = pygame.Rect(self.x, self.y, POWER_SWORD_SIZE[0], POWER_SWORD_SIZE[1])

    def update(self):
        if not self.active and random.random() < POWER_SWORD_SPAWN_CHANCE:
            self.x = random.randint(0, SCREEN_WIDTH - POWER_SWORD_SIZE[0])
            self.y = random.randint(0, SCREEN_HEIGHT - POWER_SWORD_SIZE[1])
            self.active = True
            self.rect.x = self.x
            self.rect.y = self.y

    def draw(self, screen):
        if self.active:
            screen.blit(self.assets.get_image('power_sword'), (self.x, self.y))

    def collect(self):
        self.active = False
        self.x = -100
        self.y = -100
        self.rect.x = self.x
        self.rect.y = self.y 