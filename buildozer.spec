[app]
# App identity
title = Space Invaders
package.name = spaceinvaders
package.domain = com.hasaki

# Sources
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,ogg,wav,mp3,ttf,txt,json
include_patterns = img/*

# Versioning
version = 0.1.0

# Android specifics
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a
android.permissions = 
android.ndk = 26b

# Python / p4a
requirements = python3, pygame, sdl2_image, sdl2_mixer, sdl2_ttf
p4a.bootstrap = sdl2

# Use latest python-for-android for improved CMake/jpeg handling
p4a.branch = develop

# Optional: icons/splash (provide files to enable)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
