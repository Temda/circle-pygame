import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Game"

# Colors
WHITE = (255, 255, 255)
BG_COLOR = (38, 38, 38)

# Character settings
CHARACTER_SPEED = 1.5
CHARACTER_SIZE = (100, 100)
CHARACTER_START_X = 10
CHARACTER_START_Y = 485

# Zombie settings
ZOMBIE_SIZE = (80, 80)
ZOMBIE_SPEED = 0.8
ZOMBIE_SPAWN_CHANCE = 0.002  # 0.2% chance per frame
MAX_ZOMBIES = 5
ZOMBIE_DETECTION_RADIUS = 300  # How far zombies can see the player

# Power sword settings
POWER_SWORD_SIZE = (50, 50)
POWER_SWORD_SPAWN_CHANCE = 0.005  # 0.5% chance per frame

# Sword settings
SWORD_SIZE = (100, 50)
SWORD_ORBIT_RADIUS = 70
SWORD_ROTATION_SPEED = 2  # Degrees per frame

# Font settings
FONT_SIZE = 32
FONT_FILE = 'freesansbold.ttf'

# Asset paths   
ASSETS = {
    'character': 'anime.gif',
    'power_sword': 'power_sword.png',
    'sword': 'fire-sword.gif',
    'sword_update': 'power_sword_update.png',
    'music': 'powers.mp3',
    'zombie': 'zombie.gif'  # You'll need to add a zombie image
} 