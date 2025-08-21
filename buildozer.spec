[app]
title = Space Invaders
package.name = spaceinvaders
package.domain = org.spaceinvaders
source.dir = .
source.main = main-adroid.py
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,pillow,cython

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Fixed architecture configuration
android.archs = armeabi-v7a arm64-v8a

# Fixed API configuration
android.api = 33
android.minapi = 21

# Remove deprecated android.sdk
# android.sdk = 28

android.ndk = 25b

android.private_storage = True
android.accept_sdk_license = True

# Cython configuration
p4a.bootstrap = sdl2
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
