# 第一課：列印和輸入

## 1. Hello world
在 Python 中，你可以用一行指令就執行程式。相比於同樣是高階語言的 C/C++，Python 的語法更加多樣且簡單。

python
```python
# 列印 "hello world"
print("hello world")
```
C
```C
#include <stdio.h>

int main()
{
    printf("hello world\n");
    return 0;
}
```
C++
```CPP
#include <iostream>
using namespace std;

int main()
{
    cout << "hello world" << endl;
    return 0;
}
```

> Hello World 的由來 -https://kknews.cc/zh-tw/tech/l9x2e8b.html


## 2. print 函數和 input 函數

在 Python 中，print 函數用來將資訊輸出到控制台，而 input 函數用來獲取使用者的輸入。

```python
# 使用 print 在螢幕上輸出字串
print("Hello, world!")

# 使用 input 獲取使用者輸入的文字
name = input("請輸入您的姓名：")
print("你好，" + name + "！")
```

print 函數有兩個常用的參數：**sep** 和 **end**
```python
print(字串1, 字串2, ... , sep=" ", end="\n") # 預設值
```
所有字串會被印出並用 sep 所代表的字串分隔。預設是 " "（空白鍵）。而結尾會連接 end 所代表的字串，預設是換行符號 `\n`。

## 練習
請完成程式中的填空，讓輸出字串使用輸入字串作為分隔符號。

```
Enter seperator: @@@
Enter a string: Apple
Apple@@@Apple@@@Apple@@@Apple@@@Apple
```