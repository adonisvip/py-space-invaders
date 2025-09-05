# Space Invaders

A modern Python implementation of the classic Space Invaders arcade game built with Pygame. This project features a modular architecture, player name input, score tracking, and both desktop and mobile (Android) support.

## 🎮 Features

- **Classic Gameplay**: Defend Earth from invading aliens in this timeless arcade shooter
- **Player Personalization**: Enter your name and track your high scores
- **Score System**: Earn points by destroying aliens (10 points per alien)
- **Health System**: 3-hit health system with visual health bar
- **Sound Effects**: Immersive audio with laser shots and explosion sounds
- **Game History**: Track your last 3 games with scores and duration
- **Multiple Game States**: Menu, gameplay, victory, and game over screens
- **Pause System**: Pause and resume functionality during gameplay
- **Desktop Game**: Optimized for desktop gameplay

## 🎯 Game Controls

### Desktop Controls
- **Arrow Keys**: Move spaceship left/right
- **Spacebar**: Shoot laser
- **ESC**: Pause game / Return to menu
- **Q**: Quick quit
- **Tab**: Activate name input field
- **Enter**: Start game / Confirm name
- **R**: Restart after game over
- **Y/N**: Confirm quit dialog


## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Pygame 2.0.0 or higher

### Desktop Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd py-space-invaders
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python main.py
   ```


## 📁 Project Structure

```
py-space-invaders/
├── main.py              # Main game entry point
├── config.py            # Game configuration and constants
├── game_manager.py      # Game state and logic management
├── sprites.py           # All sprite classes (player, aliens, bullets, explosions)
├── ui_manager.py        # User interface and text rendering
├── requirements.txt     # Python dependencies
├── history.json        # Game history storage (auto-generated)
└── img/                # Game assets
    ├── spaceship.png   # Player spaceship
    ├── alien1-5.png    # Alien sprites (5 variants)
    ├── bullet.png      # Player bullet
    ├── alien_bullet.png # Alien bullet
    ├── exp1-5.png      # Explosion animation frames
    ├── bg.png          # Background image
    ├── explosion.wav   # Explosion sound effect
    ├── explosion2.wav  # Spaceship hit sound
    └── laser.wav       # Laser shot sound
```

## 🏗️ Architecture

The game uses a modular architecture with clear separation of concerns:

- **`main.py`**: Main game loop and event handling
- **`config.py`**: All game constants, settings, and configuration
- **`game_manager.py`**: Game state management, scoring, and sprite coordination
- **`sprites.py`**: All game objects (Spaceship, Aliens, Bullets, Explosions)
- **`ui_manager.py`**: User interface rendering and input handling

### Key Classes

- **`SpaceInvadersGame`**: Main game orchestrator
- **`GameManager`**: Handles game logic, scoring, and state transitions
- **`UIManager`**: Manages all UI elements and text rendering
- **`Spaceship`**: Player-controlled spaceship with health system
- **`Aliens`**: Enemy aliens with movement patterns
- **`Bullets`**: Projectile system for both player and aliens
- **`Explosion`**: Animated explosion effects

## 🎮 Gameplay

1. **Start Screen**: Enter your name and press Enter to begin
2. **Countdown**: 3-second countdown before gameplay starts
3. **Gameplay**: 
   - Move with arrow keys
   - Shoot with spacebar
   - Destroy all aliens to win
   - Avoid alien bullets to survive
4. **Scoring**: Earn 10 points for each alien destroyed
5. **Health**: Start with 3 health points, lose 1 when hit by alien bullets
6. **Game Over**: Lose when health reaches 0
7. **Victory**: Win when all aliens are destroyed

## ⚙️ Configuration

Game settings can be modified in `config.py`:

- **Screen dimensions**: 600x800 pixels
- **FPS**: 60 frames per second
- **Alien formation**: 5x5 grid
- **Player health**: 3 hits
- **Bullet speeds**: Player (5), Alien (2)
- **Cooldowns**: Player (500ms), Alien (1000ms)

## 🔧 Development

### Adding New Features

1. **New sprites**: Add classes to `sprites.py`
2. **UI elements**: Extend `UIManager` class
3. **Game logic**: Modify `GameManager` class
4. **Configuration**: Update `config.py`

### Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to all classes and methods
- Keep functions focused on single responsibilities

## 🐛 Troubleshooting

### Common Issues

1. **Sound not playing**: Check if audio files exist in `img/` directory
2. **Images not loading**: Verify all image files are present in `img/` directory
3. **Game crashes on start**: Check Python and Pygame versions

### Dependencies

- **Pygame**: Core game engine


## 🎯 Future Enhancements

Potential improvements for future versions:

- Power-ups and special weapons
- Multiple difficulty levels
- High score leaderboard
- Multiplayer support
- More alien types and movement patterns
- Particle effects and improved graphics
- Level progression system

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the project repository.

---

**Enjoy defending Earth from the alien invasion!** 🚀👾
