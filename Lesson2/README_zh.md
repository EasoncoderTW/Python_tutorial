# 第二課：類型和物件 - 認識 Python 的數據寶可夢！🎮

## 🌟 歡迎來到數據類型的世界！

想像一下，如果數據類型是寶可夢，每一種都有自己的特殊能力和個性！在 Python 的世界裡，每個值都有自己的「屬性」，就像每隻寶可夢都有火系、水系、草系一樣。

Python 是一個**動態型別語言**，這意味著你不需要事先告訴電腦「這是什麼類型」— 它會像智能手機一樣，自動識別你輸入的是什麼！

## 🎯 Python 中的四大基本類型

### 1. Int（整數）- 數學系寶可夢 🔢

整數就像是完美的計數器，沒有小數點，乾淨俐落！

```python
# 整數的例子
my_age = 16
game_score = 9999
temperature = -5
followers = 1000

print(f"我今年 {my_age} 歲")
print(f"我的遊戲分數是 {game_score}")
print(f"今天溫度是 {temperature}°C")
print(f"我有 {followers} 個粉絲！")
```

**整數的超能力：**
- ➕ 可以做所有數學運算
- 🎯 精確，不會有小數誤差
- 💾 占用記憶體相對較少

### 2. Float（浮點數）- 精密系寶可夢 🎯

浮點數就像是精密的測量工具，可以表示小數！

```python
# 浮點數的例子
height = 165.5
pi = 3.14159
money = 99.99
speed = 2.5e2  # 科學記號：250.0

print(f"我的身高是 {height} 公分")
print(f"圓周率約等於 {pi}")
print(f"這個商品要 ${money}")
print(f"光速是 {speed} 百萬公里/秒")
```

**浮點數的超能力：**
- 🎯 可以表示極大或極小的數字
- 🔬 適合科學計算
- 💰 處理金錢相關計算

### 3. Str（字串）- 文字系寶可夢 📝

字串就像是會說話的寶可夢，可以包含任何文字內容！

```python
# 字串的例子
username = "超級玩家123"
message = '今天天氣真好！'
emoji_text = "🎮💻🚀⭐"
song_lyrics = """
    我是一隻程式碼小白
    每天都在學習新技能
    Python 是我最好的朋友
"""

print(f"使用者名稱：{username}")
print(f"今日訊息：{message}")
print(f"表情符號：{emoji_text}")
print(f"歌詞：{song_lyrics}")
```

**字串的超能力：**
- 🎨 可以包含任何字符（文字、數字、符號、表情符號）
- 🔤 可以用單引號、雙引號、三引號包圍
- 🎭 可以模擬對話和故事

### 4. Bool（布林值）- 邏輯系寶可夢 ⚡

布林值是最簡單卻最重要的類型，只有兩個值：True（真）和 False（假）

```python
# 布林值的例子
is_student = True
homework_done = False
game_over = True
weekend = False

print(f"是學生嗎？{is_student}")
print(f"作業做完了嗎？{homework_done}")
print(f"遊戲結束了嗎？{game_over}")
print(f"現在是週末嗎？{weekend}")
```

**布林值的超能力：**
- 🔀 控制程式流程（if/else）
- 🎯 做決策和判斷
- 🔍 比較和邏輯運算

## 🔍 型別檢查器 - 你的數據偵探

使用 `type()` 函數來檢查任何值的類型：

```python
# 類型檢查實戰
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# 檢查變數的類型
my_score = 95
print(f"my_score 的類型是：{type(my_score)}")

user_input = input("請輸入任何東西：")
print(f"你輸入的內容類型是：{type(user_input)}")  # 提示：總是 str！
```

## 🔄 型別轉換 - 數據變身術

有時候我們需要讓數據「變身」成另一種類型，就像寶可夢進化一樣！

### 轉換函數大全：
```python
# 型別轉換示範
original_number = 3.14
age_str = "18"
money_str = "99.99"
zero_value = 0

# 轉換成整數
print(f"3.14 轉成整數：{int(original_number)}")        # 3
print(f"'18' 轉成整數：{int(age_str)}")                # 18

# 轉換成浮點數
print(f"18 轉成浮點數：{float(18)}")                   # 18.0
print(f"'99.99' 轉成浮點數：{float(money_str)}")       # 99.99

# 轉換成字串
print(f"123 轉成字串：'{str(123)}'")                   # '123'
print(f"3.14 轉成字串：'{str(3.14)}'")                 # '3.14'

# 轉換成布林值（特別有趣！）
print(f"1 轉成布林值：{bool(1)}")                      # True
print(f"0 轉成布林值：{bool(0)}")                      # False
print(f"'Hello' 轉成布林值：{bool('Hello')}")          # True
print(f"'' 轉成布林值：{bool('')}")                    # False
```

### 💡 布林值轉換的秘密規則：
```python
# 這些值轉換成布林值時會變成 False：
print(bool(0))          # False - 數字零
print(bool(0.0))        # False - 浮點數零
print(bool(""))         # False - 空字串
print(bool(None))       # False - 空值

# 其他所有值都會變成 True：
print(bool(1))          # True
print(bool(-1))         # True
print(bool("0"))        # True（注意：這是字串！）
print(bool("False"))    # True（注意：這也是字串！）
```

## 🎮 實戰練習：個人資料處理器

讓我們創建一個有趣的個人資料處理程式：

```python
print("🎮 歡迎來到個人資料處理器！")
print("=" * 40)

# 收集資料
name = input("你的暱稱是什麼？")
age_str = input("你幾歲了？")
height_str = input("你的身高是多少公分？")
is_gamer = input("你喜歡玩遊戲嗎？(yes/no)")

# 型別轉換
age = int(age_str)
height = float(height_str)
likes_gaming = is_gamer.lower() == "yes"

# 資料分析
is_teenager = 13 <= age <= 19
is_tall = height > 170
next_year_age = age + 1

# 顯示結果
print(f"\n🎉 {name} 的個人檔案分析完成！")
print(f"📊 年齡：{age} 歲（類型：{type(age).__name__}）")
print(f"📏 身高：{height} 公分（類型：{type(height).__name__}）")
print(f"🎮 喜歡遊戲：{likes_gaming}（類型：{type(likes_gaming).__name__}）")
print(f"🧒 是青少年：{is_teenager}")
print(f"🏀 算高個子：{is_tall}")
print(f"🎂 明年就 {next_year_age} 歲了！")
```

## 🧩 挑戰任務：數據類型大師

### 任務 1：類型偵探
```python
# 請預測以下變數的類型，然後用程式驗證：
mystery_1 = 42
mystery_2 = "42"
mystery_3 = 4.2
mystery_4 = True
mystery_5 = "True"

# 你的預測：
# mystery_1 是 _____ 類型
# mystery_2 是 _____ 類型
# mystery_3 是 _____ 類型
# mystery_4 是 _____ 類型
# mystery_5 是 _____ 類型

# 驗證答案：
print(f"mystery_1 的類型：{type(mystery_1)}")
print(f"mystery_2 的類型：{type(mystery_2)}")
print(f"mystery_3 的類型：{type(mystery_3)}")
print(f"mystery_4 的類型：{type(mystery_4)}")
print(f"mystery_5 的類型：{type(mystery_5)}")
```

### 任務 2：型別轉換大挑戰
```python
# 完成以下轉換，並處理可能的錯誤：
test_values = ["123", "45.67", "True", "0", ""]

for value in test_values:
    print(f"\n原始值：'{value}'（類型：{type(value).__name__}）")

    # 嘗試轉換成不同類型
    try:
        print(f"轉成整數：{int(value)}")
    except ValueError:
        print("轉成整數：❌ 失敗")

    try:
        print(f"轉成浮點數：{float(value)}")
    except ValueError:
        print("轉成浮點數：❌ 失敗")

    print(f"轉成布林值：{bool(value)}")
```

## 🌟 本課重點回顧

- ✅ **int（整數）**：沒有小數點的數字，適合計數
- ✅ **float（浮點數）**：有小數點的數字，適合精密計算
- ✅ **str（字串）**：文字內容，用引號包圍
- ✅ **bool（布林值）**：只有 True 或 False
- ✅ **type()** 函數：檢查數據類型的偵探
- ✅ **型別轉換**：int(), float(), str(), bool() 讓數據變身

## 💡 生活應用場景

學會數據類型可以讓你：
- 🎮 製作遊戲計分系統（int）
- 💰 處理購物車價格計算（float）
- 💬 設計聊天機器人（str）
- 🔍 建立智能判斷系統（bool）

## 🚀 下一課預告

接下來我們要學習**算術運算**- 讓你的程式變成超級計算機！準備好用 Python 解決各種數學問題了嗎？🔥