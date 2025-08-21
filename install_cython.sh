#!/bin/bash

# 🔧 Script cài đặt Cython và sửa lỗi buildozer

echo "🔧 Cài đặt Cython và sửa lỗi buildozer..."

# Cài đặt Cython
echo "📦 Cài đặt Cython..."
pip install cython==0.29.33

# Kiểm tra Cython
if python -c "import cython; print('Cython version:', cython.__version__)" 2>/dev/null; then
    echo "✅ Cython đã được cài đặt thành công!"
else
    echo "❌ Cài đặt Cython thất bại!"
    exit 1
fi

# Cài đặt buildozer dependencies
echo "📦 Cài đặt buildozer dependencies..."
pip install buildozer

# Cài đặt Kivy
echo "📦 Cài đặt Kivy..."
pip install kivy

# Cài đặt Pillow
echo "📦 Cài đặt Pillow..."
pip install pillow

echo "✅ Tất cả dependencies đã được cài đặt!"
echo "🚀 Bây giờ bạn có thể chạy: buildozer android debug" 