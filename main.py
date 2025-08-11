"""
Space Invaders - Optimized Version
Main game file with modular structure, player name input, and score tracking.

This optimized version includes:
- Modular code structure with separate files for different components
- Player name input system
- Score tracking and display
- Improved game state management
- Better code organization and documentation
"""

import pygame
from pygame import mixer
from pygame.locals import *
import sys

# Import our custom modules
from config import *
from ui_manager import UIManager
from game_manager import GameManager

class SpaceInvadersGame:
    """
    Main game class that orchestrates all game components
    """
    
    def __init__(self):
        """Initialize the game with all components"""
        # Initialize Pygame and mixer
        self._initialize_pygame()
        
        # Create game components
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Space Invaders - Optimized')
        
        # Initialize game managers
        self.ui_manager = UIManager()
        self.game_manager = GameManager()
        
        # Load game assets
        self.game_manager.load_background()
        
        # Game loop control
        self.clock = pygame.time.Clock()
        self.running = True
        
    def _initialize_pygame(self):
        """Initialize Pygame and audio system"""
        # Initialize mixer with optimized settings
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        
    def run(self):
        """Main game loop"""
        while self.running:
            # Handle events
            self._handle_events()
            
            # Update game state based on current state
            if self.game_manager.game_state == GAME_STATE_MENU:
                self._update_menu()
            elif self.game_manager.game_state == GAME_STATE_PLAYING:
                self._update_game()
            elif self.game_manager.game_state == GAME_STATE_GAME_OVER:
                self._update_game_over()
            elif self.game_manager.game_state == GAME_STATE_VICTORY:
                self._update_victory()
            
            # Update display
            pygame.display.update()
            
            # Control frame rate
            self.clock.tick(FPS)
    
    def _handle_events(self):
        """Handle all pygame events"""
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                self.running = False
                return
            
            # Handle events based on game state
            if self.game_manager.game_state == GAME_STATE_MENU:
                self._handle_menu_events(event)
            elif self.game_manager.game_state in [GAME_STATE_GAME_OVER, GAME_STATE_VICTORY]:
                self._handle_end_game_events(event)
    
    def _handle_menu_events(self, event):
        """Handle events during menu state"""
        # Handle player name input
        if self.ui_manager.handle_input_events(event):
            # Player pressed Enter, start game if name is provided
            if self.ui_manager.player_name.strip():
                self.game_manager.start_new_game(self.ui_manager.player_name)
    
    def _handle_end_game_events(self, event):
        """Handle events during game over/victory state"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Restart
                self.game_manager.reset_game()
                self.ui_manager.player_name = ""
            elif event.key == pygame.K_q:  # Quit
                self.running = False
    
    def _update_menu(self):
        """Update and render menu screen"""
        # Draw background
        self.game_manager.draw_background(self.screen)
        
        # Draw menu UI
        last_history = self.game_manager.get_last_history()
        self.ui_manager.draw_menu(self.screen, last_history=last_history)
    
    def _update_game(self):
        """Update and render game screen"""
        # Draw background
        self.game_manager.draw_background(self.screen)
        
        # Update game logic
        game_over = self.game_manager.update_game_logic()
        
        # Draw countdown if still counting down
        if self.game_manager.countdown > 0:
            self.ui_manager.draw_countdown(self.screen, self.game_manager.countdown)
        
        # Draw sprites
        self.game_manager.draw_sprites(self.screen)
        
        # Draw HUD (score, player name, health)
        self.ui_manager.draw_hud(
            self.screen, 
            self.game_manager.score, 
            self.game_manager.player_name, 
            self.game_manager.get_player_health()
        )
    
    def _update_game_over(self):
        """Update and render game over screen"""
        # Draw background
        self.game_manager.draw_background(self.screen)
        
        # Draw game over screen
        self.ui_manager.draw_game_over_screen(
            self.screen, 
            self.game_manager.score, 
            self.game_manager.player_name
        )
    
    def _update_victory(self):
        """Update and render victory screen"""
        # Draw background
        self.game_manager.draw_background(self.screen)
        
        # Draw victory screen
        self.ui_manager.draw_victory_screen(
            self.screen, 
            self.game_manager.score, 
            self.game_manager.player_name
        )
    
    def quit(self):
        """Clean up and quit the game"""
        pygame.quit()
        sys.exit()


def main():
    """
    Main function to start the game
    
    This function:
    1. Creates the game instance
    2. Runs the main game loop
    3. Handles cleanup when the game ends
    """
    try:
        # Create and run the game
        game = SpaceInvadersGame()
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure proper cleanup
        pygame.quit()


if __name__ == "__main__":
    main() 