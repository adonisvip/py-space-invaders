#!/bin/bash

# 🚀 Space Invaders Android Build Script
# Tự động build APK cho Android

echo "🚀 Bắt đầu build Space Invaders cho Android..."

# Kiểm tra môi trường
echo "📋 Kiểm tra môi trường..."

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 không được cài đặt!"
    exit 1
fi

# Kiểm tra pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 không được cài đặt!"
    exit 1
fi

# Kiểm tra buildozer
if ! command -v buildozer &> /dev/null; then
    echo "📦 Cài đặt buildozer..."
    pip3 install buildozer
fi

# Kiểm tra Kivy
if ! python3 -c "import kivy" &> /dev/null; then
    echo "📦 Cài đặt Kivy..."
    pip3 install kivy
fi

echo "✅ Môi trường đã sẵn sàng!"

# Tạo thư mục build
echo "📁 Tạo thư mục build..."
mkdir -p build
cd build

# Khởi tạo buildozer nếu chưa có
if [ ! -f "buildozer.spec" ]; then
    echo "🔧 Khởi tạo buildozer..."
    buildozer init
fi

# Copy file cấu hình
echo "📋 Copy file cấu hình..."
cp ../buildozer.spec .
cp ../main.py .
cp ../requirements.txt .

# Build APK
echo "🔨 Bắt đầu build APK..."
echo "⏳ Quá trình này có thể mất 10-30 phút..."

buildozer android debug

# Kiểm tra kết quả
if [ -f "bin/*.apk" ]; then
    echo "🎉 Build thành công!"
    echo "📱 APK được tạo tại: build/bin/"
    ls -la bin/*.apk
    
    # Copy APK ra thư mục gốc
    cp bin/*.apk ../
    echo "📁 APK đã được copy vào thư mục gốc!"
else
    echo "❌ Build thất bại!"
    echo "📋 Kiểm tra log để debug:"
    echo "buildozer android debug deploy run logcat"
    exit 1
fi

echo "🎮 Space Invaders Android APK đã sẵn sàng!"
echo "📱 Cài đặt APK vào thiết bị Android để chơi!" 