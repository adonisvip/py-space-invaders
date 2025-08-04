# Space Invaders - Installation Guide

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation Steps

### 1. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

Or install pygame directly:
```bash
pip install pygame>=2.0.0
```

### 2. Verify Installation

Run the test script to verify everything is working:
```bash
python test_optimized.py
```

You should see output like:
```
🧪 Testing Optimized Space Invaders Game
==================================================
Testing module imports...
✅ config.py imported successfully
✅ ui_manager.py imported successfully
✅ sprites.py imported successfully
✅ game_manager.py imported successfully

🎉 All modules imported successfully!

Testing basic functionality...
✅ Config constants are correct
✅ UI manager initialized successfully
✅ Game manager initialized successfully

🎉 Basic functionality tests passed!

Checking required assets...
✅ All required assets found

==================================================
📊 Test Results:
Imports: ✅ PASS
Functionality: ✅ PASS
Assets: ✅ PASS

🎉 All tests passed! The optimized game is ready to run.
Run 'python main_optimized.py' to start the game.
```

## Running the Game

### Option 1: Run the Optimized Version
```bash
python main_optimized.py
```

### Option 2: Run the Original Version
```bash
python main.py
```

## Game Controls

- **Arrow Keys**: Move spaceship left/right
- **Spacebar**: Shoot bullets
- **Enter**: Confirm player name and start game
- **R**: Restart game (on end screens)
- **Q**: Quit game (on end screens)

## Troubleshooting

### Common Issues

1. **"No module named 'pygame'"**
   ```bash
   pip install pygame
   ```

2. **"pygame.error: No available video device"**
   - This usually happens on headless servers
   - The game requires a display to run

3. **Missing assets**
   - Make sure all image and sound files are in the `img/` directory
   - The game will run with fallback graphics if some assets are missing

4. **Import errors**
   - Make sure you're running from the correct directory
   - All Python files should be in the same directory

### Performance Issues

- Close other applications to free up resources
- Update graphics drivers if experiencing lag
- Reduce FPS in `config.py` if needed

## System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.6 or higher
- **Memory**: 512MB RAM minimum
- **Graphics**: Any modern graphics card (integrated graphics work fine)
- **Storage**: 50MB free space

## Development Setup

For developers who want to modify the game:

```bash
# Install development dependencies
pip install pytest black flake8

# Run tests
python test_optimized.py

# Format code (optional)
black *.py

# Lint code (optional)
flake8 *.py
``` 