# 第四課：Python的決策超能力！ 🤖🧠

歡迎來到智能程式設計的世界！今天我們要學習如何讓Python思考和做決定，就像你每天做的一樣！🎯

## 為什麼程式需要做決定？ 🤔

想想你的日常生活：
- "我該帶雨傘嗎？"（檢查是否下雨）
- "我能買這個遊戲嗎？"（檢查你有沒有足夠的錢）
- "我年齡夠看這部電影嗎？"（檢查你的年齡）

Python也能做這些決定！讓我們給你的程式一些腦力！🧠

## 決策三人組：if、elif、else 🎭

### if 敘述：守門員 🚪
`if` 敘述就像俱樂部的保鑣 - 只有當條件為真時，才讓程式碼通過！

```python
# 遊戲例子：你可以升級嗎？
player_experience = 1500
required_exp = 1000

if player_experience >= required_exp:
    print("🎉 恭喜！你升級了！")
    print("新技能解鎖！ 🔓")

# 社群媒體例子：你可以發文嗎？
followers = 250
if followers >= 100:
    print("✨ 你現在可以發限時動態了！")
    print("你的影響力正在增長！ 📈")
```

### elif 敘述：選擇題大師 📝
`elif` (else if) 就像多選題 - 它檢查不同的可能性！

```python
# 有個性的成績檢查器！
test_score = 87

if test_score >= 90:
    print("🏆 太棒了！你是超級巨星！")
elif test_score >= 80:
    print("👍 做得好！你很厲害！")
elif test_score >= 70:
    print("😊 不錯的表現！繼續保持！")
elif test_score >= 60:
    print("😐 還可以，但你可以做得更好！")
else:
    print("😢 糟糕！該更用功讀書了！")

# 遊戲難度選擇器
player_level = 15

if player_level >= 50:
    difficulty = "傳奇 🔥"
elif player_level >= 30:
    difficulty = "專家 💪"
elif player_level >= 15:
    difficulty = "中等 🎯"
elif player_level >= 5:
    difficulty = "初學者 🌱"
else:
    difficulty = "新手 🐣"

print(f"建議難度：{difficulty}")
```

### else 敘述：安全網 🛡️
`else` 就像你的備用計劃 - 它捕獲所有不符合其他條件的情況！

```python
# 天氣服裝選擇器
temperature = 25  # 攝氏度

if temperature > 30:
    print("🌞 很熱！穿短褲和T恤！")
elif temperature > 20:
    print("😎 完美天氣！穿什麼都可以！")
elif temperature > 10:
    print("🧥 有點涼，拿件輕外套！")
else:
    print("🧤 好冷！穿暖和的衣服！")
```

## 比較運算子：裁判 ⚖️

這些運算子幫助Python比較值並做決定！

```python
# 社群媒體比較
my_followers = 150
friend_followers = 120

print(f"我的追蹤者比較多嗎？ {my_followers > friend_followers}")  # True
print(f"我們有相同的追蹤者嗎？ {my_followers == friend_followers}")  # False
print(f"我的追蹤者比較少嗎？ {my_followers < friend_followers}")  # False

# 遊戲統計比較
my_score = 9500
high_score = 10000

print(f"我打破高分了嗎？ {my_score > high_score}")  # False
print(f"我接近高分了嗎？ {my_score >= (high_score - 1000)}")  # True
print(f"我需要改進嗎？ {my_score != high_score}")  # True
```

## 邏輯運算子：組合器 🔗

這些幫助你組合多個條件 - 就像同時問多個問題！

### AND (&)：完美主義者 🎯
兩個條件都必須為真！

```python
# 你可以開車嗎？
age = 17
has_license = True

if age >= 16 and has_license:
    print("🚗 你可以開車！注意安全！")
else:
    print("🚫 抱歉，你還不能開車！")

# 遊戲：你可以進入VIP區域嗎？
player_level = 25
has_premium = True
is_member = True

if player_level >= 20 and has_premium and is_member:
    print("✨ 歡迎來到VIP區域！享受獨家內容！")
else:
    print("🔒 VIP存取被拒絕。檢查你的資格！")
```

### OR (|)：靈活的朋友 🤝
至少一個條件必須為真！

```python
# 你可以得到折扣嗎？
is_student = False
is_senior = False
is_member = True

if is_student or is_senior or is_member:
    print("🎊 你可以得到20%折扣！")
else:
    print("😔 沒有折扣可用，但謝謝光臨！")

# 遊戲：你可以使用這個功能嗎？
has_premium = False
reached_level_50 = True
completed_tutorial = True

if has_premium or reached_level_50 or completed_tutorial:
    print("🎮 功能解鎖！玩得開心！")
else:
    print("🔒 完成教學或升級到進階版！")
```

### NOT (!)：相反日 🔄
把真變假，把假變真！

```python
# 安全檢查
is_banned = False
is_suspicious = False

if not is_banned and not is_suspicious:
    print("✅ 存取許可！歡迎！")
else:
    print("⛔ 基於安全原因拒絕存取！")

# 遊戲：你準備好魔王戰了嗎？
is_injured = True
has_enough_ammo = True

if not is_injured and has_enough_ammo:
    print("⚔️ 準備戰鬥！來打魔王！")
else:
    print("🏥 在大戰前先治療並補充彈藥！")
```

## 嵌套條件：決策樹 🌳

有時你需要在決策中做決策！

```python
# 電影推薦系統
age = 16
likes_action = True
likes_comedy = False

if age >= 13:
    if likes_action:
        if age >= 17:
            print("🎬 看《動作英雄R級》！")
        else:
            print("🎬 看《青少年動作冒險》！")
    elif likes_comedy:
        print("🎬 看《搞笑高中》！")
    else:
        print("🎬 看《熱門青少年劇情片》！")
else:
    print("🎬 看《家庭歡樂冒險》！")

# 遊戲：角色職業選擇器
strength = 8
intelligence = 6
agility = 9

if strength >= 7:
    if agility >= 8:
        character_class = "🗡️ 聖騎士 - 強壯且快速！"
    else:
        character_class = "🛡️ 戰士 - 純力量！"
elif intelligence >= 7:
    if agility >= 8:
        character_class = "🏹 遊俠 - 聰明且敏捷！"
    else:
        character_class = "🔮 法師 - 魔法大師！"
else:
    character_class = "🗡️ 盜賊 - 快速且隱密！"

print(f"你的角色職業：{character_class}")
```

## 史詩挑戰 - 提升你的技能！ 🚀

### 挑戰1：密碼強度檢查器 🔐
創建一個程式檢查密碼是否對遊戲帳戶足夠強！

```python
# 挑戰1：你的解答在這裡！
password = "SuperGamer123!"
length = len(password)
has_number = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_special = any(char in "!@#$%^&*" for char in password)

if length >= 12 and has_number and has_uppercase and has_special:
    print("🔒 超強！你的帳戶像諾克斯堡一樣安全！")
elif length >= 8 and has_number and has_uppercase:
    print("🔐 強！你的帳戶有良好保護！")
elif length >= 6 and has_number:
    print("🔑 中等！考慮添加大寫字母和特殊字符！")
else:
    print("🚫 弱！你的帳戶容易被駭客攻擊！")
```

### 挑戰2：遊戲商店結帳 🛒
計算含折扣和稅金的總價！

```python
# 挑戰2：你的解答在這裡！
game_price = 59.99
dlc_price = 19.99
is_member = True
is_student = False
student_discount = 0.10  # 10%
member_discount = 0.05   # 5%
tax_rate = 0.08          # 8%

total = game_price + dlc_price

if is_student:
    total = total * (1 - student_discount)
    print(f"💰 學生折扣已套用！省下 ${(game_price + dlc_price) * student_discount:.2f}")
elif is_member:
    total = total * (1 - member_discount)
    print(f"💰 會員折扣已套用！省下 ${(game_price + dlc_price) * member_discount:.2f}")

total_with_tax = total * (1 + tax_rate)
print(f"🎮 最終總額：${total_with_tax:.2f}")
```

### 挑戰3：社群媒體情緒偵測器 📱
分析社群媒體貼文並判斷情緒！

```python
# 挑戰3：你的解答在這裡！
post_text = "我對新遊戲發布超級興奮！等不及要和朋友一起玩了！ 🎮🎉"
likes = 50
comments = 15

has_positive_words = any(word in post_text for word in ["興奮", "開心", "愛", "棒", "好"])
has_negative_words = any(word in post_text for word in ["傷心", "生氣", "恨", "糟糕", "awful"])
has_emojis = any(emoji in post_text for emoji in ["😊", "😍", "🎉", "❤️", "😢", "😡"])

if has_positive_words and likes > 20:
    if has_emojis:
        mood = "🌟 超級正面！這篇貼文散發好氣息！"
    else:
        mood = "😊 正面！大家都喜歡這篇！"
elif has_negative_words or likes < 5:
    mood = "😔 負面！這篇貼文可能需要一些支持！"
else:
    mood = "😐 中性！相當標準的貼文！"

print(f"貼文情緒分析：{mood}")
```

### 挑戰4：遊戲錦標賽等級 🏆
根據玩家統計資料決定錦標賽位置！

```python
# 挑戰4：你的解答在這裡！
wins = 25
losses = 8
kill_death_ratio = 2.3
team_player_rating = 8.5  # 滿分10分

win_rate = wins / (wins + losses)

if win_rate >= 0.8 and kill_death_ratio >= 2.0 and team_player_rating >= 8.0:
    bracket = "🏆 冠軍級 - 你準備好參加錦標賽了！"
elif win_rate >= 0.7 and kill_death_ratio >= 1.5:
    bracket = "💎 鑽石級 - 幾乎到頂了！"
elif win_rate >= 0.6 and kill_death_ratio >= 1.0:
    bracket = "🥇 黃金級 - 穩定的表現！"
elif win_rate >= 0.5:
    bracket = "🥈 白銀級 - 持續改進！"
else:
    bracket = "🥉 青銅級 - 熟能生巧！"

print(f"錦標賽等級：{bracket}")
print(f"勝率：{win_rate:.1%}")
```

## 決策大師的專業建議！ 🎯

1. **保持簡單** - 不要讓你的條件太複雜
2. **使用有意義的變數名稱** - `is_student` 比 `s` 好
3. **測試極端情況** - 極端值會發生什麼？
4. **使用括號** - 讓複雜條件清楚：`(a and b) or (c and d)`
5. **考慮順序** - 把最可能的條件放在前面以獲得更好的效能

## 現實世界應用 🌍

這些條件敘述無處不在：
- **遊戲**：角色能力、等級進展、傷害計算
- **應用程式**：使用者權限、功能存取、通知
- **網站**：登入系統、購物車、內容篩選
- **人工智慧**：決策樹、聊天機器人、推薦系統

你不只是在學Python - 你在學習如何製作能對周圍世界反應的智慧、回應式程式！🚀

掌握這些概念，你就能創建像你一樣會思考、決定和回應的程式！🧠✨