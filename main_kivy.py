#!/usr/bin/env python3
"""
Space Invaders - Kivy Version for Android
Main game file using Kivy framework for cross-platform compatibility.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import json
import os

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
PLAYER_SPEED = 8
BULLET_SPEED = 5
ALIEN_SPEED = 1
ALIEN_ROWS = 5
ALIEN_COLS = 5

class GameScreen(Screen):
    """Main game screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_widget = GameWidget()
        self.add_widget(self.game_widget)

class MenuScreen(Screen):
    """Main menu screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title
        title = Label(
            text='SPACE INVADERS',
            font_size='48sp',
            size_hint=(1, 0.3)
        )
        self.layout.add_widget(title)
        
        # Instructions
        instructions = [
            'Enter your name:',
            'Use ARROW KEYS to move',
            'Press SPACE to shoot',
            'Press ESC to quit'
        ]
        
        for instruction in instructions:
            label = Label(
                text=instruction,
                font_size='24sp',
                size_hint=(1, 0.1)
            )
            self.layout.add_widget(label)
        
        # Name input
        self.name_input = TextInput(
            text='',
            multiline=False,
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5}
        )
        self.layout.add_widget(self.name_input)
        
        # Start button
        start_btn = Button(
            text='START GAME',
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5},
            on_press=self.start_game
        )
        self.layout.add_widget(start_btn)
        
        # Quit button
        quit_btn = Button(
            text='QUIT',
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5},
            on_press=self.quit_game
        )
        self.layout.add_widget(quit_btn)
        
        self.add_widget(self.layout)
    
    def start_game(self, instance):
        if self.name_input.text.strip():
            self.manager.current = 'game'
            self.manager.get_screen('game').game_widget.start_game(self.name_input.text)
    
    def quit_game(self, instance):
        App.get_running_app().stop()

class GameOverScreen(Screen):
    """Game over screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Game over text
        game_over = Label(
            text='GAME OVER!',
            font_size='48sp',
            size_hint=(1, 0.3)
        )
        self.layout.add_widget(game_over)
        
        # Score display
        self.score_label = Label(
            text='Score: 0',
            font_size='32sp',
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.score_label)
        
        # Buttons
        restart_btn = Button(
            text='RESTART',
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5},
            on_press=self.restart_game
        )
        self.layout.add_widget(restart_btn)
        
        menu_btn = Button(
            text='MAIN MENU',
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5},
            on_press=self.go_to_menu
        )
        self.layout.add_widget(menu_btn)
        
        self.add_widget(self.layout)
    
    def set_score(self, score):
        self.score_label.text = f'Score: {score}'
    
    def restart_game(self, instance):
        self.manager.current = 'game'
        self.manager.get_screen('game').game_widget.restart_game()
    
    def go_to_menu(self, instance):
        self.manager.current = 'menu'

class GameWidget(Widget):
    """Main game widget"""
    
    score = NumericProperty(0)
    player_health = NumericProperty(3)
    game_state = StringProperty('playing')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_name = ""
        self.player_pos = [SCREEN_WIDTH // 2, 100]
        self.bullets = []
        self.aliens = []
        self.alien_bullets = []
        self.explosions = []
        self.alien_direction = 1
        self.alien_move_timer = 0
        
        # Initialize aliens
        self.init_aliens()
        
        # Start game loop
        Clock.schedule_interval(self.update, 1.0 / FPS)
    
    def init_aliens(self):
        """Initialize alien positions"""
        self.aliens = []
        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                x = 100 + col * 80
                y = SCREEN_HEIGHT - 200 - row * 60
                self.aliens.append([x, y])
    
    def start_game(self, player_name):
        """Start a new game"""
        self.player_name = player_name
        self.score = 0
        self.player_health = 3
        self.game_state = 'playing'
        self.bullets = []
        self.alien_bullets = []
        self.explosions = []
        self.init_aliens()
    
    def restart_game(self):
        """Restart the current game"""
        self.start_game(self.player_name)
    
    def update(self, dt):
        """Main game update loop"""
        if self.game_state != 'playing':
            return
        
        # Update bullets
        self.update_bullets()
        
        # Update aliens
        self.update_aliens()
        
        # Update alien bullets
        self.update_alien_bullets()
        
        # Update explosions
        self.update_explosions()
        
        # Check collisions
        self.check_collisions()
        
        # Check game over
        self.check_game_over()
    
    def update_bullets(self):
        """Update bullet positions"""
        for bullet in self.bullets[:]:
            bullet[1] += BULLET_SPEED
            if bullet[1] > SCREEN_HEIGHT:
                self.bullets.remove(bullet)
    
    def update_aliens(self):
        """Update alien positions"""
        self.alien_move_timer += 1
        if self.alien_move_timer >= 60:  # Move every 60 frames
            self.alien_move_timer = 0
            
            # Check if aliens need to change direction
            need_direction_change = False
            for alien in self.aliens:
                if alien[0] <= 50 or alien[0] >= SCREEN_WIDTH - 50:
                    need_direction_change = True
                    break
            
            if need_direction_change:
                self.alien_direction *= -1
                # Move aliens down
                for alien in self.aliens:
                    alien[1] -= 20
            else:
                # Move aliens horizontally
                for alien in self.aliens:
                    alien[0] += ALIEN_SPEED * self.alien_direction
    
    def update_alien_bullets(self):
        """Update alien bullet positions"""
        for bullet in self.alien_bullets[:]:
            bullet[1] -= BULLET_SPEED * 0.5
            if bullet[1] < 0:
                self.alien_bullets.remove(bullet)
    
    def update_explosions(self):
        """Update explosion animations"""
        for explosion in self.explosions[:]:
            explosion[2] -= 1
            if explosion[2] <= 0:
                self.explosions.remove(explosion)
    
    def check_collisions(self):
        """Check for collisions between game objects"""
        # Player bullets vs Aliens
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                if (abs(bullet[0] - alien[0]) < 30 and 
                    abs(bullet[1] - alien[1]) < 30):
                    # Hit!
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    self.score += 100
                    self.explosions.append([alien[0], alien[1], 10])
                    break
        
        # Alien bullets vs Player
        for bullet in self.alien_bullets[:]:
            if (abs(bullet[0] - self.player_pos[0]) < 30 and 
                abs(bullet[1] - self.player_pos[1]) < 30):
                # Player hit!
                self.alien_bullets.remove(bullet)
                self.player_health -= 1
                self.explosions.append([self.player_pos[0], self.player_pos[1], 15])
    
    def check_game_over(self):
        """Check if game should end"""
        if self.player_health <= 0:
            self.game_state = 'game_over'
            self.manager.get_screen('game_over').set_score(self.score)
            self.manager.current = 'game_over'
        elif len(self.aliens) == 0:
            self.game_state = 'victory'
            self.manager.get_screen('game_over').set_score(self.score)
            self.manager.current = 'game_over'
    
    def on_touch_move(self, touch):
        """Handle touch movement for player"""
        if self.game_state == 'playing':
            # Move player based on touch position
            if touch.x < SCREEN_WIDTH // 2:
                self.player_pos[0] = max(50, self.player_pos[0] - PLAYER_SPEED)
            else:
                self.player_pos[0] = min(SCREEN_WIDTH - 50, self.player_pos[0] + PLAYER_SPEED)
    
    def on_touch_down(self, touch):
        """Handle touch input for shooting"""
        if self.game_state == 'playing':
            # Shoot bullet
            self.bullets.append([self.player_pos[0], self.player_pos[1] + 30])
    
    def draw(self):
        """Draw all game objects"""
        self.canvas.clear()
        
        with self.canvas:
            # Draw player
            Color(0, 1, 0)
            Rectangle(pos=(self.player_pos[0] - 15, self.player_pos[1] - 15), 
                     size=(30, 30))
            
            # Draw bullets
            Color(1, 1, 0)
            for bullet in self.bullets:
                Ellipse(pos=(bullet[0] - 2, bullet[1] - 2), size=(4, 4))
            
            # Draw aliens
            Color(1, 0, 0)
            for alien in self.aliens:
                Rectangle(pos=(alien[0] - 20, alien[1] - 20), size=(40, 40))
            
            # Draw alien bullets
            Color(1, 0, 1)
            for bullet in self.alien_bullets:
                Ellipse(pos=(bullet[0] - 2, bullet[1] - 2), size=(4, 4))
            
            # Draw explosions
            Color(1, 1, 1)
            for explosion in self.explosions:
                size = explosion[2] * 2
                Rectangle(pos=(explosion[0] - size//2, explosion[1] - size//2), 
                         size=(size, size))

class SpaceInvadersApp(App):
    """Main application class"""
    
    def build(self):
        """Build the application"""
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(GameOverScreen(name='game_over'))
        
        return sm

if __name__ == '__main__':
    SpaceInvadersApp().run() 