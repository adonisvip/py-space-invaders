[app]
title = Space Invaders
package.name = spaceinvaders
package.domain = org.spaceinvaders
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

android.arch = armeabi-v7a arm64-v8a

android.api = 28
android.minapi = 21
android.sdk = 28
android.ndk = 19b

android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
