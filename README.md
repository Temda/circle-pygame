# Circle Pygame - เกมต่อสู้กับซอมบี้

[English version below](#english)

## 🎮 เกี่ยวกับเกม
เกม Circle Pygame เป็นเกมที่ผู้เล่นจะต้องควบคุมตัวละครในการต่อสู้กับซอมบี้ โดยใช้ดาบที่โคจรรอบตัวละครในการโจมตี

## 🚀 คุณสมบัติ
- ระบบการเคลื่อนที่แบบฟิสิกส์
- ระบบดาบโคจรรอบตัวละคร
- ระบบซอมบี้ที่ไล่ตามผู้เล่น
- ระบบเก็บไอเทมเพื่อเพิ่มพลัง
- ระบบคะแนนและการนับจำนวนซอมบี้ที่ฆ่า

## 🎯 วิธีการเล่น
1. ใช้ปุ่มลูกศร (↑, ↓, ←, →) เพื่อเคลื่อนที่
2. เก็บดาบพลัง (Power Sword) เพื่อเพิ่มจำนวนดาบที่โคจร
3. ใช้ดาบที่โคจรในการฆ่าซอมบี้
4. หลีกเลี่ยงการถูกซอมบี้แตะ
5. กด R เพื่อเริ่มเกมใหม่เมื่อตาย

## 🛠️ การติดตั้ง
1. ติดตั้ง Python 3.x
2. ติดตั้ง Pygame:
```bash
pip install pygame
```
3. รันเกม:
```bash
python main.py
```

## 📦 โครงสร้างไฟล์
```
circle-pygame/
├── main.py          # ไฟล์หลักของเกม
├── game.py          # คลาสจัดการเกม
├── entities.py      # คลาสตัวละครและซอมบี้
├── assets.py        # จัดการรูปภาพและเสียง
└── config.py        # การตั้งค่าต่างๆ
```

## 🎨 ทรัพยากรที่ใช้
- ตัวละคร: anime.gif
- ดาบ: fire-sword.gif
- ดาบพลัง: power_sword.png
- ดาบพลังอัพเกรด: power_sword_update.png
- ซอมบี้: zombie.gif
- เพลง: powers.mp3

---

# Circle Pygame - Zombie Fighting Game

## 🎮 About
Circle Pygame is a game where players control a character fighting against zombies using orbiting swords.

## 🚀 Features
- Physics-based movement system
- Orbiting swords system
- Zombie AI that chases the player
- Power-up collection system
- Score and kill count system

## 🎯 How to Play
1. Use arrow keys (↑, ↓, ←, →) to move
2. Collect Power Swords to increase orbiting swords
3. Use orbiting swords to kill zombies
4. Avoid being touched by zombies
5. Press R to restart when dead

## 🛠️ Installation
1. Install Python 3.x
2. Install Pygame:
```bash
pip install pygame
```
3. Run the game:
```bash
python main.py
```

## 📦 File Structure
```
circle-pygame/
├── main.py          # Main game file
├── game.py          # Game management class
├── entities.py      # Character and zombie classes
├── assets.py        # Image and sound management
└── config.py        # Game configuration
```

## 🎨 Assets Used
- Character: anime.gif
- Sword: fire-sword.gif
- Power Sword: power_sword.png
- Upgraded Power Sword: power_sword_update.png
- Zombie: zombie.gif
- Music: powers.mp3
