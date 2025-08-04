"""
Game Manager
Handles game state management, scoring, and overall game logic.
"""

import pygame
import random
from config import *
from sprites import Spaceship, Aliens, Bullets, Alien_Bullets, Explosion

class GameManager:
    """
    Manages the overall game state, scoring, and game logic
    """
    
    def __init__(self):
        """Initialize the game manager"""
        # Game state
        self.game_state = GAME_STATE_MENU
        self.game_over = 0  # 0=playing, 1=victory, -1=defeat
        
        # Game timing
        self.countdown = COUNTDOWN_TIME
        self.last_count = pygame.time.get_ticks()
        self.last_alien_shot = pygame.time.get_ticks()
        
        # Score tracking
        self.score = 0
        self.player_name = ""
        
        # Sprite groups
        self.spaceship_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        self.alien_bullet_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        
        # Game objects
        self.spaceship = None
        self.bg = None
        
        # Sound effects
        self.sounds = {}
        self._load_sounds()
        
    def _load_sounds(self):
        """Load all sound effects"""
        try:
            self.sounds['explosion'] = pygame.mixer.Sound(SOUNDS['explosion'])
            self.sounds['explosion2'] = pygame.mixer.Sound(SOUNDS['explosion2'])
            self.sounds['laser'] = pygame.mixer.Sound(SOUNDS['laser'])
            
            # Set volume for all sounds
            for sound in self.sounds.values():
                sound.set_volume(0.25)
        except:
            print("Warning: Could not load some sound effects")
    
    def load_background(self):
        """Load the background image"""
        try:
            self.bg = pygame.image.load(IMAGES['background'])
        except:
            print("Warning: Could not load background image")
            # Create a simple background if image fails to load
            self.bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg.fill(BLACK)
    
    def draw_background(self, screen):
        """Draw the background on the screen"""
        if self.bg:
            screen.blit(self.bg, (0, 0))
        else:
            screen.fill(BLACK)
    
    def create_aliens(self):
        """Create the initial alien formation"""
        for row in range(ROWS):
            for item in range(COLS):
                alien = Aliens(100 + item * 100, 100 + row * 70)
                self.alien_group.add(alien)
    
    def create_spaceship(self):
        """Create the player spaceship"""
        self.spaceship = Spaceship(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100, PLAYER_HEALTH)
        self.spaceship_group.add(self.spaceship)
    
    def start_new_game(self, player_name):
        """
        Start a new game with the given player name
        
        Args:
            player_name (str): Name of the player
        """
        self.player_name = player_name
        self.score = 0
        self.game_over = 0
        self.countdown = COUNTDOWN_TIME
        self.last_count = pygame.time.get_ticks()
        self.last_alien_shot = pygame.time.get_ticks()
        
        # Clear all sprite groups
        self.spaceship_group.empty()
        self.bullet_group.empty()
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.explosion_group.empty()
        
        # Create new game objects
        self.create_aliens()
        self.create_spaceship()
        
        self.game_state = GAME_STATE_PLAYING
    
    def update_countdown(self):
        """Update the countdown timer"""
        if self.countdown > 0:
            count_timer = pygame.time.get_ticks()
            if count_timer - self.last_count > 1000:
                self.countdown -= 1
                self.last_count = count_timer
    
    def update_alien_shooting(self):
        """Handle alien shooting logic"""
        time_now = pygame.time.get_ticks()
        
        # Create alien bullets with cooldown and limits
        if (time_now - self.last_alien_shot > ALIEN_COOLDOWN and 
            len(self.alien_bullet_group) < MAX_ALIEN_BULLETS and 
            len(self.alien_group) > 0):
            
            # Choose random alien to shoot
            attacking_alien = random.choice(self.alien_group.sprites())
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            self.alien_bullet_group.add(alien_bullet)
            self.last_alien_shot = time_now
    
    def update_game_logic(self):
        """
        Update all game logic including sprites and game state
        
        Returns:
            int: Game state (-1=defeat, 0=playing, 1=victory)
        """
        if self.countdown == 0:
            # Handle alien shooting
            self.update_alien_shooting()
            
            # Check for victory (all aliens destroyed)
            if len(self.alien_group) == 0:
                self.game_over = 1
                self.game_state = GAME_STATE_VICTORY
            
            # Update game if still playing
            if self.game_over == 0:
                # Update spaceship and check for defeat
                self.game_over = self.spaceship.update(self.bullet_group, self.explosion_group, self.spaceship_group, self)
                
                if self.game_over == -1:
                    self.game_state = GAME_STATE_GAME_OVER
                
                # Update all sprite groups
                self._update_sprite_groups()
                
                # Update score based on destroyed aliens
                self._update_score()
        
        # Update countdown
        self.update_countdown()
        
        # Update explosions
        self.explosion_group.update()
        
        return self.game_over
    
    def _update_sprite_groups(self):
        """Update all sprite groups"""
        self.bullet_group.update(self.alien_group, self.explosion_group, self)
        self.alien_group.update()
        self.alien_bullet_group.update(self.spaceship_group, self.explosion_group, self)
    
    def _update_score(self):
        """Update score based on game events"""
        # Score increases when aliens are destroyed
        # This is handled in the bullet collision detection
        pass
    
    def add_score(self, points):
        """Add points to the current score"""
        self.score += points
    
    def draw_sprites(self, screen):
        """Draw all sprites on the screen"""
        self.spaceship_group.draw(screen)
        self.bullet_group.draw(screen)
        self.alien_group.draw(screen)
        self.alien_bullet_group.draw(screen)
        self.explosion_group.draw(screen)
    
    def handle_bullet_collision(self):
        """Handle bullet collision with aliens and update score"""
        # This is called when a bullet hits an alien
        self.add_score(10)  # 10 points per alien
        if 'explosion' in self.sounds:
            self.sounds['explosion'].play()
    
    def handle_laser_sound(self):
        """Play laser sound when player shoots"""
        if 'laser' in self.sounds:
            self.sounds['laser'].play()
    
    def handle_explosion_sound(self):
        """Play explosion sound when spaceship is hit"""
        if 'explosion2' in self.sounds:
            self.sounds['explosion2'].play()
    
    def reset_game(self):
        """Reset the game to menu state"""
        self.game_state = GAME_STATE_MENU
        self.game_over = 0
        self.countdown = COUNTDOWN_TIME
        self.last_count = pygame.time.get_ticks()
        self.last_alien_shot = pygame.time.get_ticks()
        
        # Clear all sprite groups
        self.spaceship_group.empty()
        self.bullet_group.empty()
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.explosion_group.empty()
    
    def get_player_health(self):
        """Get current player health"""
        if self.spaceship:
            return self.spaceship.health_remaining
        return 0 