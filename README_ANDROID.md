# 🚀 Space Invaders - Android Build Guide

## 📱 **Chuyển đổi từ Pygame sang Kivy cho Android**

### **1. Cài đặt môi trường**

```bash
# Cài đặt Kivy và buildozer
pip install kivy buildozer

# Cài đặt các dependencies
pip install -r requirements.txt
```

### **2. Cấu trúc file đã thay đổi**

- ✅ `main.py` - Phiên bản Kivy (thay thế pygame)
- ✅ `buildozer.spec` - Cấu hình build Android
- ✅ `requirements.txt` - Dependencies cho Kivy

### **3. Các thay đổi chính**

#### **Từ Pygame sang Kivy:**
- **Graphics**: `pygame.draw` → `kivy.graphics`
- **Events**: `pygame.event` → `kivy.touch`
- **Audio**: `pygame.mixer` → `kivy.core.audio`
- **UI**: Custom drawing → `kivy.uix` widgets

#### **Touch Controls:**
- **Di chuyển**: Vuốt trái/phải màn hình
- **Bắn**: Chạm vào màn hình
- **Menu**: Nút bấm thay vì phím

### **4. Build Android APK**

#### **Bước 1: Chuẩn bị môi trường Linux/WSL**
```bash
# Cài đặt dependencies
sudo apt update
sudo apt install -y python3 python3-pip git zip unzip openjdk-8-jdk python3-virtualenv

# Cài đặt Android SDK và NDK
sudo apt install -y android-sdk android-ndk
```

#### **Bước 2: Build APK**
```bash
# Khởi tạo buildozer (nếu chưa có)
buildozer init

# Build APK
buildozer android debug

# Hoặc build release
buildozer android release
```

### **5. Cấu hình buildozer.spec**

File `buildozer.spec` đã được tối ưu với:

```ini
[app]
title = Space Invaders
package.name = spaceinvaders
package.domain = org.spaceinvaders
version = 1.0

requirements = python3,kivy,pillow

android.api = 28
android.minapi = 21
android.arch = armeabi-v7a arm64-v8a
```

### **6. Chạy trên Android**

#### **Cài đặt APK:**
1. Copy file `.apk` vào thiết bị Android
2. Bật "Install from unknown sources"
3. Cài đặt APK
4. Chạy game!

#### **Controls:**
- **Di chuyển**: Vuốt trái/phải
- **Bắn**: Chạm màn hình
- **Menu**: Sử dụng nút bấm

### **7. Troubleshooting**

#### **Lỗi thường gặp:**
```bash
# Lỗi Java version
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Lỗi Android SDK
export ANDROID_HOME=/usr/lib/android-sdk

# Lỗi NDK
export ANDROID_NDK_HOME=/usr/lib/android-ndk
```

#### **Kiểm tra log:**
```bash
buildozer android debug deploy run logcat
```

### **8. Tối ưu hóa**

#### **Performance:**
- Giảm FPS xuống 30 cho thiết bị yếu
- Sử dụng `kivy.graphics` thay vì `kivy.uix`
- Tối ưu collision detection

#### **Memory:**
- Giới hạn số lượng bullets/explosions
- Sử dụng object pooling
- Cleanup resources thường xuyên

### **9. Phát hành**

#### **Build release:**
```bash
buildozer android release
```

#### **Sign APK:**
```bash
# Tạo keystore
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

# Sign APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore app-release-unsigned.apk alias_name
```

### **10. Kết quả**

🎮 **Game Space Invaders hoàn toàn tương thích với Android!**

- ✅ Touch controls
- ✅ Responsive UI
- ✅ Cross-platform
- ✅ APK ready
- ✅ Performance optimized

### **11. Liên kết hữu ích**

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Guide](https://buildozer.readthedocs.io/)
- [Android Development](https://developer.android.com/)
- [Python for Android](https://python-for-android.readthedocs.io/)

---

**🎯 Mục tiêu đã đạt được: Chuyển đổi thành công từ Pygame sang Kivy để build Android app!** 