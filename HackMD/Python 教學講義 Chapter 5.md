# Python 教學講義 Chapter 5
[TOC]
###### tags: `python tutorial`


## 模組(Module)
一個典型的Python程式是由數個原始碼檔案(source file)所構成。每個原始碼檔案都是一個**模組(module)**，將程式碼與資料包成一組以便再利用。

由於模組中常常會描述一些函式的宣告，我們也常稱之為**函式庫**
### 模組主體
一個模組的主體(body)是該模組的原始程式碼檔案(source code file)中一連串的述句。不需要特殊語法來指出一個原始碼檔案是模組。
:::info
**模組主體**的存在是為了繫結模組的**屬性**，
**def** 繫結函式、**class** 繫結類別等等。
:::
### 為什麼要將code分模組?
請看以下範例
**main_1.py**
```python=
def Factorial(N):
    if N<0:
        return 0
    ans = 1
    for i in range(1,N+1):
        ans *= i
    return ans

def Pow(a,b):
    return a**b

def Fibonacci_fast(x):
    history = [0,1]
    if x < 0:
        print("Invallid value")
    if x < 2:
        return history[x]
    else:
        while len(history) < x+1:
            h = history[-1] + history[-2]
            history.append(h)
        return history[x]

def main():
    print(10, "! =", Factorial(10))
    print("Fibonacci",12, "=", Factorial(12))
    print(3,'^',5,"=", Pow(3,5))

if __name__ == "__main__":
    main()
```
**main_2.py**
```python=
def Factorial(N):
    if N<0:
        return 0
    ans = 1
    for i in range(1,N+1):
        ans *= i
    return ans

def Pow(a,b):
    return a**b

def Fibonacci_fast(x):
    history = [0,1]
    if x < 0:
        print("Invallid value")
    if x < 2:
        return history[x]
    else:
        while len(history) < x+1:
            h = history[-1] + history[-2]
            history.append(h)
        return history[x]

def main():
    print(10, "! =", Factorial(10))
    print(9, "! =", Factorial(9))
    print("Fibonacci",8, "=", Fibonacci(8))

if __name__ == "__main__":
    main()
```
由上面兩個程式可以發現**Factorial**、**Fibonacci**等函式常常會使用到，如果集中變成一份程式碼，優點如下:
:::success
1. 將使用到的程式另外寫成一份檔案(**.py**)，可以方便讓其他程式重複利用，不必每次寫新的程式都打一遍。
2. 我們將集合成一份檔案的函式稱做一個模組，如此一來只需要寫一份模組，在任何地方只要匯入它，便可使用裡面的函式。
3. 由於模組只是一個檔案，如果原先設計的函式有需要修正，或是需要新增功能(函式)，也只需要在該檔案中修改或新增，達到**方便管理程式碼**的效果。
4. 由於函式的宣告都另外寫成一份檔案了，原先的main.py就會變得比較精簡，一目了然。
:::
#### 將程式整理的結果

**Func_tion.py**
```python=
def Factorial(N):
    if N<0:
        return 0
    ans = 1
    for i in range(1,N+1):
        ans *= i
    return ans

def Pow(a,b):
    return a**b

def Fibonacci_fast(x):
    history = [0,1]
    if x < 0:
        print("Invallid value")
    if x < 2:
        return history[x]
    else:
        while len(history) < x+1:
            h = history[-1] + history[-2]
            history.append(h)
        return history[x]

```
**main_1.py**
```python=
import Func_tion

def main():
    print(10, "! =", Func_tion.Factorial(10))
    print("Fibonacci",12, "=", Func_tion.Factorial(12))
    print(3,'^',5,"=", Func_tion.Pow(3,5))

if __name__ == "__main__":
    main()
```
**main_2.py**
```python=
import Func_tion

def main():
    print(10, "! =", Func_tion.Factorial(10))
    print(9, "! =", Func_tion.Factorial(9))
    print("Fibonacci",8, "=", Func_tion.Fibonacci(8))

if __name__ == "__main__":
    main()
```
### import module
可以將模組從現行目錄中匯入進來，納入範疇。
方式:
```python=
import [module name]
```
範例

:::info
**module.py**
```python=
def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    if __name__ == 'module':
        print("Using this file as a module.")
    if __name__=='__main__':
        print('Usnig this file as a main.')
    return

def Factorial(N):
    if N<0:
        return 0
    ans = 1
    for i in range(1,N+1):
        ans *= i
    return ans

def main():
    print("Test Factorial Function.")
    n = 10
    print(n,"! =",Factorial(n))
    return

info()
if __name__ == '__main__':
    main()

```
單純執行module.py
```shell=
__name__ = __main__
__file__ = E:/CODE/PycharmProjects/lesson1/module.py
Usnig this file as a main.
Test Factorial Function.
10 ! = 3628800
```
**\_\_name\_\_** : 該模組在程式中的名稱，因為現在是將模組視為主程式，因此為"\_\_main\_\_"
**\_\_file\_\_** : 該模組的檔案位置
**info()** : 用於輸出該模組的參數狀態
:::

:::info
**main.py**
```python=
import module

# 主程式
def main():
    print("Test Factorial Function.")
    n = 10
    print(n, "! =", module.Factorial(n))
    return

if __name__ == "__main__":
    main()
```
以**mian.py**作為主程式，並將**module.py**視為模組匯入到**命名空間(namespace)** 中
使用**module.py**函式時需要以 **[模組].[函式]** 的方式呼叫
```shell=
__name__ = module
__file__ = E:\CODE\PycharmProjects\lesson1\module.py
Using this file as a module.
Test Factorial Function.
10 ! = 3628800
```
此時 module.py 被視為模組所以__name__為模組名稱
，檔案位置相同。
:::
### import A as B
如果模組的名稱不方便撰寫(名稱過長或不易辨識)，可以使用 **as** 將**A模組**在命名空間中以**B名稱**存在。但是__name__依然為原名稱。
```python=
import Func_tion as F
...
print(F.Pow(3,5)) ## F means Func_tion
...
```
### from A import B
由於**A模組**中有許多Funtion，甚至是許多屬性。
但目前你只想使用其中一個函式而已，我們就可以使用該述句單獨將該函式匯入到命名空間當中。
如此在使用時只需要呼叫 **[函式名稱]** 即可，不需要撰寫 **[模組].[函式]**
```python=
## main.py
# only import Factorial function
from module import Factorial

# 主程式
def main():
    print("Test Factorial Function.")
    n = 10
    ## only call function name
    print(n, "! =", Factorial(n)) 
    return

if __name__ == "__main__":
    main()
```
```shell=
__name__ = module
__file__ = E:\CODE\PycharmProjects\lesson1\module.py
Using this file as a module.
Test Factorial Function.
10 ! = 3628800
```
#### namespace override (命名空間覆寫)
如果出現**一樣的函式名稱**在不同的模組之中，如下。
:::info
```python=
## test.py

def test_print():
    print("test_print function in",__name__)
```
```python=
## test2.py

def test_print():
    print("test_print function in",__name__)
```
:::
但它們卻又被import到同一個namespace中(例如main Program的namespace)，有以下兩個現象。
:::success
1. 使用 import 將整個模組匯入進來，由於模組名稱不同，因此可以分開呼叫。
```python=
## main.py 

import test1
import test2

# 主程式
def main():
    test1.test_print()
    test2.test_print()
    return

if __name__ == "__main__":
    main()
```
```shell=
test_print function in test1
test_print function in test2
```
:::
:::warning
2. 如果是用 **from module import function** 的方式，則會以**最後敘述**的模組**覆蓋**前面的namespace。
```python=
## main.py 

from test1 import test_print
from test2 import test_print

# 主程式
def main():
    test_print()
    return

if __name__ == "__main__":
    main()
```
```shell=
test_print function in test2
``` 
同樣的，如果有相同的module name被import，最後import的module會代表module name 所匯入的模組。
:::
#### from A import *
如果今天大部分的function都需要用到，但是想省略寫module的名稱，該敘述可以達到目的。
:::info
**from A import \*** 表示把A模組中的所有屬性跟函式都import到現行的namespace中，方便呼叫。
```python=
from A import F1
from A import F2
from A import F3
```
```python=
from A import *
```
:::

### if \_\_name__ == "\_\_main__"
這是一個確認是否檔案被視為主程式而執行的慣用語。
:::info
**Main function**
主程式，也是一個程式的起始點(Entry)
慣例以下方描述所撰寫
```python=
import ...

def function(...):
    statement(s)...

def main():
    statement(s)...

## code entry
if __name__ == "__main__":
    main()
    
```
通常在模組中使用main function主要是為了做**單元測試(Unit Test)**
:::
### 避免循環匯入
:::danger
盡量避免以下的循環匯入，容易導致錯誤與管理上的困難。
```python=
## module A.py
import B
...
```
```python=
## module B.py
import A
...
```
:::

## 套件(Package)
一個套件(Package)式含有其他模組的一個模組。
```
Package
    | - __init__.py (Package 主體，必須存在)
    | - Module1.py
    | - Module2.py
    | - Module3.py
    | - SubPackage1
            | -  __init__.py (SubPackage1 主體，必須存在)
            | - Module4.py
            | - Module5.py
    | - SubPackage2
            | -  __init__.py (SubPackage2 主體，必須存在)
            | - Module6.py
            | - Module7.py
```
### \_\_init__.py
假設P為一個套件的名稱，則P的模組主體位在檔案P/\_\_init\_\_.py中。這個檔案**必須**存在，即使它空的(代表一個空的模組主體)，**以告知python目錄確實是一個套件**。
:::info
**\_\_init__.py 的用途**
可以自動將其他需要的模組或套件也匯入
```python=
# package
# __init__.py
import re
import urllib
import sys
import os
```
匯入package時
```python=
# main.py
import package 
print(package.re, package.urllib, package.sys, package.os)
```
**全域變數 \_\_all__**
可以選擇性的決定python執行**from Package import \*** 會有什麼動作。
```python=
# package
# __init__.py
__all__ = ['os', 'sys', 're', 'urllib']
```
```python=
# main.py
from package import *
# import os, sys, re ,urllib
```
**\_\_path__**
字串組成的串列，指的是目前package所在的目錄。
:::

### Package 使用範例
```
Project Folder
| - main.py
| - P
    | - __init__.py 
    | - M1.py
    | - M2.py
    | - P2
        | -  __init__.py 
        | - M3.py
        | - M4.py

```
:::info
**P/\_\_init__.py**
:::spoiler
```python=
__all__ = ['M1','M2','P2']

def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    print('__path__ =',__path__)
    if __name__ !='__main__':
        print("Using this file as a package.\n")
    return

info()
```
:::
:::info
**P/M1.py**
:::spoiler
```python=
def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    if __name__ =='__main__':
        print("Using this file as a main.\n")
    else:
        print('Usnig this file as a module.\n')
    return

def test_print():
    print("test_print function in",__name__)


def main():
    test_print()
    return

info()
if __name__ == '__main__':
    main()

```
:::
:::info
**P/M2.py**
:::spoiler
```python=
def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    if __name__ =='__main__':
        print("Using this file as a main.\n")
    else:
        print('Usnig this file as a module.\n')
    return

def test_print():
    print("test_print function in",__name__)


def main():
    test_print()
    return

info()
if __name__ == '__main__':
    main()

```
:::
:::info
**P/P2/\_\_init__.py**
:::spoiler
```python=
__all__ = ['M3', 'M4']

def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    print('__path__ =',__path__)
    if __name__ !='__main__':
        print("Using this file as a package.\n")
    return

info()
```
:::
:::info
**P/P2/M3.py**
:::spoiler
```python=
def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    if __name__ == '__main__':
        print("Using this file as a main.\n")
    else:
        print('Usnig this file as a module.\n')
    return

def test_print():
    print("test_print function in",__name__)


def main():
    test_print()
    return

info()
if __name__ == '__main__':
    main()

```
:::
:::info
**P/P2/M4.py**
:::spoiler
```python=
def info():
    print('__name__ =',__name__)
    print('__file__ =',__file__)
    if __name__ == '__main__':
        print("Using this file as a main.\n")
    else:
        print('Usnig this file as a module.\n')
    return

def test_print():
    print("test_print function in",__name__)


def main():
    test_print()
    return

info()
if __name__ == '__main__':
    main()

```
:::
:::info
**main.py**
```python=
from P import *
from P.P2 import *

# 主程式
def main():
    M1.test_print()
    M2.test_print()
    M3.test_print()
    M4.test_print()
    return

if __name__ == "__main__":
    main()
```
:::
**輸出結果**
:::success
run main.py
```shell=
__name__ = P
__file__ = E:\CODE\PycharmProjects\lesson1\P\__init__.py
__path__ = ['E:\\CODE\\PycharmProjects\\lesson1\\P']
Using this file as a package.

__name__ = P.M1
__file__ = E:\CODE\PycharmProjects\lesson1\P\M1.py
Usnig this file as a module.

__name__ = P.M2
__file__ = E:\CODE\PycharmProjects\lesson1\P\M2.py
Usnig this file as a module.

__name__ = P.P2
__file__ = E:\CODE\PycharmProjects\lesson1\P\P2\__init__.py
__path__ = ['E:\\CODE\\PycharmProjects\\lesson1\\P\\P2']
Using this file as a package.

__name__ = P.P2.M3
__file__ = E:\CODE\PycharmProjects\lesson1\P\P2\M3.py
Usnig this file as a module.

__name__ = P.P2.M4
__file__ = E:\CODE\PycharmProjects\lesson1\P\P2\M4.py
Usnig this file as a module.

test_print function in P.M1
test_print function in P.M2
test_print function in P.P2.M3
test_print function in P.P2.M4

```
:::
## 總結
無論是Module或是Package的產生都是為了將專案結構化，以利於程式碼的閱讀與管理，善加利用這些功能對於開發套件很有幫助。