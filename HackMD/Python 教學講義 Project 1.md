# Python 教學講義 Project 1
[TOC]
###### tags: `python tutorial`

## 網路協定 
### 超文本傳輸協定(HTTP)
全文 **HyperText Transfer Protocol** [維基百科](https://zh.wikipedia.org/zh-tw/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)

### HTTP回應
所有HTTP回應的第一行都是狀態行，依次是當前HTTP版本號，3位數字組成的狀態代碼，以及描述狀態的短語，彼此由空格分隔。
:::info
#### 狀態碼
狀態代碼的第一個數字代表當前回應的類型
```
1xx訊息——請求已被伺服器接收，繼續處理
2xx成功——請求已成功被伺服器接收、理解、並接受
3xx重新導向——需要後續操作才能完成這一請求
4xx請求錯誤——請求含有詞法錯誤或者無法被執行
5xx伺服器錯誤——伺服器在處理某個正確請求時發生錯誤
```
:::
### 客戶端請求
```htmlmixed=
GET / HTTP/1.1
Host: www.google.com
```
### 伺服器應答
```htmlmixed=
HTTP/1.1 200 OK
Content-Length: 3059
Server: GWS/2.0
Date: Sat, 11 Jan 2003 02:44:04 GMT
Content-Type: text/html
Cache-control: private
Set-Cookie: PREF=ID=73d4aef52e57bae9:TM=1042253044:LM=1042253044:S=SMCc_HRPCQiqy
X9j; expires=Sun, 17-Jan-2038 19:14:07 GMT; path=/; domain=.google.com
Connection: keep-alive
```
### 超文本傳輸安全協定(HTTPS)
全文 **HyperText Transfer Protocol Secure** [維基百科](https://zh.wikipedia.org/zh-tw/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE)

:::warning
HTTP不是安全的，而且攻擊者可以透過監聽和中間人攻擊等手段，取得網站帳戶和敏感訊息等。HTTPS的設計可以防止前述攻擊，在正確組態時是安全的。
:::

## 台灣地震資料彙集與繪圖
### [台灣交通部中央氣象局](https://www.cwb.gov.tw/V8/C/)

### 有編號之地震- 地震參數下載
[第076號 7月1日21時32分 規模 4.8 臺東縣政府南南東方 69.9 公里 (位於臺灣東南部海域)](https://scweb.cwb.gov.tw/zh-tw/earthquake/parameters/2022070121320948076)
![](https://i.imgur.com/lhTVmI6.png)

### txt 下載網址
![](https://i.imgur.com/z2auxH8.png)

```
https://scweb.cwb.gov.tw/zh-tw/earthquake/download?file=%2FdrawTrace%2Foutcome%2F2022%2F2022076.txt
```
#### 注意網址後半部
```
file=%2FdrawTrace%2Foutcome%2F2022%2F2022076.txt
```
#### 觀察格式
```
file=%2FdrawTrace%2Foutcome%2F[年分]%2F[年分][編號].txt
```
#### 建立基本網址格式
```python=
base_URL = 'https://scweb.cwb.gov.tw/zh-tw/earthquake/download?'+\
'file=%2FdrawTrace%2Foutcome%2F{:04d}%2F{:04d}{:03d}.txt'

```
字串中的 **{}** 都是代填入的數值
1. **{:04d}**，d表示整數，4表示四位數，0表示不滿四位在前面補0。在此表示年份要填的位置。
2. **{:03d}**，d表示整數，3表示三位數，0表示不滿三位在前面補0。在此表示地震編號要填的位置

#### 生成實際的網址
```python=
year = 2022 # 年分
index = 76  # 編號
URL = base_URL.format(year, year, index) # 網址
```
利用 **format** 將相對應的數值填入字串預留的空位中，產生對應的網址。
```python=
print(URL)
```
```shell=
https://scweb.cwb.gov.tw/zh-tw/earthquake/download?file=%2FdrawTrace%2Foutcome%2F2022%2F2022076.txt
```
### 獲取txt資料
#### requests
我們需要使用**requests**的函式庫來獲取資料
```python=
import requests

response = requests.get(URL) # 回應物件
# 回應物件的文字(string, 解碼格式: ANSI)
Text = response.content.decode('ansi')         
```
將字串以 **換行(\n)** 拆分(將 **\r** 刪除)
```python=
Text_List = Text.replace('\r','').split('\n')
```
print前面幾行資訊
```python=
print(Text_List[0]) # 震央
print(Text_List[1]) # 精度
print(Text_List[2]) # 緯度
print(Text_List[3]) # 深度
print(Text_List[4]) # 規模
```
```shell=
Origin Time:2022/07/01 21:32:09
Lon:121.42°E
Lat:22.17°N
Depth:21.4km
Mag:4.8
```
後面開始為**各處地震觀測站測量資訊**，稱之為**data**。
將data 進行細部的整理。
```python=
# 將Text後面皆視為data
data = Text_List[5:]
# 將每筆data string 以 ',' 分隔開來
data = [d.split(',') for d in data]
# 將每一筆 data 的參數以 '=' 分開成'關鍵字'與'內容'
# 並且削去字串中的空格
data = [[i.replace(' ','').split('=') for i in d] for d in data]
# 將每一筆 data 的參數以'關鍵字'與'內容'的對應方式建立字典
data = [{i[0]:i[1] for i in d if len(i)==2} for d in data]
# 最後檢查，並且刪去空字典
data = [d for d in data if d!={}]
# 輸出整理過後的資料
for d in data:
    print(d)
```
```shell=
{'Stacode': 'LAY', 'Staname': '蘭嶼', 'Stalon': '121.56', 'Stalat': '22.04', 'Dist': '21.00', 'BAZ': '316.12', 'PGA(V)': '18.90', 'PGA(NS)': '42.28', 'PGA(EW)': '52.56', 'PGV(V)': '0.41', 'PGV(NS)': '1.05', 'PGV(EW)': '0.97', 'Int': '4級', 'PGA(SUM)': '35.64', 'PGV(SUM)': '1.16'}
{'Stacode': 'LDU', 'Staname': '綠島', 'Stalon': '121.47', 'Stalat': '22.67', 'Dist': '55.55', 'BAZ': '185.56', 'PGA(V)': '1.18', 'PGA(NS)': '2.02', 'PGA(EW)': '1.82', 'PGV(V)': '0.03', 'PGV(NS)': '0.08', 'PGV(EW)': '0.06', 'Int': '1級', 'PGA(SUM)': '2.17', 'PGV(SUM)': '0.08'}
{'Stacode': 'TAWH', 'Staname': '大武', 'Stalon': '120.89', 'Stalat': '22.34', 'Dist': '57.54', 'BAZ': '108.60', 'PGA(V)': '1.13', 'PGA(NS)': '2.77', 'PGA(EW)': '1.97', 'PGV(V)': '0.02', 'PGV(NS)': '0.06', 'PGV(EW)': '0.05', 'Int': '2級', 'PGA(SUM)': '2.71', 'PGV(SUM)': '0.06'}
{'Stacode': 'SMS', 'Staname': '滿州', 'Stalon': '120.84', 'Stalat': '22.02', 'Dist': '62.21', 'BAZ': '74.13', 'PGA(V)': '2.40', 'PGA(NS)': '9.39', 'PGA(EW)': '9.10', 'PGV(V)': '0.06', 'PGV(NS)': '0.23', 'PGV(EW)': '0.25', 'Int': '3級', 'PGA(SUM)': '11.91', 'PGV(SUM)': '0.30'}
{'Stacode': 'SLIU', 'Staname': '獅子', 'Stalon': '120.80', 'Stalat': '22.22', 'Dist': '63.89', 'BAZ': '94.19', 'PGA(V)': '1.44', 'PGA(NS)': '1.58', 'PGA(EW)': '1.83', 'PGV(V)': '0.03', 'PGV(NS)': '0.05', 'PGV(EW)': '0.05', 'Int': '1級', 'PGA(SUM)': '1.75', 'PGV(SUM)': '0.07'}
{'Stacode': 'SEB', 'Staname': '鵝鑾鼻', 'Stalon': '120.86', 'Stalat': '21.90', 'Dist': '65.40', 'BAZ': '62.46', 'PGA(V)': '0.63', 'PGA(NS)': '1.94', 'PGA(EW)': '1.37', 'PGV(V)': '0.04', 'PGV(NS)': '0.10', 'PGV(EW)': '0.12', 'Int': '1級', 'PGA(SUM)': '1.98', 'PGV(SUM)': '0.15'}
{'Stacode': 'TWK1', 'Staname': '墾丁', 'Stalon': '120.81', 'Stalat': '21.94', 'Dist': '67.43', 'BAZ': '67.42', 'PGA(V)': '0.48', 'PGA(NS)': '0.81', 'PGA(EW)': '0.87', 'PGV(V)': '0.02', 'PGV(NS)': '0.04', 'PGV(EW)': '0.03', 'Int': '1級', 'PGA(SUM)': '0.82', 'PGV(SUM)': '0.04'}
{'Stacode': 'HEN', 'Staname': '恆春', 'Stalon': '120.75', 'Stalat': '22.00', 'Dist': '71.75', 'BAZ': '74.77', 'PGA(V)': '1.03', 'PGA(NS)': '2.50', 'PGA(EW)': '2.77', 'PGV(V)': '0.05', 'PGV(NS)': '0.19', 'PGV(EW)': '0.19', 'Int': '2級', 'PGA(SUM)': '3.08', 'PGV(SUM)': '0.20'}
{'Stacode': 'SNW', 'Staname': '南灣', 'Stalon': '120.75', 'Stalat': '21.96', 'Dist': '72.84', 'BAZ': '71.00', 'PGA(V)': '1.96', 'PGA(NS)': '4.48', 'PGA(EW)': '4.59', 'PGV(V)': '0.10', 'PGV(NS)': '0.13', 'PGV(EW)': '0.22', 'Int': '2級', 'PGA(SUM)': '5.26', 'PGV(SUM)': '0.22'}
{'Stacode': 'EDH', 'Staname': '東河', 'Stalon': '121.30', 'Stalat': '22.97', 'Dist': '89.18', 'BAZ': '172.51', 'PGA(V)': '1.04', 'PGA(NS)': '1.66', 'PGA(EW)': '1.42', 'PGV(V)': '0.03', 'PGV(NS)': '0.05', 'PGV(EW)': '0.05', 'Int': '1級', 'PGA(SUM)': '1.59', 'PGV(SUM)': '0.06'}
{'Stacode': 'SSP', 'Staname': '新埤', 'Stalon': '120.57', 'Stalat': '22.48', 'Dist': '93.91', 'BAZ': '111.40', 'PGA(V)': '1.00', 'PGA(NS)': '0.54', 'PGA(EW)': '0.57', 'PGV(V)': '0.03', 'PGV(NS)': '0.04', 'PGV(EW)': '0.07', 'Int': '1級', 'PGA(SUM)': '0.97', 'PGV(SUM)': '0.07'}
{'Stacode': 'CHK', 'Staname': '成功', 'Stalon': '121.37', 'Stalat': '23.10', 'Dist': '102.40', 'BAZ': '177.47', 'PGA(V)': '0.41', 'PGA(NS)': '1.39', 'PGA(EW)': '1.16', 'PGV(V)': '0.02', 'PGV(NS)': '0.03', 'PGV(EW)': '0.04', 'Int': '1級', 'PGA(SUM)': '1.42', 'PGV(SUM)': '0.04'}
{'Stacode': 'ECS', 'Staname': '池上', 'Stalon': '121.22', 'Stalat': '23.10', 'Dist': '104.03', 'BAZ': '168.73', 'PGA(V)': '0.40', 'PGA(NS)': '0.56', 'PGA(EW)': '0.89', 'PGV(V)': '0.02', 'PGV(NS)': '0.03', 'PGV(EW)': '0.03', 'Int': '1級', 'PGA(SUM)': '0.90', 'PGV(SUM)': '0.04'}

```
**data** 便已準備完成。

### 繪圖
將想呈現的資訊繪製在地圖上以供參考
1. **經緯座標(Stalon, Stalat)** 作為坐標系
2. 觀測站以圓形圖案表示
3. 測站所測之 **最大地動加速度, PGA(SUM)** 以圓形 **半徑大小** 表示
4. 測站所測之 **震度, Int** 以圓形 **顏色** 表示

#### 使用 folium 建立地圖
```python=
import folium
# 顏色定義
color = ['green','green','yellow', 'orange', 'red', 'purple']
# 台灣地理中心座標
Taiwan_center = [23.97565, 120.9738819]
# 世界地圖起始放大倍率
zoom = 8

# 建立地圖物件
fmap = folium.Map(location=Taiwan_center, zoom_start=zoom)
```
**開始繪製地圖**
```python=
# 重複直到每筆偵測站的資料都跑過一遍
for d in data: 
    # 經度
    lon = float(d['Stalon'])
    # 緯度
    lat = float(d['Stalat'])
    # 最大地動加速度
    PGA = float(d['PGA(SUM)'])*200+1500 #數值太小所以乘上倍率
    # 震度
    Int = int(d['Int'][:-1]) # 去掉中文字'級'

    # 顏色選擇
    if Int < len(color):
        c = color[Int] # 在 color list 範圍內
    else:
        c = color[-1] # 在 color list 範圍外則使用最後一個顏色

    # 在地圖物件上加上子物件(Circle)
    fmap.add_child(folium.Circle(location=[lat,lon],
                                 color=c,  # Circle 顏色
                                 radius=PGA,  # Circle 寬度
                                 popup='Skytree',  # 彈出視窗內容
                                 fill=True,  # 填滿中間區域
                                 fill_opacity=0.5  # 設定透明度
                                 ))

# 將地圖資訊存成網頁檔(html)
fmap.save('map.html')
```
地圖資訊會存在 **map.html**裡面，需要用瀏覽器開啟。

### 呈現結果
#### 利用webbrowser自動開啟地圖
```python=
import webbrowser
## 開啟地圖資訊 html
webbrowser.open('map.html')
```
**結果**

![](https://i.imgur.com/E6hdFt6.png)


**結果二**
year = 2022
index = 1

![](https://i.imgur.com/7tMZsXk.png)

