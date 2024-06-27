# Python 教學講義 Homework 1
[TOC]
###### tags: `python tutorial homework`

## Lab 1-1 print 
- print 的 隱藏參數 **end**
- 預設 **end = '\n'**
```python=
>>> print("This is a book.", end = "(this the end parameter)\n")
This is a book.(this the end parameter)
>>>
```
### 跳脫字元(escape character)
- 輸出一些無法透過文字表達的格式(游標換行、tab、游標至頭)
    - 游標換行 (next line): **\n**
    - 游標至頭 (return): **\r**
    - Tab間隔 (tab): **\t**
```python=
>>> print("This\nisa\tbook.\n")
This
isa     book.

>>>
```
```python=
print("This is ",end='')
print("a",end=' ')
print("book.",end='\n')
print("That is ",end='')
print("a",end=' ')
print("pen.",end='\n')
```
```shell=
This is a book.
That is a pen.

```
## HW 1-1
- 利用 for 化簡以下指令，且輸出結果不變
- 提示 : 字串的可重複性
```python=
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
print("********")
print("*********")
print("**********")
```

## HW 1-2
- 製作可運算 N! (階層)的程式
- 注意 : python中沒直接算階層的運算符號
```shell=
Input N = 3
N! =  6

Input N = 5
N! =  120
```

## HW 1 挑戰題
- 輸出9x9乘法表
- 可以從 2x2 ~ 2x9 開始設計程式，再延伸到全部。
- 範例輸出
```shell=
2 * 2 = 4 2 * 3 = 6 2 * 4 = 8 2 * 5 = 10 2 * 6 = 12 2 * 7 = 14 2 * 8 = 16 2 * 9 = 18
3 * 2 = 6 3 * 3 = 9 3 * 4 = 12 3 * 5 = 15 3 * 6 = 18 3 * 7 = 21 3 * 8 = 24 3 * 9 = 27
4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 4 * 5 = 20 4 * 6 = 24 4 * 7 = 28 4 * 8 = 32 4 * 9 = 36
5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 5 * 6 = 30 5 * 7 = 35 5 * 8 = 40 5 * 9 = 45
6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 6 * 7 = 42 6 * 8 = 48 6 * 9 = 54
7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 7 * 8 = 56 7 * 9 = 63
8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 8 * 9 = 72
9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
```
