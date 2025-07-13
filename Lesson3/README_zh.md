# 第三課：Python的數學超能力！ 🧮✨

歡迎來到Python數學的精彩世界！把Python想像成你超級聰明的計算機，它能比你說出「披薩」還要快地解決問題！🍕

## 為什麼程式設計需要數學？ 🤔

想像你正在製作一個玩家收集金幣的遊戲，或者建立一個計算你存了多少零用錢的應用程式。數學在程式設計中無處不在！讓我們探索Python的數學超能力。

## 基本算術運算 - 四大天王！

### 加法 (+)：收集者 🎯
加法就像在電子遊戲中收集物品！
```python
# 你有10個金幣，又找到5個
coins_before = 10
coins_found = 5
total_coins = coins_before + coins_found
print(f"總金幣數：{total_coins}")  # 輸出：總金幣數：15

# 現實世界例子：社群媒體按讚數
instagram_likes = 245
new_likes = 38
total_likes = instagram_likes + new_likes
print(f"哇！你現在有 {total_likes} 個讚！ 🎉")  # 輸出：哇！你現在有 283 個讚！ 🎉
```

### 減法 (-)：消費者 💸
減法就像花錢或在遊戲中失去生命！
```python
# 你有50塊錢，花20塊買遊戲
money_before = 50
spent_on_game = 20
money_left = money_before - spent_on_game
print(f"剩餘金額：${money_left}")  # 輸出：剩餘金額：$30

# 遊戲例子：生命值
player_health = 100
damage_taken = 25
current_health = player_health - damage_taken
print(f"剩餘生命值：{current_health} HP")  # 輸出：剩餘生命值：75 HP
```

### 乘法 (*)：倍增器 🚀
乘法就像複製或重複加法 - 超級強大！
```python
# 你每天工作8小時，每小時賺15塊
hours_worked = 8
hourly_rate = 15
daily_earnings = hours_worked * hourly_rate
print(f"每日收入：${daily_earnings}")  # 輸出：每日收入：$120

# 遊戲例子：經驗值
enemies_defeated = 12
exp_per_enemy = 50
total_exp = enemies_defeated * exp_per_enemy
print(f"總共獲得經驗值：{total_exp} 點！ 🎮")  # 輸出：總共獲得經驗值：600 點！ 🎮
```

### 除法 (/)：分享者 🍰
除法就像在朋友間平均分配披薩片！
```python
# 8片披薩分給4個朋友
pizza_slices = 8
number_of_friends = 4
slices_per_person = pizza_slices / number_of_friends
print(f"每個人得到 {slices_per_person} 片")  # 輸出：每個人得到 2.0 片

# 學習例子：平均分數
total_points = 450
number_of_tests = 5
average_score = total_points / number_of_tests
print(f"你的平均分數：{average_score}%")  # 輸出：你的平均分數：90.0%
```

## 進階數學三人組 - 升級！ 🎯

### 取餘數 (%)：餘數偵探 🕵️
取餘數找出「剩餘」- 超級適合檢查數字是偶數還是奇數！
```python
# 檢查數字是偶數還是奇數
number = 17
remainder = number % 2
if remainder == 0:
    print(f"{number} 是偶數！")
else:
    print(f"{number} 是奇數！")  # 輸出：17 是奇數！

# 現實例子：組織團隊
total_students = 23
team_size = 4
students_left_out = total_students % team_size
print(f"{students_left_out} 位學生需要加入現有團隊")  # 輸出：3 位學生需要加入現有團隊
```

### 指數 (**)：力量提升器 💪
指數就像為你的數字加上超級能量！
```python
# 計算複利（錢隨時間增長）
initial_amount = 1000
growth_rate = 1.1  # 10% 增長
years = 3
final_amount = initial_amount * (growth_rate ** years)
print(f"{years} 年後：${final_amount:.2f}")  # 輸出：3 年後：$1331.00

# 遊戲例子：升級傷害
base_damage = 5
level = 4
damage_multiplier = 2 ** level  # 每級傷害翻倍
final_damage = base_damage * damage_multiplier
print(f"等級 {level} 傷害：{final_damage} 點！ 💥")  # 輸出：等級 4 傷害：80 點！ 💥
```

### 整數除法 (//)：無條件捨去冠軍 📉
整數除法只給你整數 - 不允許小數！
```python
# 50天中有多少完整週？
total_days = 50
days_per_week = 7
full_weeks = total_days // days_per_week
print(f"完整週數：{full_weeks}")  # 輸出：完整週數：7

# 電影院例子：可以排多少排6人座？
total_seats = 100
seats_per_row = 6
full_rows = total_seats // seats_per_row
print(f"我們可以排 {full_rows} 排完整座位")  # 輸出：我們可以排 16 排完整座位
```

## 運算子優先順序 - 運算順序！ 📋

把這個想像成照食譜做菜 - 你需要按正確順序做事！

### 黃金法則：PEMDAS（請原諒我親愛的莎莉阿姨）
1. **P**arentheses `()` 括號 - 第一優先！
2. **E**xponents `**` 指數 - 力量行動！
3. **M**ultiplication `*` 乘法和 **D**ivision `/` 除法（包括 `//` 和 `%`）- 由左到右
4. **A**ddition `+` 加法和 **S**ubtraction `-` 減法 - 由左到右

### 現實世界例子：計算你的遊戲分數 🎮
```python
# 複雜的計分系統
base_score = 100
bonus_multiplier = 2
power_up_bonus = 3 ** 2  # 道具給9分
penalty = 15
combo_hits = 4

final_score = base_score + bonus_multiplier * power_up_bonus * combo_hits - penalty
print(f"你的最終分數：{final_score}")  # 輸出：你的最終分數：157

# 讓我們一步步分解：
# 1. 首先：3 ** 2 = 9 （指數）
# 2. 然後：2 * 9 = 18 （乘法）
# 3. 然後：18 * 4 = 72 （乘法）
# 4. 然後：100 + 72 = 172 （加法）
# 5. 最後：172 - 15 = 157 （減法）
```

## 有趣挑戰 - 測試你的技能！ 🎯

### 挑戰1：零用錢計算機 💰
你每週得到20塊零用錢。如果你每週花15塊買零食，計算6週後你會有多少錢。

```python
# 你的解答在這裡！
weekly_allowance = 20
weekly_spending = 15
weeks = 6
money_saved = (weekly_allowance - weekly_spending) * weeks
print(f"{weeks} 週後存的錢：${money_saved}")  # 輸出：6 週後存的錢：$30
```

### 挑戰2：成績計算機 📊
如果你的考試成績是：85, 92, 78, 96, 88，計算你的學期平均分數

```python
# 你的解答在這裡！
test_scores = [85, 92, 78, 96, 88]
total_points = sum(test_scores)
number_of_tests = len(test_scores)
average = total_points / number_of_tests
print(f"你的學期平均分數：{average}%")  # 輸出：你的學期平均分數：87.8%
```

### 挑戰3：披薩派對規劃師 🍕
你要為23個人訂披薩。每個披薩有8片，可以餵飽3個人。你需要多少個披薩？

```python
# 你的解答在這裡！
people = 23
people_per_pizza = 3
pizzas_needed = people // people_per_pizza + (1 if people % people_per_pizza > 0 else 0)
print(f"派對需要 {pizzas_needed} 個披薩！")  # 輸出：派對需要 8 個披薩！
```

### 挑戰4：複利計算機 🏦
如果你投資500塊，年利率5%（1.05倍數），10年後你會有多少錢？

```python
# 你的解答在這裡！
principal = 500
interest_rate = 1.05
years = 10
final_amount = principal * (interest_rate ** years)
print(f"{years} 年後，你會有：${final_amount:.2f}")  # 輸出：10 年後，你會有：$814.45
```

## 年輕程式設計師的專業建議！ 🌟

1. **使用括號**當你不確定運算順序時 - 安全第一！
2. **註解你的程式碼** - 解釋你的數學在做什麼
3. **先用簡單數字測試**，然後再試複雜的
4. **想像現實世界** - 把數學關聯到你關心的事物（遊戲、金錢、社群媒體）

記住：每個應用程式、遊戲和網站都使用這些基本數學運算。你正在學習數位世界的基礎！🚀

現在去像編程巫師一樣計算吧！🧙‍♂️✨