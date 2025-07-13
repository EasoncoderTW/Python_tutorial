# 第九課 - 檔案

在本課程中，我們將介紹 Python 中處理檔案的基礎，包括如何開啟、讀取、寫入和關閉檔案，以及理解檔案模式和處理例外。

## 開啟和關閉檔案

### 開啟檔案
檔案使用 `open()` 函數開啟，該函數返回一個檔案物件。您需要指定檔案名稱和開啟檔案的模式。
```python
file = open('example.txt', 'r')  # 開啟以供讀取
```

### 關閉檔案
執行操作後關閉檔案以釋放系統資源是很重要的。
```python
file.close()
```

### 使用 `with` 敘述
使用 `with` 敘述開啟檔案確保在其套件完成後檔案能夠正確關閉，即使出現例外也是如此。
```python
with open('example.txt', 'r') as file:
    content = file.read()
```

## 從檔案讀取

### 讀取整個檔案
您可以使用 `read()` 方法讀取檔案的全部內容。
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 逐行讀取
您可以使用 `readline()` 方法逐行讀取檔案。
```python
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # end='' 避免雙重換行
        line = file.readline()
```

### 將所有行讀取到列表中
您可以使用 `readlines()` 方法將檔案的所有行讀取到列表中。
```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
```

## 寫入檔案

### 寫入檔案
您可以使用 `write()` 方法寫入檔案。
```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
```

### 寫入行列表
您可以使用 `writelines()` 方法將行列表寫入檔案。
```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

## 檔案模式

### 常見的檔案模式
- `'r'` - 讀取模式（預設）。開啟檔案供讀取。
- `'w'` - 寫入模式。開啟檔案供寫入（建立新檔案或截斷現有檔案）。
- `'a'` - 附加模式。開啟檔案供寫入，如果檔案存在則附加到檔案末尾。
- `'b'` - 二進位模式。與其他模式一起使用以讀取/寫入二進位檔案。

### 不同模式的範例
```python
# 讀取模式
with open('example.txt', 'r') as file:
    content = file.read()

# 寫入模式
with open('example.txt', 'w') as file:
    file.write("Overwriting the content.")

# 附加模式
with open('example.txt', 'a') as file:
    file.write("\nAppending this line.")

# 二進位模式
with open('example.bin', 'wb') as file:
    file.write(b"Binary data")
```

## 檔案例外處理

### 處理例外
在處理檔案時處理例外是很重要的，以避免因檔案相關錯誤而導致的崩潰。
```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("檔案未找到。")
except IOError:
    print("讀取檔案時發生錯誤。")
```

## 範例和練習

### 範例 1：讀取檔案
讀取檔案內容並印出每一行。
```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

### 範例 2：寫入檔案
將多行寫入檔案。
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

### 範例 3：附加到檔案
將一行附加到現有檔案。
```python
with open('example.txt', 'a') as file:
    file.write("Appending this line.\n")
```

### 範例 4：例外處理
在嘗試讀取不存在的檔案時處理例外。
```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("檔案未找到。")
except IOError:
    print("讀取檔案時發生錯誤。")
```

### 練習

#### 練習 1：計算行數
編寫一個函數，接收檔案名稱作為參數並回傳檔案中的行數。

#### 解答
```python
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# 測試
print(count_lines('example.txt'))  # 輸出：（example.txt 中的行數）
```

#### 練習 2：複製檔案
編寫一個函數，接收兩個檔案名稱作為參數，並將第一個檔案的內容複製到第二個檔案。

#### 解答
```python
def copy_file(source, destination):
    with open(source, 'r') as src_file:
        content = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(content)

# 測試
copy_file('example.txt', 'copy_example.txt')
```

#### 練習 3：單字頻率
編寫一個函數，接收檔案名稱作為參數，並回傳一個字典，包含檔案中每個單字的頻率。

#### 解答
```python
def word_frequency(filename):
    with open(filename, 'r') as file:
        content = file.read()
    words = content.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# 測試
print(word_frequency('example.txt'))  # 輸出：{word: frequency, ...}
```

理解如何在 Python 中處理檔案對於資料處理和儲存是至關重要的。練習這些範例和練習，以熟練開啟、讀取、寫入和處理檔案，以及管理檔案模式和例外。