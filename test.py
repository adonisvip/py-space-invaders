"""
Test script for the optimized Space Invaders game
Verifies that all modules can be imported and basic functionality works
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported successfully"""
    print("Testing module imports...")
    
    try:
        # Test config import
        from config import *
        print("✅ config.py imported successfully")
        
        # Test UI manager import
        from ui_manager import UIManager
        print("✅ ui_manager.py imported successfully")
        
        # Test sprites import
        from sprites import Spaceship, Aliens, Bullets, Alien_Bullets, Explosion
        print("✅ sprites.py imported successfully")
        
        # Test game manager import
        from game_manager import GameManager
        print("✅ game_manager.py imported successfully")
        
        print("\n🎉 All modules imported successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality of the modules"""
    print("\nTesting basic functionality...")
    
    try:
        # Test config constants
        from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
        assert SCREEN_WIDTH == 600, "Screen width should be 600"
        assert SCREEN_HEIGHT == 800, "Screen height should be 800"
        assert FPS == 60, "FPS should be 60"
        print("✅ Config constants are correct")
        
        # Test UI manager initialization
        from ui_manager import UIManager
        ui = UIManager()
        assert ui.player_name == "", "Player name should be empty initially"
        print("✅ UI manager initialized successfully")
        
        # Test game manager initialization
        from game_manager import GameManager
        gm = GameManager()
        assert gm.game_state == 'menu', "Game state should be 'menu' initially"
        assert gm.score == 0, "Score should be 0 initially"
        print("✅ Game manager initialized successfully")
        
        print("\n🎉 Basic functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

def check_assets():
    """Check if required assets exist"""
    print("\nChecking required assets...")
    
    required_files = [
        "img/bg.png",
        "img/spaceship.png",
        "img/bullet.png",
        "img/alien_bullet.png",
        "img/explosion.wav",
        "img/explosion2.wav",
        "img/laser.wav"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"⚠️  Missing files: {missing_files}")
        print("The game will still run but may have missing graphics/sounds")
    else:
        print("✅ All required assets found")
    
    return len(missing_files) == 0

def main():
    """Run all tests"""
    print("🧪 Testing Optimized Space Invaders Game")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test functionality
    functionality_ok = test_basic_functionality()
    
    # Check assets
    assets_ok = check_assets()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print(f"Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"Functionality: {'✅ PASS' if functionality_ok else '❌ FAIL'}")
    print(f"Assets: {'✅ PASS' if assets_ok else '⚠️  WARNING'}")
    
    if imports_ok and functionality_ok:
        print("\n🎉 All tests passed! The optimized game is ready to run.")
        print("Run 'python main_optimized.py' to start the game.")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
    
    return imports_ok and functionality_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 