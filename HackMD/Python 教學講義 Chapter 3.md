# Python 教學講義 Chapter 3
[TOC]
###### tags: `python tutorial`


## 流程控制 (control flow)

### if 敘述
![](https://i.imgur.com/ofo45Rq.png)
- **格式**
```python=
if expression:
    statement(s)
elif expression:  ##Optional
    statement(s)
elif expression:  ##Optional
    statement(s)

...
else:             ##Optional
    statement(s)
```
- 範例
```python=
>>> x = 5
>>> if x < 0:
...     print('x is negative')
... elif x % 2:
...     print('x is positive and odd')
... else:
...     print('x is even and non-negative')
...

```
```
x is positive and odd
```
- 寫法優化
```python=
# Best
if x:

# Not so good
if x is True:
if x == True:
if Bool(x):
```

### while 敘述
![](https://i.imgur.com/2Du04d9.png)

- while 敘述會重複執行**敘述區塊**直到**expression**不成立。
```python=
while expression:
    statement(s) / loop body

(else:    
    statement(s))
```
- 範例
```python=
>>> x = 5
>>> while x > 0:
...     x -= 1
...     print(x)
...

```
```shell=
4
3
2
1
0
```

### for 敘述
- for 敘述會重複執行**敘述區塊**直到**iterable**被歷遍。
```python=
for target in iterable:
    statement(s) / loop body

(else:    
    statement(s))
```
- 這裡的**iterable**可以是前面的序列物件，只要是可以迭代的物件即可。
```python=
>>> for i in "apple":
...     print("Got letter: ", i)
...
```
```shell=
Got letter:  a
Got letter:  p
Got letter:  p
Got letter:  l
Got letter:  e
```
- 字典透過 **d . items()** 產生一組串列 
```python=
>>> d
{'a': 100, 'b': 3.14, 'c': 'cat', 'd': 'dog'}
>>> for key,value in d.items():
...     print(key, value)
...
```
```shell=
a 100
b 3.14
c cat
d dog
```

## range
### range 的產物
- **range( 起始(含), 結束, 間隔)**
```python=
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python=
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10))
[2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
```
### 利用range控制for敘述的執行次數與target的內容
- 範例 1
```python=
>>> for i in range(5):
...     print("run ", i, " times")
...
```
```shell=
run  0  times
run  1  times
run  2  times
run  3  times
run  4  times
```
- 範例 2
```python=
>>> c = 0
>>> for i in range(2,10,2):
...     c += 1
...     print("run ", c, " times. got value ", i)
...
```
```shell=
run  1  times. got value  2
run  2  times. got value  4
run  3  times. got value  6
run  4  times. got value  8
```
## 讓迴圈有更多變化
### break
- break續屬只能用在**迴圈主體(loop body)** 中
- 一個break只會終止**一個最內層**的迴圈

```python=
>>> x = 5
>>> while True:
...     x -= 1
...     print("loop ",x)
...     if x < 0:
...             print('break loop')
...             break
...
```
```shell=
loop  4
loop  3
loop  2
loop  1
loop  0
loop  -1
break loop
```
### continue
```python=
>>> for i in range(10):
...     print('check ones ',i)
...     if i < 5:
...             print("skip ", i)
...             continue
...     print('check twice ',i)
...
```
```shell=
check ones  0
skip  0
check ones  1
skip  1
check ones  2
skip  2
check ones  3
skip  3
check ones  4
skip  4
check ones  5
check twice  5
check ones  6
check twice  6
check ones  7
check twice  7
check ones  8
check twice  8
check ones  9
check twice  9
```
### pass
- 在維持特定的架構之下，如果有一個程式區塊不可省略，可以使用**pass**

- 範例
```python=
>>> x = 10
>>> if x < 10:
... else:
...     print("else")
...
```
```shell=
  File "<stdin>", line 2
    else:
       ^
IndentationError: expected an indented block
```
- 加入 pass
```python=
>>> x = 10
>>> if x < 10:
...     pass
... else:
...     print("else")
...
```
```shell=
else
```