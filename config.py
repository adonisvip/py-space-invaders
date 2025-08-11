"""
Game Configuration File
Contains all constants, settings, and configuration values for the Space Invaders game.
"""

import pygame

# Display Settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60

# Game Settings
ROWS = 5
COLS = 5
ALIEN_COOLDOWN = 1000  # Bullet cooldown in milliseconds
COUNTDOWN_TIME = 3

# Player Settings
PLAYER_HEALTH = 3
PLAYER_SPEED = 8
PLAYER_COOLDOWN = 500  # milliseconds

# Bullet Settings
PLAYER_BULLET_SPEED = 5
ALIEN_BULLET_SPEED = 2
MAX_ALIEN_BULLETS = 5

# Alien Settings
ALIEN_MOVE_DISTANCE = 75
ALIEN_MOVE_SPEED = 1

# Explosion Settings
EXPLOSION_SPEED = 3
EXPLOSION_SIZES = {
    1: (20, 20),   # Small explosion
    2: (40, 40),   # Medium explosion
    3: (160, 160)  # Large explosion
}

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
FONT_SIZES = {
    'small': 20,
    'medium': 30,
    'large': 40
}

# Game States
GAME_STATE_MENU = 'menu'
GAME_STATE_PLAYING = 'playing'
GAME_STATE_GAME_OVER = 'game_over'
GAME_STATE_VICTORY = 'victory'

# File Paths
ASSETS_PATH = "img/"
SOUNDS = {
    'explosion': f"{ASSETS_PATH}explosion.wav",
    'explosion2': f"{ASSETS_PATH}explosion2.wav",
    'laser': f"{ASSETS_PATH}laser.wav"
}

IMAGES = {
    'background': f"{ASSETS_PATH}bg.png",
    'spaceship': f"{ASSETS_PATH}spaceship.png",
    'bullet': f"{ASSETS_PATH}bullet.png",
    'alien_bullet': f"{ASSETS_PATH}alien_bullet.png"
} 

# History / Persistence
# File used to store recent game history (last N sessions)
HISTORY_FILE = "history.json"
MAX_HISTORY = 3