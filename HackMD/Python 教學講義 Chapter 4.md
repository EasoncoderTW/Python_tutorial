# Python 教學講義 Chapter 4
[TOC]
###### tags: `python tutorial`


## 函式(function)

### 函式是什麼?
- 函式可以說是一種方程式，像數學的方程式一樣，將給予的數值經過一系列的運算過後，得到一個或事物個運算的結果。
```
f(x,y)  = x^2 + y^2
g(x) = x^2 + 2x + 1
h(y) = x*y
```
- 當部分的程式碼會在程式的許多不連續處被使用到，可以將其包裝成函式來使用，方便撰寫與除錯，也可以增加程式的**可讀性**。(如果連續重複可以用迴圈化簡處理)
- 範例
```python=
person_count = 0

s1 = str(input("Enter Data: ")).split()

name =s1[0]
age = int(s1[1])
city = s1[2]
person_count += 1

print("person",person_count)
print("name",name)
print("city",city)
print("age",age)

s2 = str(input("Enter Data: ")).split()

name =s2[0]
age = int(s2[1])
city = s2[2]
person_count += 1

print("person",person_count)
print("name",name)
print("city",city)
print("age",age)

s3 = str(input("Enter Data: ")).split()

name =s3[0]
age = int(s3[1])
city = s3[2]
person_count += 1

print("person",person_count)
print("name",name)
print("city",city)
print("age",age)

```
- 建立函式後的寫法
```python=
# 函式定義

# 讀取資料輸入並分析拆解
def get_data():
    s = str(input("Enter Data: ")).split()
    name = s[0]
    age = int(s[1])
    city = s[2]
    return name, age, city

# 將資訊輸出呈現
def show_data(pc, name, age, city):
    print("person",pc)
    print("name",name)
    print("city",city)
    print("age",age)
    return

# 使用方式
person_count = 0
# data 1
person_count += 1
name, age, city = get_data()
show_data(person_count, name, age, city)
# data 2
person_count += 1
name, age, city = get_data()
show_data(person_count, name, age, city)
# data 3
person_count += 1
name, age, city = get_data()
show_data(person_count, name, age, city)

```
### 函式的宣告 def
:::info
- 函式的宣告架構(特徵式)
```python=
def function_name(parameters):
    statement(s)
    return return_values
```
:::
- **parameter 參數**
    參數可稱為傳入值，也就是從**呼叫端(Caller)** 給予 **被呼叫的函式(Collee)** 的資訊。
- **return valuse 回傳值**
    將運算完的資訊傳回。
:::warning
不必擔心資料傳遞的問題，電腦會自行銜接起來，但是如果銜接不上，電腦會提出例外(像是傳入值宣告時應該有三個，但是使用時只有傳入兩個)。
:::

### 函式的使用
- **呼叫(Call)**
    當想要使用宣告好的函式時，我們稱這個動作叫做**呼叫**。
呼叫方式如下。
```python=
...
result = function_name(parameters)
...
```
- **parameter**是給予函式的參數。
- **result**是用來承接函式的回傳結果。

### 參數的細節 (More detail about parameters)
:::info
參數的擺放須按照以下規則:
```python=
def function_name(positional,...,*args,keyword-only...,**kwargs):
```
:::
#### 位置引數 (positional)
- 非常一般的參數，呼叫時可不必註記參數名稱。

#### 額外位置引述(*args，不具名)
- 沒有明確指定在特徵式中
- 不具參數名稱
- 會被集中在一個元組當中(有可能為空)

#### 僅限關鍵字引數(keyword-only)
- 當有傳入值時需標明關鍵字與參數，否則會產生例外

#### 額外位置具名引述(*kwargs，具名)
- 沒有明確指定在特徵式中
- 具有參數名稱
- 會被集中在一個字典當中({keyword:value})(有可能為空)

:::info
- 範例
```python=
def function(a,b,c = 10,*args,d,e = 12,**kwargs):
    print('< Parameter >')
    print('a',a)
    print('b',b)
    print('c',c)
    print('*args',args)
    print('d',d)
    print('e',e)
    print('**kwargs',kwargs)
```
:::
:::success
- 呼叫 1 (全寫)
```python=
function(1,2,3,4,5,d=10,e=11,k=13,z=20)
```
```shell=
< Parameter >
a 1
b 2
c 3
*args (4, 5)
d 10
e 11
**kwargs {'k': 13, 'z': 20}
```
:::
:::success
- 呼叫 2 (只給定必要參數)
```python=
function(1,2,d=10)
```

```shell=
< Parameter >
a 1
b 2
c 10
*args ()
d 10
e 12
**kwargs {}
```
:::
:::danger
- 呼叫 3 (keyword-only 少給無預設值的 d)
```python=
function(1,2,3,4,5,10,k=13,z=20)
```
```shell=
Traceback (most recent call last):
  File "E:/CODE/PycharmProjects/lesson1/venv/test.py", line 11, in <module>
    function(1,2,3,4,5,10,k=13,z=20)
TypeError: function() missing 1 required keyword-only argument: 'd'
```
:::
:::danger
- 呼叫 4 (positional 少給無預設值的 b)
```python=
function(1,d=10,k=13,z=20)
```
```shell=
Traceback (most recent call last):
  File "E:/CODE/PycharmProjects/lesson1/venv/test.py", line 11, in <module>
    function(1,d=10,k=13,z=20)
TypeError: function() missing 1 required positional argument: 'b'
```
:::
## 命名空間 (namespace)

### 區域命名空間(Local namespace)
- 又稱**區域範疇(Local scope)**
- 在該空間底下的變數也可稱為**區域變數(Local Variables)**

### 全域變數(Global Variables)
- 非區域的變數(模組中的任何位置都可以存取)
- 又稱**模組物件(module object)的屬性**

```python=
c = 30
def function():
    a = 10
    b = 20
    return a+b
```
1. a跟b為functionc函式中的區域變數
2. c為全域變數

### global
- 可以連結將區域範疇中的變數跟全域變數連結(不良的實務做法)
```python=
global variable
```
:::danger
- **沒事的話避開使用global**
:::

## 函式的應用
### 遞迴函式 (Recusion)

#### 數學上的遞迴
- **費波那契數列的遞迴表示法**

:::info
F(0)=0
F(1)=1
F(n) = F(n-1) + F(n-2), n>=2
:::

:::info
- **F(4)展開**
F(4) 
= F(3)+F(2)
= F(2)+F(1)+F(1)+F(0)
= F(1)+F(0)+F(1)+F(1)+F(0)
= 3F(1)+2F(0)
:::
- 每一個運算都是拆分運算後的結果相加

#### 程式上遞迴的架構
:::info
- 透過呼叫函式自己本身達到遞迴的目的
- 呼叫後，原先的變數會被存放至堆疊空間(stack)中，等到retrun後才會復原。
- 每呼叫一次自身函式，可以想像成多一層的運算，多一個遞迴深度的運算。
```python=
def Recusive_function(parameter(s)):
    if stop_recusive_condition: # stop condition
        statement(s)
        return
    else:
        statement(s)
        Recusive_function(parameter(s)) # Call function it self
        statement(s)
        return
```
:::
:::danger
- **必須要有遞迴停止的條件限制!!!**，否則會進入無底洞的深淵，甚至占用記憶體到電腦當機。
- python預設當遞迴深度超過1000時會中斷並提出一個例外(RecursionError)。
```python=
def Recursion(x):
    print("level",x)
    try:
        Recursion(x+1)
    except RecursionError:
        print('\nRecursionLimitExceeded')
        print(RecursionError)
    print("out level" ,x)
    return

Recursion(0)
```
```shell=
level 0
level 1
level 2
level 3
...
level 994
level 995
level 996
level 997
RecursionError
<class 'RecursionError'>
out level 996
out level 995
out level 994
out level 993
...
out level 3
out level 2
out level 1
out level 0
```
:::
#### 實作費波那契遞迴函式
- 遞迴終止條件:參數為0或1的時候，因為這是已知的答案，不需要再運算。
```python=
def Fibonacci(x):
    if x < 0:
        print("Invallid value")
    if x == 0:
        return 0
    if x == 1:
        return 1
    return Fibonacci(x-1) + Fibonacci(x-2)

print(Fibonacci(4))
```
```shell=
3
```
:::success
- 透過print更多資訊去觀察遞迴的運作
```python=
def Fibonacci(level,x):
    print('|  '*level+'|--'+'x =',x, end=" -> ") # info
    if x < 0:
        print("Invallid value") # info
    if x == 0:
        print("return 0") # info
        return 0
    if x == 1:
        print("return 1") # info
        return 1

    print("Recursion call") # info
    r = Fibonacci(level+1,x-1) + Fibonacci(level+1,x-2)
    print('|  '*level+'|--'+'x =',x, 'return',r) # info
    return r

print(Fibonacci(0,4))
```
```shell=
|--x = 4 -> Recursion call
|  |--x = 3 -> Recursion call
|  |  |--x = 2 -> Recursion call
|  |  |  |--x = 1 -> return 1
|  |  |  |--x = 0 -> return 0
|  |  |--x = 2 return 1
|  |  |--x = 1 -> return 1
|  |--x = 3 return 2
|  |--x = 2 -> Recursion call
|  |  |--x = 1 -> return 1
|  |  |--x = 0 -> return 0
|  |--x = 2 return 1
|--x = 4 return 3
3
```

:::