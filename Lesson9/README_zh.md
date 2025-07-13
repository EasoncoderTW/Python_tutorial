# 第九課：Python 的檔案魔法！📁✨

歡迎來到神奇的檔案操作世界！今天我們要學習如何讓 Python 像數位巫師一樣讀取、寫入和管理檔案！🧙‍♂️

## 為什麼我們需要處理檔案？🤔

想想你的數位生活：
- 「我想保存遊戲進度！」（將資料寫入檔案）
- 「讓我看看聊天記錄！」（從檔案讀取資料）
- 「我需要備份照片！」（複製檔案）
- 「我把作業存在哪裡了？」（尋找並開啟檔案）

Python 可以處理所有這些檔案操作甚至更多！讓我們為你的程式賦予檔案超能力！🦸‍♂️

## 檔案冒險開始：開啟和關閉檔案 🚪

### 開啟檔案：魔法傳送門 🌟
`open()` 函數就像連接程式與檔案的魔法傳送門！

```python
# 開啟檔案來讀取 - 就像打開一本書！📖
file = open('my_diary.txt', 'r')

# 開啟檔案來寫入 - 就像拿到一本空白筆記本！📝
file = open('shopping_list.txt', 'w')

# 開啟檔案來追加 - 就像在日記本上繼續寫！✍️
file = open('daily_log.txt', 'a')
```

### 關閉檔案：負責任的做法 🔒
用完檔案後一定要關閉 - 就像看完書後把書合上！

```python
file = open('example.txt', 'r')
# 對檔案做些什麼...
file.close()  # 別忘了這個！
```

### `with` 語句：聰明的做法 🧠
使用 `with` 就像有自動關閉功能 - 它會為你處理一切！

```python
# 聰明的做法 - Python 會自動關閉檔案！
with open('game_scores.txt', 'r') as file:
    content = file.read()
    print("📊 遊戲分數已載入！")
# 檔案會在這裡自動關閉 - 不用擔心！
```

## 讀取檔案：解鎖數位寶藏 🗝️

### 讀取整個檔案：速讀者 🏃‍♂️
適合小檔案 - 一次讀取所有內容！

```python
# 讀取你的整個聊天記錄
with open('chat_log.txt', 'r') as file:
    all_messages = file.read()
    print("💬 所有聊天訊息：")
    print(all_messages)

# 讀取設定檔
with open('game_settings.txt', 'r') as file:
    settings = file.read()
    print("⚙️ 遊戲設定已載入！")
    print(settings)
```

### 逐行讀取：謹慎的探索者 🧭
適合大檔案 - 一次讀取一行！

```python
# 逐行讀取故事檔案
with open('adventure_story.txt', 'r') as file:
    line_number = 1
    for line in file:
        print(f"📖 第 {line_number} 章：{line.strip()}")
        line_number += 1

# 讀取高分榜
with open('high_scores.txt', 'r') as file:
    print("🏆 頂尖玩家：")
    rank = 1
    for line in file:
        print(f"{rank}. {line.strip()}")
        rank += 1
```

### 讀取所有行到串列：組織者 📋
適合處理多行內容！

```python
# 讀取播放清單
with open('my_playlist.txt', 'r') as file:
    songs = file.readlines()
    print("🎵 你的播放清單：")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song.strip()}")

# 讀取購物清單
with open('shopping_list.txt', 'r') as file:
    items = file.readlines()
    print("🛒 購物清單：")
    for item in items:
        print(f"• {item.strip()}")
```

## 寫入檔案：創造數位傑作 ✍️

### 寫入檔案：內容創作者 📝
建立新檔案或覆蓋現有檔案！

```python
# 建立日記條目
with open('daily_journal.txt', 'w') as file:
    file.write("📅 今天的記錄：\n")
    file.write("學習 Python 的一天太棒了！🐍\n")
    file.write("檔案操作真的很酷！😎\n")
    print("✅ 日記條目已保存！")

# 建立遊戲存檔
player_data = {
    'name': 'CoolGamer123',
    'level': 15,
    'score': 9500,
    'items': ['sword', 'shield', 'potion']
}

with open('game_save.txt', 'w') as file:
    file.write(f"玩家：{player_data['name']}\n")
    file.write(f"等級：{player_data['level']}\n")
    file.write(f"分數：{player_data['score']}\n")
    file.write(f"道具：{', '.join(player_data['items'])}\n")
    print("💾 遊戲進度已保存！")
```

### 寫入行串列：批次建立者 📦
有效率地寫入多行！

```python
# 建立待辦事項清單
todo_items = [
    "📚 完成 Python 作業\n",
    "🎮 玩新發售的遊戲\n",
    "📱 回覆訊息\n",
    "🏃‍♂️ 去跑步\n",
    "🎬 和朋友看電影\n"
]

with open('todo_list.txt', 'w') as file:
    file.writelines(todo_items)
    print("✅ 待辦事項清單已建立！")

# 建立聯絡人清單
contacts = [
    "Alice: alice@email.com\n",
    "Bob: bob@email.com\n",
    "Charlie: charlie@email.com\n"
]

with open('contacts.txt', 'w') as file:
    file.writelines(contacts)
    print("📞 聯絡人清單已保存！")
```

## 檔案模式：不同的超能力 🦸‍♀️

### 模式小隊 🎭
每個模式都給你的程式不同的能力！

```python
# 📖 'r' - 讀取模式：閱讀者
with open('story.txt', 'r') as file:
    content = file.read()
    print("📚 讀取模式：非常適合消耗內容！")

# ✍️ 'w' - 寫入模式：創造者/破壞者
with open('new_story.txt', 'w') as file:
    file.write("從前從前...")
    print("📝 寫入模式：建立新檔案或覆蓋現有檔案！")

# ➕ 'a' - 追加模式：貢獻者
with open('story.txt', 'a') as file:
    file.write("\n結束！")
    print("📄 追加模式：在現有內容後面添加！")

# 🔢 'b' - 二進位模式：資料處理者
with open('image.png', 'rb') as file:
    image_data = file.read()
    print("💾 二進位模式：處理非文字檔案！")
```

### 模式組合：威力組合 💪
```python
# 讀取和寫入文字檔案
with open('config.txt', 'r+') as file:
    content = file.read()
    file.write("\n新增了新設定！")

# 處理二進位檔案
with open('game_data.bin', 'wb') as file:
    file.write(b"二進位遊戲資料")

# 追加到二進位檔案
with open('log.bin', 'ab') as file:
    file.write(b"新的日誌條目")
```

## 異常處理：安全網 🛡️

### 像專業人士一樣處理檔案錯誤 🎯
檔案可能很棘手 - 永遠要做好準備！

```python
# 安全的檔案讀取
def read_user_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"✅ 成功讀取 {filename}！")
            return content
    except FileNotFoundError:
        print(f"😱 糟糕！{filename} 不存在！")
        print("💡 提示：檢查檔案名稱並重試！")
        return None
    except PermissionError:
        print(f"🚫 拒絕存取！無法存取 {filename}")
        return None
    except IOError:
        print(f"💥 讀取 {filename} 時發生錯誤")
        return None

# 測試看看
content = read_user_file('my_secret_diary.txt')
if content:
    print("📖 檔案內容成功載入！")
```

### 終極錯誤處理器 🛠️
```python
def safe_file_operation(filename, mode, content=None):
    try:
        with open(filename, mode) as file:
            if mode == 'r':
                data = file.read()
                print(f"📖 從 {filename} 讀取了 {len(data)} 個字元")
                return data
            elif mode == 'w':
                file.write(content)
                print(f"✍️ 內容已寫入 {filename}")
                return True
            elif mode == 'a':
                file.write(content)
                print(f"➕ 內容已追加到 {filename}")
                return True
    except FileNotFoundError:
        print(f"🔍 找不到檔案 {filename}！")
    except PermissionError:
        print(f"🔒 沒有權限存取 {filename}")
    except IOError as e:
        print(f"💥 檔案操作失敗：{e}")
    except Exception as e:
        print(f"😵 意外的錯誤：{e}")

    return False

# 使用範例
safe_file_operation('test.txt', 'w', '你好，世界！')
safe_file_operation('test.txt', 'r')
```

## 史詩級挑戰 - 提升你的檔案技能！🚀

### 挑戰 1：個人日記管理器 📔
建立一個數位日記來保存你的想法！

```python
# 挑戰 1：在這裡寫你的解答！
import datetime

def write_diary_entry():
    today = datetime.date.today()
    entry = input("📝 今天發生了什麼事？ ")

    with open('my_diary.txt', 'a') as file:
        file.write(f"\n📅 {today}\n")
        file.write(f"💭 {entry}\n")
        file.write("-" * 50 + "\n")

    print("✅ 日記條目已保存！")

def read_diary():
    try:
        with open('my_diary.txt', 'r') as file:
            print("📖 你的日記條目：")
            print(file.read())
    except FileNotFoundError:
        print("📔 還沒有日記條目！開始寫吧！")

# 測試你的日記
write_diary_entry()
read_diary()
```

### 挑戰 2：遊戲高分追蹤器 🏆
記錄你的遊戲成就！

```python
# 挑戰 2：在這裡寫你的解答！
def add_high_score(player_name, score, game):
    score_entry = f"{player_name},{score},{game}\n"

    with open('high_scores.txt', 'a') as file:
        file.write(score_entry)

    print(f"🎮 新高分已加入：{player_name} 在 {game} 得到 {score} 分！")

def view_high_scores():
    try:
        with open('high_scores.txt', 'r') as file:
            print("🏆 高分排行榜：")
            print("-" * 40)

            scores = []
            for line in file:
                name, score, game = line.strip().split(',')
                scores.append((name, int(score), game))

            # 按分數排序（最高分在前）
            scores.sort(key=lambda x: x[1], reverse=True)

            for i, (name, score, game) in enumerate(scores, 1):
                print(f"{i}. {name}：{score} 分 ({game})")

    except FileNotFoundError:
        print("📊 還沒有高分記錄！開始遊戲吧！")

# 測試你的高分追蹤器
add_high_score("超酷玩家", 9500, "太空冒險")
add_high_score("專業玩家", 12000, "賽車遊戲")
view_high_scores()
```

### 挑戰 3：聊天記錄分析器 💬
分析你的聊天訊息來獲得有趣的統計！

```python
# 挑戰 3：在這裡寫你的解答！
def analyze_chat_log(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        total_messages = len(lines)
        word_count = 0
        longest_message = ""
        emoji_count = 0

        for line in lines:
            words = line.split()
            word_count += len(words)

            if len(line) > len(longest_message):
                longest_message = line.strip()

            # 計算表情符號（簡單檢查）
            emoji_count += sum(1 for char in line if ord(char) > 127)

        print("📊 聊天分析報告：")
        print(f"💬 總訊息數：{total_messages}")
        print(f"📝 總單字數：{word_count}")
        print(f"📏 每則訊息平均單字數：{word_count/total_messages:.1f}")
        print(f"📱 使用的表情符號：{emoji_count}")
        print(f"📖 最長訊息：{longest_message[:50]}...")

    except FileNotFoundError:
        print("💬 找不到聊天記錄！")

# 建立範例聊天記錄
sample_chat = [
    "嗨！最近怎麼樣？😊\n",
    "剛完成 Python 作業！🐍\n",
    "等等要不要一起玩遊戲？🎮\n",
    "好啊！我剛買了新的賽車遊戲 🏎️\n",
    "太棒了！晚上七點線上見 👋\n"
]

with open('chat_log.txt', 'w') as file:
    file.writelines(sample_chat)

analyze_chat_log('chat_log.txt')
```

### 挑戰 4：檔案備份系統 💾
為重要檔案建立簡單的備份系統！

```python
# 挑戰 4：在這裡寫你的解答！
import shutil
import datetime

def backup_file(source_file, backup_folder="backups"):
    try:
        # 如果備份資料夾不存在就建立
        import os
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        # 用時間戳記建立備份檔名
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}_{source_file}"
        backup_path = os.path.join(backup_folder, backup_name)

        # 複製檔案
        shutil.copy2(source_file, backup_path)

        print(f"✅ 備份已建立：{backup_path}")

    except FileNotFoundError:
        print(f"😱 找不到原始檔案 {source_file}！")
    except Exception as e:
        print(f"💥 備份失敗：{e}")

def restore_backup(backup_file, restore_name):
    try:
        shutil.copy2(backup_file, restore_name)
        print(f"🔄 檔案已還原為：{restore_name}")
    except Exception as e:
        print(f"💥 還原失敗：{e}")

# 測試備份系統
with open('important_file.txt', 'w') as file:
    file.write("這是非常重要的資料！💎")

backup_file('important_file.txt')
```

### 挑戰 5：文字雲產生器 🌟
為任何文字檔案建立詞頻分析器！

```python
# 挑戰 5：在這裡寫你的解答！
def create_word_cloud(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()

        # 清理文字並分割成單字
        import string
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()

        # 計算詞頻
        word_freq = {}
        for word in words:
            if len(word) > 2:  # 只計算超過 2 個字元的單字
                word_freq[word] = word_freq.get(word, 0) + 1

        # 按頻率排序
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        print("☁️ 文字雲分析：")
        print("=" * 40)

        for word, count in sorted_words[:10]:  # 前 10 個單字
            bar = "█" * (count // 2 + 1)  # 視覺化長條
            print(f"{word:15} {bar} ({count})")

        # 保存結果
        with open('word_analysis.txt', 'w') as file:
            file.write("詞頻分析結果\n")
            file.write("=" * 30 + "\n")
            for word, count in sorted_words:
                file.write(f"{word}: {count}\n")

        print("\n💾 完整分析已保存到 word_analysis.txt")

    except FileNotFoundError:
        print(f"📄 找不到檔案 {filename}！")

# 建立範例文字檔案
sample_text = """
Python 很棒！Python 讓程式設計變得有趣又簡單。
學習 Python 開啟了許多可能性。
Python 被用於網頁開發、資料科學和人工智慧。
Python 社群很友善也很有幫助。
Python 語法乾淨易讀。
"""

with open('sample_text.txt', 'w') as file:
    file.write(sample_text)

create_word_cloud('sample_text.txt')
```

## 檔案高手的專業技巧！🎯

1. **總是使用 `with` 語句** - 它們會自動處理檔案關閉！🔐
2. **處理異常** - 檔案可能不可預測，所以要做好準備！🛡️
3. **選擇正確的模式** - 讀取用 `'r'`、寫入用 `'w'`、追加用 `'a'`！📝
4. **使用有意義的檔名** - `game_save.txt` 比 `file1.txt` 好！📄
5. **檢查檔案是否存在** - 開啟前使用 `os.path.exists()`！🔍
6. **正確處理路徑** - 使用 `os.path.join()` 確保跨平台相容性！🛤️

## 真實世界的應用 🌍

檔案操作在現代程式設計中無所不在：
- **遊戲**：存檔、設定、高分、關卡資料 🎮
- **社群媒體**：聊天記錄、使用者檔案、媒體檔案 📱
- **學校**：作業繳交、成績簿、出勤記錄 📚
- **商業**：資料庫、報告、備份、設定 💼
- **創意**：照片編輯、音樂製作、影片剪輯 🎨

你學的不只是檔案操作 - 你學的是如何讓程式記住、儲存和分享資訊！這就是數位記憶的製作方式！🧠✨

掌握這些概念，你就能建立可以保存遊戲進度、分析資料、備份重要檔案等等的程式！🚀💫

記住：手機上的每個應用程式、玩的每個遊戲、造訪的每個網站 - 它們都使用檔案操作來儲存和檢索資訊。你正在學習數位儲存的基礎！🏗️📁