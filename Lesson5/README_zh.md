# 第五課：Python 的超能力列表！🦸‍♂️🦸‍♀️

歡迎來到 Python 列表的世界！今天，我們將探索 Python 如何像超級英雄一樣整理數據集合！🛠️✨

## 為什麼列表如此棒？🤔

想想你的日常生活：
- "我旅行需要帶什麼？"（物品清單 🧳）
- "我最喜歡的歌曲有哪些？"（播放列表 🎵）
- "我需要買什麼雜貨？"（購物清單 🛒）

Python 列表可以做到這些，甚至更多！讓我們學習如何讓你的程式像你一樣井井有條！🧠

## 列表基礎 📝

### 什麼是列表？
列表就像一個寶箱 🧰，按特定順序存放物品。你可以隨時添加、刪除或修改物品！列表使用方括號（`[]`）定義。

### 創建列表
```python
# 你最喜歡的水果 🍎🍌🍒
fruits = ["apple", "banana", "cherry"]
print(fruits)  # 輸出：['apple', 'banana', 'cherry']
```

### 訪問元素
```python
# 拿到你最喜歡的水果 🍎
print(fruits[0])  # 輸出：apple
print(fruits[1])  # 輸出：banana
print(fruits[-1])  # 輸出：cherry
```

### 修改元素
```python
# 改變對香蕉的想法 🍌➡️🫐
fruits[1] = "blueberry"
print(fruits)  # 輸出：['apple', 'blueberry', 'cherry']
```

## 列表的超能力 🦸‍♂️

### 添加元素
- **append()**：將物品添加到列表末尾。
  ```python
  fruits.append("orange")
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry', 'orange']
  ```

- **insert()**：在指定位置插入物品。
  ```python
  fruits.insert(1, "banana")
  print(fruits)  # 輸出：['apple', 'banana', 'blueberry', 'cherry', 'orange']
  ```

### 刪除元素
- **remove()**：刪除第一次出現的物品。
  ```python
  fruits.remove("banana")
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry', 'orange']
  ```

- **pop()**：刪除並返回最後一個物品，或指定位置的物品。
  ```python
  popped_fruit = fruits.pop()
  print(popped_fruit)  # 輸出：orange
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry']
  ```

### 其他有用的方法
- **sort()**：按升序排序列表。
  ```python
  fruits.sort()
  print(fruits)  # 輸出：['apple', 'blueberry', 'cherry']
  ```

- **reverse()**：反轉列表順序。
  ```python
  fruits.reverse()
  print(fruits)  # 輸出：['cherry', 'blueberry', 'apple']
  ```

- **len()**：獲取列表中的物品數量。
  ```python
  print(len(fruits))  # 輸出：3
  ```

### 列表推導式
列表推導式就像魔法咒語 🪄，可以快速創建列表。
```python
squares = [x**2 for x in range(10)]
print(squares)  # 輸出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 超越列表：元組、字典和集合 🌟

### 元組
元組就像上鎖的寶箱 🧰——你不能改變裡面的物品。
```python
# 混合物品 🎲
tuple_example = (1, "apple", 3.14)
print(tuple_example)  # 輸出：(1, 'apple', 3.14)
print(tuple_example[1])  # 輸出：apple
```

### 字典
字典就像秘密特工 🕵️‍♂️——它們將鍵與值配對。
```python
# 個人信息 🧑‍💻
dict_example = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_example)  # 輸出：{'name': 'Alice', 'age': 25, 'city': 'New York'}
print(dict_example["name"])  # 輸出：Alice

# 添加更多信息 📧
dict_example["email"] = "alice@example.com"
print(dict_example)  # 輸出：{'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
```

### 集合
集合就像超級英雄團隊 🦸‍♀️🦸‍♂️——它們只允許唯一的成員。
```python
# 獨特的水果 🍎🍌🍒
set_example = {"apple", "banana", "cherry"}
print(set_example)  # 輸出：{'apple', 'cherry', 'banana'}

# 添加新成員 🍊
set_example.add("orange")
print(set_example)  # 輸出：{'apple', 'cherry', 'banana', 'orange'}

# 刪除成員 🍌
set_example.remove("banana")
print(set_example)  # 輸出：{'apple', 'cherry', 'orange'}
```

## 史詩挑戰 - 提升你的技能！🚀

### 挑戰 1：電影列表 🎥
創建一個你最喜歡的電影列表並：
1. 添加一部新電影。
2. 刪除第二部電影。
3. 打印最終列表。

### 挑戰 2：個人字典 🧑‍💻
創建一個包含你的姓名、年齡和城市的字典。然後：
1. 添加你的電子郵件。
2. 更新你的年齡。
3. 打印最終字典。

### 挑戰 3：多彩集合 🌈
創建一個你最喜歡的顏色集合並：
1. 添加一種新顏色。
2. 刪除一種現有顏色。
3. 打印最終集合。

### 挑戰 4：前三名學生 🏆
從包含姓名和分數的字典中找到前三名學生：
```python
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Carol": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 91,
}

# 在這裡編寫你的程式碼
```

列表、元組、字典和集合是你組織和管理數據的工具！練習這些挑戰，成為 Python 超級英雄！🦸‍♂️🦸‍♀️