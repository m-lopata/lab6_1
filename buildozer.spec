[app]
# Назва вашого додатка
title = Triangle Area

# Унікальне ім'я пакету (без великих літер і пробілів)
package.name = trianglearea
package.domain = org.example

# Версія додатка
version = 1.0

# Головний файл програми
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = tests,bin

# Сторонні бібліотеки, які використовує ваш додаток
requirements = python3,kivy

# Орієнтація екрана
orientation = portrait

# Дозволи для Android
android.permissions = INTERNET

# Іконки та заставка
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Вкажіть Android API рівень
android.api = 31
android.minapi = 21

# Target Android SDK
android.sdk = 31

# Архітектури для підтримки
android.archs = armeabi-v7a,arm64-v8a

# Python версія
python3 = True

[buildozer]
log_level = 2
warn_on_root = 1
