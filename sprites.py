"""
Sprites Module
Contains all sprite classes for the Space Invaders game including player, aliens, bullets, and explosions.
"""

import pygame
import random
from config import *

class Spaceship(pygame.sprite.Sprite):
    """
    Player spaceship class
    Handles player movement, shooting, and health management
    """
    
    def __init__(self, x, y, health):
        """
        Initialize the spaceship
        
        Args:
            x (int): Initial x position
            y (int): Initial y position
            health (int): Starting health points
        """
        pygame.sprite.Sprite.__init__(self)
        
        # Load and set up the spaceship image
        self.image = pygame.image.load(IMAGES['spaceship'])
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
        # Health management
        self.health_start = health
        self.health_remaining = health
        
        # Shooting cooldown
        self.last_shot = pygame.time.get_ticks()
        
        # Create collision mask for precise collision detection
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, bullet_group, explosion_group, spaceship_group, game_manager=None):
        """
        Update spaceship state - movement, shooting, and health
        
        Args:
            bullet_group: Sprite group for player bullets
            explosion_group: Sprite group for explosions
            spaceship_group: Sprite group containing the spaceship
            game_manager: Game manager instance for sound effects
            
        Returns:
            int: Game state (-1 for game over, 0 for continue)
        """
        # Get current time for cooldown management
        time_now = pygame.time.get_ticks()
        game_over = 0

        # Handle keyboard input for movement
        key = pygame.key.get_pressed()
        
        # Left movement with boundary check
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
            
        # Right movement with boundary check
        if key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

        # Shooting mechanism with cooldown
        if key[pygame.K_SPACE] and time_now - self.last_shot > PLAYER_COOLDOWN:
            # Create new bullet at spaceship position
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
            
            # Play laser sound if game manager is available
            if game_manager:
                game_manager.handle_laser_sound()

        # Update collision mask
        self.mask = pygame.mask.from_surface(self.image)

        # Draw health bar
        self._draw_health_bar()
        
        # Check if spaceship is destroyed
        if self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            game_over = -1
            
        return game_over

    def _draw_health_bar(self):
        """Draw the health bar below the spaceship"""
        # Draw red background (empty health)
        pygame.draw.rect(pygame.display.get_surface(), RED, 
                        (self.rect.x, self.rect.bottom + 10, self.rect.width, 15))
        
        # Draw green health bar (remaining health)
        if self.health_remaining > 0:
            health_width = int(self.rect.width * (self.health_remaining / self.health_start))
            pygame.draw.rect(pygame.display.get_surface(), GREEN, 
                           (self.rect.x, self.rect.bottom + 10, health_width, 15))


class Bullets(pygame.sprite.Sprite):
    """
    Player bullet class
    Handles bullet movement and collision with aliens
    """
    
    def __init__(self, x, y):
        """
        Initialize bullet
        
        Args:
            x (int): Initial x position
            y (int): Initial y position
        """
        pygame.sprite.Sprite.__init__(self)
        
        # Load bullet image
        self.image = pygame.image.load(IMAGES['bullet'])
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self, alien_group, explosion_group, game_manager=None):
        """
        Update bullet position and check collisions
        
        Args:
            alien_group: Sprite group containing aliens
            explosion_group: Sprite group for explosions
            game_manager: Game manager instance for scoring and sound effects
        """
        # Move bullet upward
        self.rect.y -= PLAYER_BULLET_SPEED
        
        # Remove bullet if it goes off screen
        if self.rect.bottom < 0:
            self.kill()
            
        # Check collision with aliens
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            # Create explosion at bullet position
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)
            
            # Update score and play sound if game manager is available
            if game_manager:
                game_manager.handle_bullet_collision()


class Aliens(pygame.sprite.Sprite):
    """
    Alien enemy class
    Handles alien movement patterns
    """
    
    def __init__(self, x, y):
        """
        Initialize alien
        
        Args:
            x (int): Initial x position
            y (int): Initial y position
        """
        pygame.sprite.Sprite.__init__(self)
        
        # Load random alien image (1-5)
        alien_number = random.randint(1, 5)
        self.image = pygame.image.load(f"{ASSETS_PATH}alien{alien_number}.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
        # Movement variables
        self.move_counter = 0
        self.move_direction = ALIEN_MOVE_SPEED

    def update(self):
        """Update alien movement"""
        # Move alien horizontally
        self.rect.x += self.move_direction
        self.move_counter += 1
        
        # Change direction when reaching movement limit
        if abs(self.move_counter) > ALIEN_MOVE_DISTANCE:
            self.move_direction *= -1
            self.move_counter *= self.move_direction


class Alien_Bullets(pygame.sprite.Sprite):
    """
    Alien bullet class
    Handles alien bullet movement and collision with player
    """
    
    def __init__(self, x, y):
        """
        Initialize alien bullet
        
        Args:
            x (int): Initial x position
            y (int): Initial y position
        """
        pygame.sprite.Sprite.__init__(self)
        
        # Load alien bullet image
        self.image = pygame.image.load(IMAGES['alien_bullet'])
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self, spaceship_group, explosion_group, game_manager=None):
        """
        Update alien bullet position and check collisions
        
        Args:
            spaceship_group: Sprite group containing the spaceship
            explosion_group: Sprite group for explosions
            game_manager: Game manager instance for sound effects
        """
        # Move bullet downward
        self.rect.y += ALIEN_BULLET_SPEED
        
        # Remove bullet if it goes off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
            
        # Check collision with spaceship using mask for precise collision
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            # Reduce spaceship health
            for spaceship in spaceship_group:
                spaceship.health_remaining -= 1
            # Create explosion at bullet position
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)
            
            # Play explosion sound if game manager is available
            if game_manager:
                game_manager.handle_explosion_sound()


class Explosion(pygame.sprite.Sprite):
    """
    Explosion animation class
    Handles explosion animation and cleanup
    """
    
    def __init__(self, x, y, size):
        """
        Initialize explosion
        
        Args:
            x (int): X position for explosion
            y (int): Y position for explosion
            size (int): Size of explosion (1=small, 2=medium, 3=large)
        """
        pygame.sprite.Sprite.__init__(self)
        
        # Load explosion animation frames
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"{ASSETS_PATH}exp{num}.png")
            # Scale image based on explosion size
            scaled_size = EXPLOSION_SIZES[size]
            img = pygame.transform.scale(img, scaled_size)
            self.images.append(img)
            
        # Animation variables
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        """Update explosion animation"""
        # Update animation counter
        self.counter += 1

        # Advance to next frame when counter reaches speed limit
        if self.counter >= EXPLOSION_SPEED and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # Remove explosion when animation is complete
        if self.index >= len(self.images) - 1 and self.counter >= EXPLOSION_SPEED:
            self.kill() 