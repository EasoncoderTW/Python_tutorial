# Python 教學講義 Chapter 2
[TOC]
###### tags: `python tutorial`


## 序列 (sequences)
- 序列可以接一些元素集合在一起，成為一個序列，每個元素皆為該序列的成員(member / element)
- 序列化的資料會讓我們比較好找尋與操作資料。
### 序列的串接與重複
同型別的序列可以透過運算子 **+** 來達成串接(concatenate)(S + S)
序列可以透過運算子 **\*** 加上一個整數來達成重複串接(S * n)

```python=
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> ['a','b','c'] * 3
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
```
### 成員資格的測試
簡單來說，就是檢查一個物件是否式序列中的成員，也就是是否在序列之中。
關鍵字: **in**
```python=
>>> 1 in [1,2,3]
True
>>> 4 in [1,2,3]
False
```
### 序列的索引
- 在python中，序列的索引編號式從**0**開始計算，如果序列**S有K個成員**，則S的索引範圍為**S[0]~S[K-1]**。
- 索引的另外一種表示方式: **倒數**，**s[-1]~s[-K]** 也是容許的索引範圍，且**S[-1]等同S[K-1]**、**S[-2]等同S[K-2]**，以此類推。
```python=
>>> S = [12, 23, 34, 45, 56]
>>> S[0]
12
>>> S[-1]
56
>>> S[2]
34
>>> S[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

### 序列切片
既然我們可以使用序列所引取的序列特定的成員，也可透過索引的夾擊將序列切片。
- 語法: **S[ i : j ]**，將S序列中的下界**i(包含)** 與上界**j(不包含)** 
```python=
>>> S = [12, 23, 34, 45, 56]
>>> S[1:3]
[23, 34]
>>> S[2:5]
[34, 45, 56]
```
- **當 j = K 時 j 可省略，當 i = 0 時 i 可省略**
**S[ i : L ] -> S[ i : ]**
**S[ 0 : j ] -> S[ : j ]**
**S[ 0 : L ] -> S[ : ] (S序列的淺層拷貝，shallow copy)**
```python=
>>> S = [12, 23, 34, 45, 56]
>>> S[:3]
[12, 23, 34]
>>> S[2:]
[34, 45, 56]
>>> S[:]
[12, 23, 34, 45, 56]
```
- **S[ 起始索引(含) i : 結束索引 j : 間隔 k ]**
    - 間隔 k > 0，正向跳躍間隔
    - 間隔 k < 0，反向跳躍間隔
```python=
>>> S = [12, 23, 34, 45, 56, 67, 78, 89]
>>> S[::2]
[12, 34, 56, 78]
>>> S[::-2]
[89, 67, 45, 23]
>>> S[0:7:-2] # 反向須注意順序
[]
>>> S[7:0:-2]
[89, 67, 45, 23]
```

## 序列種類
### 字串(String)
### 元組(tuple)
- **不可變的物件**
- 以 **( )** 表示
```python=
>>> t = (1,2,3)
>>> type(t)
<class 'tuple'>
>>> t[0] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t[0:1]
(1,)
>>> t[0:2]
(1, 2)
```
### 串列(List)
- **串列物件是可變的**，可變長變短。
- 以 **[ ]** 表示
```python=
>>> x = [1,2,3,4,5]
>>> x[1:3]
[2, 3]
>>> x[2] = 10
>>> x
[1, 2, 10, 4, 5]
>>> x[2:4] = [7,8,9]
>>> x
[1, 2, 7, 8, 9, 5]
>>> x[2:4] = [11,12]
>>> x
[1, 2, 11, 12, 9, 5]
>>> x[2:3] = []
>>> x
[1, 2, 12, 9, 5]
>>> del x[3]
>>> x
[1, 2, 12, 5]
```
#### 串列方法
- **L . count( x )**
- **L . index( x )**
- **L . append( x )**
- **L . extend( s )**
- **L . insert( i, x )**
- **L . remove( x )**
- **L . pop( i=-1 )**
- **L . reverse()**

### 串列排序
- **L . sort(key=None, reverse = False)**
- Key 是一個給予判斷的方法，如果沒有提供，預設為原述職的大小判斷。
- 預設為**由小到大**排序，若reverse為True則由大到小排序。
```python=
>>> x = [2, 5, 8, 1, 9, 3, 7, 6, 4]
>>> x.sort()
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.sort(reverse = True)
>>> x
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```
```python=
>>> x = ['apple', 'egg', 'book', 'dog', 'cat']
>>> x.sort()
>>> x
['apple', 'book', 'cat', 'dog', 'egg']
>>> x.sort(key=len)
>>> x
['cat', 'dog', 'egg', 'book', 'apple']
```

### 集合(Set)
- **分為集合(set)與凍結集合(frozened set)**
- 以 **{ }** 表示
- 無索引功能
```python=
>>> x = {100, 3.14, 'apple'}
>>> type(x)
<class 'set'>
>>> x[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> x.add('cat')
>>> x
{'apple', 3.14, 100, 'cat'}
```

### 字典(Dict)
- 索引方式:透過**key值**索引。
- 格式 **{ key : value, ... }**
- 新增 ** D[newkey] = value
- 修改 ** D[oldkey] = value
```python=
>>> d = {'a':10, 'b':3.14, 'c':'cat'}
>>> d['a']
10
>>> d['c']
'cat'
>>> d[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> d['a'] = 100
>>> d['d'] = 'dog'
>>> d
{'a': 100, 'b': 3.14, 'c': 'cat', 'd': 'dog'}
>>> d.keys()
dict_keys(['a', 'b', 'c', 'd'])
>>> d.values()
dict_values([100, 3.14, 'cat', 'dog'])
>>> d.items()
dict_items([('a', 100), ('b', 3.14), ('c', 'cat'), ('d', 'dog')])
```