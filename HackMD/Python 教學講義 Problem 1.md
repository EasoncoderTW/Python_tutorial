# Python 教學講義 Problem 1
[TOC]
###### tags: `python tutorial`


## 八個皇后 (Eight Queens)
關鍵字: **稀疏矩陣** 、 **遞迴函式**
### 題目描述
[維基百科](https://zh.wikipedia.org/zh-tw/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98)

八皇后問題是一個以西洋棋為背景的問題：如何能夠在8×8的西洋棋棋盤上放置八個皇后，使得任何一個皇后都無法直接吃掉其他的皇后？為了達到此目的，任兩個皇后都不能處於同一條橫行、縱行或斜線上。八皇后問題可以推廣為更一般的n皇后擺放問題：這時棋盤的大小變為n×n，而皇后個數也變成n。若且唯若n = 1或n ≥ 4時問題有解。

![](https://i.imgur.com/tqMME91.png =x250)

### 稀疏矩陣
:::warning
仔細觀察如果我們以8x8的二維矩陣去儲存棋盤資料，會有許多空間是浪費的
```python=
chessboard = [
    [0,0,0,0,0,1,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1],
    [0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,0]
]
```
:::
:::success
實際上我們只需要儲存8個皇后所在的位置即可，這就是所謂的**稀疏矩陣**。
```python=
queens = [
  [0,5],  
  [1,3],  
  [2,6],  
  [3,0],  
  [4,7],  
  [5,1],  
  [6,4],  
  [7,2]
] ## [y,x]
```
仔細觀察，每一個橫排上只會有一個皇后，那皇后的位址紀錄只需要記錄她在直排的位置即可。
```python=
queens = [5, 3, 6, 0, 7, 1, 4, 2] 
## queens[y] = x
```
```
queens[y] = x
queens[0] = 5
表示y=0的橫排上，有一個皇后在 x=5的位置上。
```
當棋盤上沒有皇后時，以 **-1**表示
```python=
queens = [-1,-1,-1,-1,-1,-1,-1,-1] 
```
:::
### 題目拆解
如果一個橫排只能填一個皇后，所以可以將一個橫排的所有可能都試一遍。
但是把所有可能都排出來再挑選會花很多時間，所以我們產生了一種演算法
:::info
1. 由上而下擺放皇后
2. 擺放過的橫排上皇后不會違反規則
3. 每次放下一個皇后後，確認是否有衝突，若無則進入下一個橫排。如果有衝突，更換現在這排的皇后位置。
4. 如果8排皇后都排好了，且沒有發生衝突，則輸出下棋盤的樣子，並且將解法計數+1。
5. 如果一個橫排上沒有解(放哪裡都衝突)，或是已經歷遍(有解，且都輸出完了)，則回到前一個橫排的皇后繼續進行調動。
:::

### 重複做的事 - 遞迴函式
:::info
#### 超參數
```python=
QUEENS_NUM = 8 # total queens num
QUEENS_COUNT = 0 # solution count
```
:::
我們將每一橫排要測試擺放的流程作為遞迴函式的內容，以**y**參數表示目前要擺放的橫排。
:::info
#### 終止提條件與動作
1. 終止條件: 如果8排都擺完了，也就是y=8
2. 動作: 輸出下棋盤的樣子，並且將解法計數+1
```python=
def EightQueen(y, q):
    global QUEENS_COUNT # Need Globalized
    if y >= QUEENS_NUM:
        QUEENS_COUNT += 1
        Print_Board(q)  # print chess board function
    else:
        ...
    return
```
```
參數 y -> 目前橫排的index，也是q[y] = x 的 y
參數 q -> 一維稀疏矩陣(queens)，記錄當下棋盤的擺放狀態。 
```
:::
如果沒有到達終止條件，則會繼續測試下一橫排的可能位置。
:::info
#### 衝突判斷與遞迴呼叫
1. 當填入新皇后時，需判斷當下的棋盤是否產生衝突，如果有衝突，就換下一個位置測試。
2. 如果沒有發生衝突，表示當下的棋盤是合理的，則呼叫下一層的運作，將棋盤與橫排資訊傳入下一層(**遞迴函式**)。
3. 如果該橫排上的位置都測試完一遍，則將皇后移除，回到上一層的狀態，並退回上層。
```python=
def EightQueen(y, q):
    ...
    else:
        for i in range(QUEENS_NUM):
            q[y] = i # put queen
            if violate(q): # check violate function
                # if violate, continue the for loop
                continue 
            else:
                # if not, call function to put the queen of next line
                EightQueen(y+1,q)  
        # reset
        q[y] = -1
    
    # return to the previous status
    return
```
:::
### 補充函式 - Print_Board
剛剛需要用的**Print_Board**要在此實現。
:::info
#### Print_Board
將其列印出來(Q 是 queen list)
```python=
## print ChessBoard
def Print_Board(Q):
    print('='*(QUEENS_NUM-3)+"Board"+'='*(QUEENS_NUM-3))
    for q in Q:
        if q == -1:
            print('. '*QUEENS_NUM)
        else:
            print('. '*(q)+'Q '+'. '*(QUEENS_NUM-q-1))
```
**範例結果**
```shell=
=====Board=====
. . . . . . . Q
. . . Q . . . .
Q . . . . . . .
. . Q . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . . . Q .
. . . . Q . . .
```
:::
### 補充函式 - violate
剛剛需要用的**violate**要在此實現。
:::info
#### violate
判斷當下的棋盤是否有衝突(Q 是 queen list)
只要抓到一個衝突就直接**return True**

1. 首先檢查是否有直排上的衝突。
    - 如果直排上有衝突，那Q所記錄的正數數值會重複。
    - 因此計算Q中 0~(QUEENS_NUM-1) 的出現次數，如果有出現過大於1次，則引發衝突。
```python=
## print ChessBoard
# violate detect
def violate(Q):
    # check | violate
    C = [Q.count(i) for i in range(QUEENS_NUM)]
    # more then one in the same column
    if max(C) > 1:
        #print("| violate")
        return True
```
2. 檢查斜角是否有衝突。
    - 將Q中的任兩個橫排進行比對，如果有衝突直接**return True**
    - **y_1、y_2**表示兩個橫排的編號。
    - **Q[y_1]、Q[y_2]** 表示兩個橫排皇后的的位置。
    - 如果皇后不存在，就換下一個橫排做比較。
    - 兩個座標 **(Q[y_1],y_1)、(Q[y_2],y_1)**
    - **斜率 = 1** 衝突，**(Q[y_1]-Q[y_2]) == (y_1 - y_2)**
    - **斜率 = -1** 衝突，**(Q[y_1]-Q[y_2]) == (y_2 - y_1)**
```python=
    # check / violate and \ violate
    for y_1 in range(QUEENS_NUM):
        if Q[y_1] == -1:
            continue
        for y_2 in range(y_1+1,QUEENS_NUM):
            if Q[y_2] == -1:
                continue
            # if / violate
            if (Q[y_1]-Q[y_2]) == (y_1 - y_2):
                #print("/ violate")
                return True
            # if \ violate
            if (Q[y_1]-Q[y_2]) == (y_2 - y_1):
                #print("\ violate")
                return True
```
3. 都沒有衝突，**return False**
```python=
    # all pass, no violate
    return False
```
:::
### 主程式 - Main function
將棋盤紀錄重置好，並呼叫**EightQueen**進行分析。
最後輸出不同解的總數。
```python=
def main():
    # Initial
    queens = [-1,-1,-1,-1,-1,-1,-1,-1]
    EightQueen(0, queens)
    print("Finish. Total",QUEENS_COUNT,'solutions.')

if __name__ == '__main__':
    main()
```
### 完整 Python Code
:::info
:::spoiler

```python=
## Eight Queens
QUEENS_NUM = 8
QUEENS_COUNT = 0

# violate detect
def violate(Q):
	# check | violate
	C = [Q.count(i) for i in range(QUEENS_NUM)]
	# more then one in the same column
	if max(C) > 1:
		#print("| violate")
		return True

	# check / violate and \ violate
	for y_1 in range(QUEENS_NUM):
		if Q[y_1] == -1:
			continue
		for y_2 in range(y_1+1,QUEENS_NUM):
			if Q[y_2] == -1:
				continue
			# if / violate
			if (Q[y_1]-Q[y_2]) == (y_1 - y_2):
				#print("/ violate")
				return True
			# if \ violate
			if (Q[y_1]-Q[y_2]) == (y_2 - y_1):
				#print("\ violate")
				return True

	# all pass, no violate
	return False

## print ChessBoard
def Print_Board(Q):
	print('='*(QUEENS_NUM-3)+"Board"+'='*(QUEENS_NUM-3))
	for q in Q:
		if q == -1:
			print('. '*QUEENS_NUM)
		else:
			print('. '*(q)+'Q '+'. '*(QUEENS_NUM-q-1))

def EightQueen(y, q):
	global QUEENS_COUNT
	if y >= QUEENS_NUM:
		QUEENS_COUNT += 1
		Print_Board(q)
	else:
		for i in range(QUEENS_NUM):
			q[y] = i
			if violate(q):
				continue
			else:
				EightQueen(y+1,q)
		# reset
		q[y] = -1
	return

def main():
	# Initial
	queens = [-1,-1,-1,-1,-1,-1,-1,-1]
	EightQueen(0, queens)
	print("Finish. Total",QUEENS_COUNT,'solutions.')

if __name__ == '__main__':
	main()
```
:::

### 結果呈現
:::success
:::spoiler

```shell=
=====Board=====
Q . . . . . . . 
. . . . Q . . . 
. . . . . . . Q 
. . . . . Q . . 
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
=====Board=====
Q . . . . . . .
. . . . . Q . .
. . . . . . . Q
. . Q . . . . .
. . . . . . Q .
. . . Q . . . .
. Q . . . . . .
. . . . Q . . .

~
~
~

=====Board=====
. . . . . . . Q
. . Q . . . . .
Q . . . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . Q . . .
. . . . . . Q .
. . . Q . . . .
=====Board=====
. . . . . . . Q
. . . Q . . . .
Q . . . . . . .
. . Q . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . . . Q .
. . . . Q . . .
Finish. Total 92 solutions.

```
:::

### 延伸討論
#### 翻轉、旋轉、鏡像重複
如果將翻轉、旋轉、鏡像重複的樣式也合併，解會變成幾種呢?