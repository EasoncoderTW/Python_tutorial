# Python 教學講義 Chapter 1
[TOC]
###### tags: `python tutorial`

## Python 直譯器
### 1. 可以當計算機
```python=
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18)
[MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> 2
2
>>> 3-5
-2
>>> 12*4
48
>>> 6/3
2.0
>>> 9/4
2.25
>>> 9//4
2
>>> 9%4
1
>>> (1-3)*5
-10
>>> 2**5
32
>>> 
```
### 2. 運算符號
**1. 指定符號(=)**
**2. 加(+)、減(-)、乘(\*)、除(/)**
**3. 整除(//)、取餘數(%)**
**4. 次方(\*\*)**
**5. 邏輯運算符號 - 且(and)、或(or)**
**6. 關係運算符號 - 大於(>)、小於(<)、等於(==)**

### 3. 甚麼是型態?
#### int (整數)
```python=
0
-1
12
-123
4562
```
#### float (浮點數)
```python=
2.0
-1.5
3.1415926
0.00001234
```
#### str (字串)
```python=
"123"
'456'
"I'm a human."
'He say "Wow!"'

"""
This is the multi-Line string Demo.
We can write any thing down.
Python is Funny.
"""
```
#### bool (布林值)
```python=
True
False
```
### 4. 什麼是物件?
```python=
a = 1
b = 2
c = a + b
flag = False
s = "This is a string."
f = 3.14159
```
1. a ,b ,c 都是物件，型態皆為整數(int)
2. flag是物件，型態為布林值(bool)
3. s是物件，型態為字串(str)
4. f是物件，型態為浮點數(float)

## Python Script (腳本)

### 1. print and input
#### Function : print(字串or其他型態, 特殊隱藏參數)
- 功能
    - 輸出資訊，可以透過排版美化資訊樣貌。
- 參數
    - 將需要輸出至螢幕的物件傳入 print()。
- 範例 
```python=
a = 10
b = 20
c = a + b
s = "Test"
print(a,b,c,s)
print(a,c,b)
```
- output
```shell=
10 20 30 Test
10 30 20

```
#### Function : input(字串)
- 功能
    - 獲取輸入資訊。
- 參數
    - 將需要輸出至螢幕的訊息傳入 input()。
- 範例 
```python=
a = input()
b = input("Test ")
print(a,b)
```
- output
```shell=
>>> 10
>>> Test 20
10 20

```

### 2. First simple script
```python=
# First simple script
# 註解
# ax**2 + bx + c = 0 solution

a = float(input("a = ? "))
b = float(input("b = ? "))
c = float(input("c = ? "))

D = (b**2 - 4*a*c)**0.5

x1 = (-b + D)/(2*a)
x2 = (-b - D)/(2*a)

print("solution:")
print("x1 = ",x1)
print("x2 = ",x2)

```
Demo
```shell=
a = ? 2
b = ? 10
c = ? 12
solution:
x1 =  -2.0
x2 =  -3.0
```