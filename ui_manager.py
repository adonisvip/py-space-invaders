"""
UI Manager
Handles all user interface elements including text rendering, menus, and input handling.
"""

import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZES, WHITE, RED, GREEN, YELLOW

class UIManager:
    def __init__(self):
        """Initialize UI manager with fonts and UI elements"""
        # Initialize fonts with different sizes
        self.fonts = {
            'small': pygame.font.SysFont('Constantia', FONT_SIZES['small']),
            'medium': pygame.font.SysFont('Constantia', FONT_SIZES['medium']),
            'large': pygame.font.SysFont('Constantia', FONT_SIZES['large'])
        }
        
        # Input field for player name
        self.player_name = ""
        self.input_active = False
        self.input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 30)
        
    def draw_text(self, text, font_size, color, x, y, center=False):
        """
        Draw text on screen
        
        Args:
            text (str): Text to display
            font_size (str): Font size key ('small', 'medium', 'large')
            color (tuple): RGB color tuple
            x (int): X position
            y (int): Y position
            center (bool): Whether to center the text horizontally
        """
        font = self.fonts[font_size]
        img = font.render(text, True, color)
        
        if center:
            x = x - img.get_width() // 2
            
        return img, (x, y)
    
    def draw_centered_text(self, text, font_size, color, y):
        """Draw text centered horizontally on screen"""
        img, (x, _) = self.draw_text(text, font_size, color, SCREEN_WIDTH // 2, y, center=True)
        return img, (x, y)
    
    def draw_menu(self, screen, last_history=None):
        """Draw the main menu screen
        Args:
            last_history (list[dict] | None): recent history entries
        """
        # Title
        title_img, title_pos = self.draw_centered_text("SPACE INVADERS", 'large', WHITE, 200)
        screen.blit(title_img, title_pos)
        
        # Instructions
        instructions = [
            "Enter your name:",
            "Press ENTER to start",
            "Use ARROW KEYS to move",
            "Press SPACE to shoot"
        ]
        
        for i, instruction in enumerate(instructions):
            img, pos = self.draw_centered_text(instruction, 'medium', WHITE, 300 + i * 40)
            screen.blit(img, pos)
        
        # Player name input field
        pygame.draw.rect(screen, WHITE, self.input_rect, 2)
        if self.player_name:
            name_img, name_pos = self.draw_text(self.player_name, 'medium', WHITE, 
                                              self.input_rect.x + 5, self.input_rect.y + 5)
            screen.blit(name_img, name_pos)
        else:
            placeholder_img, placeholder_pos = self.draw_text("Enter name...", 'medium', (128, 128, 128),
                                                           self.input_rect.x + 5, self.input_rect.y + 5)
            screen.blit(placeholder_img, placeholder_pos)

        # Quit instruction - moved below input field to avoid overlap
        quit_img, quit_pos = self.draw_centered_text("Press ESC or Q to quit", 'medium', WHITE, 500)
        screen.blit(quit_img, quit_pos)

        # Recent history
        if last_history:
            header_img, header_pos = self.draw_centered_text("Last 3 games:", 'medium', YELLOW, 620)
            screen.blit(header_img, header_pos)
            for idx, h in enumerate(last_history[-3:][::-1]):
                name = h.get('name', 'Unknown')
                score = h.get('score', 0)
                result = h.get('result', 'n/a')
                duration_ms = h.get('duration_ms', 0)
                duration_s = max(0, int(duration_ms // 1000))
                line = f"{name} - {result} - score {score} - {duration_s}s"
                img, pos = self.draw_centered_text(line, 'small', WHITE, 660 + idx * 24)
                screen.blit(img, pos)
    
    def draw_game_over_screen(self, screen, score, player_name):
        """Draw the game over screen with final score"""
        # Game over text
        game_over_img, game_over_pos = self.draw_centered_text("GAME OVER!", 'large', RED, 200)
        screen.blit(game_over_img, game_over_pos)
        
        # Player name and score
        score_text = f"Player: {player_name}"
        score_img, score_pos = self.draw_centered_text(score_text, 'medium', WHITE, 300)
        screen.blit(score_img, score_pos)
        
        final_score_text = f"Final Score: {score}"
        final_score_img, final_score_pos = self.draw_centered_text(final_score_text, 'medium', YELLOW, 350)
        screen.blit(final_score_img, final_score_pos)
        
        # Instructions
        restart_img, restart_pos = self.draw_centered_text("Press R to restart", 'medium', WHITE, 450)
        screen.blit(restart_img, restart_pos)
        
        quit_img, quit_pos = self.draw_centered_text("Press Q to quit", 'medium', WHITE, 490)
        screen.blit(quit_img, quit_pos)
        
        # Additional quit option
        esc_quit_img, esc_quit_pos = self.draw_centered_text("Press ESC to quit", 'medium', WHITE, 530)
        screen.blit(esc_quit_img, esc_quit_pos)
    
    def draw_victory_screen(self, screen, score, player_name):
        """Draw the victory screen with final score"""
        # Victory text
        victory_img, victory_pos = self.draw_centered_text("YOU WIN!", 'large', GREEN, 200)
        screen.blit(victory_img, victory_pos)
        
        # Player name and score
        score_text = f"Player: {player_name}"
        score_img, score_pos = self.draw_centered_text(score_text, 'medium', WHITE, 300)
        screen.blit(score_img, score_pos)
        
        final_score_text = f"Final Score: {score}"
        final_score_img, final_score_pos = self.draw_centered_text(final_score_text, 'medium', YELLOW, 350)
        screen.blit(final_score_img, final_score_pos)
        
        # Instructions
        restart_img, restart_pos = self.draw_centered_text("Press R to restart", 'medium', WHITE, 450)
        screen.blit(restart_img, restart_pos)
        
        quit_img, quit_pos = self.draw_centered_text("Press Q to quit", 'medium', WHITE, 490)
        screen.blit(quit_img, quit_pos)
        
        # Additional quit option
        esc_quit_img, esc_quit_pos = self.draw_centered_text("Press ESC to quit", 'medium', WHITE, 530)
        screen.blit(esc_quit_img, esc_quit_pos)
    
    def draw_hud(self, screen, score, player_name, health):
        """Draw the heads-up display during gameplay"""
        # Score
        score_text = f"Score: {score}"
        score_img, score_pos = self.draw_text(score_text, 'medium', WHITE, 10, 10)
        screen.blit(score_img, score_pos)
        
        # Player name
        name_text = f"Player: {player_name}"
        name_img, name_pos = self.draw_text(name_text, 'medium', WHITE, 10, 40)
        screen.blit(name_img, name_pos)
        
        # Health
        health_text = f"Health: {health}"
        health_img, health_pos = self.draw_text(health_text, 'medium', WHITE, 10, 70)
        screen.blit(health_img, health_pos)
        
        # Quit instruction
        quit_text = "ESC: Pause | Q: Quit"
        quit_img, quit_pos = self.draw_text(quit_text, 'small', WHITE, 10, 100)
        screen.blit(quit_img, quit_pos)
    
    def draw_countdown(self, screen, countdown):
        """Draw the countdown screen before game starts"""
        if countdown > 0:
            ready_img, ready_pos = self.draw_centered_text("GET READY!", 'large', WHITE, SCREEN_HEIGHT // 2 + 50)
            screen.blit(ready_img, ready_pos)
            
            count_img, count_pos = self.draw_centered_text(str(countdown), 'large', WHITE, SCREEN_HEIGHT // 2 + 100)
            screen.blit(count_img, count_pos)
            
            # Quit instruction during countdown
            quit_img, quit_pos = self.draw_centered_text("Press ESC or Q to quit", 'small', WHITE, SCREEN_HEIGHT // 2 + 150)
            screen.blit(quit_img, quit_pos)
    
    def handle_input_events(self, event):
        """Handle input events for player name entry"""
        if event.type == pygame.KEYDOWN:
            if self.input_active:
                if event.key == pygame.K_RETURN:
                    self.input_active = False
                    return True  # Signal to start game
                elif event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                else:
                    # Only allow letters and numbers, max 15 characters
                    if len(self.player_name) < 15 and event.unicode.isalnum():
                        self.player_name += event.unicode
            elif event.key == pygame.K_TAB:
                self.input_active = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.input_active = True
            else:
                self.input_active = False
        
        return False 