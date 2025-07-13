# 第一課：列印和輸入 - 讓電腦跟你聊天！🎮

## 🚀 歡迎來到 Python 的世界！

想像一下，你正在跟你的電腦聊天，就像在 Discord 或 LINE 上聊天一樣。Python 就是這個「聊天室」的語言！

## 1. Hello World - 你的第一句話！👋

還記得你第一次在群組裡發訊息的感覺嗎？現在我們要讓電腦說出它的第一句話！

在 Python 中，你只需要一行程式碼就能讓電腦說話。相比其他程式語言，Python 就像是發 LINE 訊息一樣簡單！

**Python（超簡單！）：**
```python
# 讓電腦說 "Hello World"
print("Hello World! 我活過來了！🤖")
```

**C語言（要寫一堆...）：**
```c
#include <stdio.h>

int main()
{
    printf("Hello World\n");
    return 0;
}
```

**C++（還是很複雜...）：**
```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello World" << endl;
    return 0;
}
```

> 💡 **小知識：Hello World 的由來**
>
> "Hello World" 是程式設計師的傳統第一句話，就像武俠小說裡的第一招「平沙落雁」一樣經典！
>
> 更多故事：https://kknews.cc/zh-tw/tech/l9x2e8b.html

## 2. print 函數 - 讓電腦當你的傳聲筒 📢

### 基本用法
```python
# 讓電腦說話
print("嗨！我是你的 Python 助手！")
print("今天天氣真好呢～")
print("你想學什麼呢？")
```

### 進階技巧：讓電腦跟你對話
```python
# 取得使用者輸入 - 就像聊天一樣！
name = input("請問你的名字是？")
age = input("你幾歲了？")

print("哇！原來你叫 " + name + "！")
print("而且你才 " + age + " 歲，真年輕！")
print("歡迎加入 Python 的世界！🎉")
```

## 3. print 函數的超能力 - sep 和 end 參數 ⚡

print 函數有兩個隱藏技能：**sep**（分隔符）和 **end**（結尾符）

```python
print(字串1, 字串2, ... , sep=" ", end="\n") # 預設值
```

### 實際範例：
```python
# 預設情況
print("蘋果", "橘子", "香蕉")
# 輸出：蘋果 橘子 香蕉

# 用逗號分隔（像購物清單）
print("蘋果", "橘子", "香蕉", sep=", ")
# 輸出：蘋果, 橘子, 香蕉

# 用箭頭分隔（像遊戲路徑）
print("新手村", "森林", "城堡", sep=" → ")
# 輸出：新手村 → 森林 → 城堡

# 用表情符號分隔（超可愛！）
print("程式設計", "遊戲", "音樂", sep=" 🎵 ")
# 輸出：程式設計 🎵 遊戲 🎵 音樂
```

### 控制結尾的魔法：
```python
# 讓文字在同一行
print("載入中", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" 完成！")
# 輸出：載入中... 完成！

# 創造聊天效果
print("你：", end="")
print("今天天氣如何？")
print("電腦：", end="")
print("今天陽光普照，適合寫程式！☀️")
```

## 🎮 挑戰時間！

### 任務：創造你的個人簽名檔
請完成以下程式，讓輸出像你的個人簽名檔一樣酷炫！

```python
separator = input("請輸入你喜歡的分隔符號（例如：⭐, 🎮, 💫）：")
nickname = input("請輸入你的暱稱：")

# 用你選的分隔符號，重複顯示暱稱 5 次
print(nickname, nickname, nickname, nickname, nickname, sep=separator)

# 預期輸出例子：
# 請輸入你喜歡的分隔符號：⭐
# 請輸入你的暱稱：小明
# 小明⭐小明⭐小明⭐小明⭐小明
```

### 進階挑戰：打造聊天機器人
```python
print("🤖 歡迎來到 Python 聊天室！")
print("=" * 30)

user_name = input("請輸入你的暱稱：")
favorite_game = input("你最喜歡的遊戲是什麼？")
favorite_subject = input("你最喜歡的科目是什麼？")

print("\n🎉 個人檔案建立完成！")
print("🏷️  暱稱：" + user_name)
print("🎮 最愛遊戲：" + favorite_game)
print("📚 最愛科目：" + favorite_subject)
print("\n歡迎來到 Python 的世界，" + user_name + "！")
print("讓我們一起用程式創造酷炫的", favorite_game, "外掛程式吧！", sep="")
```

## 🌟 本課重點回顧

- ✅ `print()` 函數：讓電腦說話的魔法咒語
- ✅ `input()` 函數：讓電腦聽你說話
- ✅ `sep` 參數：控制文字間的分隔符號
- ✅ `end` 參數：控制文字結尾的樣式
- ✅ 字串連接：用 `+` 把文字串在一起

## 💡 生活應用

想想看，你學會的這些技能可以用來：
- 📱 設計聊天機器人
- 🎮 製作遊戲中的對話系統
- 📊 建立互動式問卷
- 🎨 創造個人化的文字藝術

準備好進入下一課了嗎？我們要學習 Python 的「數據類型」- 就像認識不同種類的寶可夢一樣有趣！🔥