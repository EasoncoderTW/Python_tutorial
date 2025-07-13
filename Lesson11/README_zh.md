# 第十一課：多執行緒、多程序、互斥鎖和信號量

在本課程中，我們將探討 Python 中的並行程式設計概念，重點介紹多執行緒、多程序、互斥鎖和信號量。我們還將討論這些概念的進階主題和實際應用。

## 並行程式設計介紹

並行程式設計涉及同時執行多個操作序列。這可以提高程式的效能，特別是那些執行 I/O 密集型或 CPU 密集型任務的程式。

## 多執行緒

多執行緒允許多個執行緒在單一程序內同時執行，共享相同的記憶體空間。這對於 I/O 密集型任務很有用。

### 範例：多執行緒
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

## 多程序

多程序涉及同時執行多個程序，每個程序都有自己的記憶體空間。這對於 CPU 密集型任務很有用。

### 範例：多程序
```python
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_numbers)

process1.start()
process2.start()

process1.join()
process2.join()
```

## 互斥鎖

互斥鎖（互斥排除）用於防止多個執行緒同時訪問共享資源，這可能導致競態條件。

### 範例：互斥鎖
```python
import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(10000):
        with counter_lock:
            counter += 1

threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'計數器：{counter}')  # 預期輸出：100000
```

## 信號量

信號量是一種同步原語，控制多個執行緒對資源的訪問。它允許有限數量的執行緒同時訪問資源。

### 範例：信號量
```python
import threading
import time

semaphore = threading.Semaphore(2)

def access_resource():
    with semaphore:
        print(f'執行緒 {threading.current_thread().name} 正在訪問資源')
        time.sleep(1)
        print(f'執行緒 {threading.current_thread().name} 釋放資源')

threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

## 進階主題

### 死結
死結發生在兩個或更多執行緒永遠阻塞，等待彼此釋放資源時。

### 避免死結
要避免死結，您可以使用以下技術：
- 鎖定順序：始終以一致的順序獲取鎖定。
- 鎖定超時：獲取鎖定時使用超時。

### 範例：避免死結
```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print('執行緒 1 獲取鎖定 1')
        with lock2:
            print('執行緒 1 獲取鎖定 2')

def thread2():
    with lock2:
        print('執行緒 2 獲取鎖定 2')
        with lock1:
            print('執行緒 2 獲取鎖定 1')

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()
```

## 實際應用

並行程式設計可用於各種應用，例如：
- 處理多個客戶端請求的網路伺服器。
- 資料處理管道。
- 即時系統。

## 練習

### 練習 1：多執行緒
建立一個多執行緒程式，使用兩個執行緒印出 1 到 10 的數字。

### 解答
```python
import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### 練習 2：多程序
建立一個多程序程式，使用兩個程序印出 1 到 10 的數字。

### 解答
```python
import multiprocessing

def print_numbers():
    for i in range(1, 11):
        print(i)

process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_numbers)

process1.start()
process2.start()

process1.join()
process2.join()
```

### 練習 3：互斥鎖
建立一個程式，使用 5 個執行緒增加計數器，通過使用互斥鎖確保計數器值正確。

### 解答
```python
import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000):
        with counter_lock:
            counter += 1

threads = []
for _ in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'計數器：{counter}')  # 預期輸出：5000
```

### 練習 4：信號量
建立一個程式，使用 3 個執行緒模擬訪問共享資源，信號量只允許 2 個執行緒同時訪問資源。

### 解答
```python
import threading
import time

semaphore = threading.Semaphore(2)

def access_resource():
    with semaphore:
        print(f'執行緒 {threading.current_thread().name} 正在訪問資源')
        time.sleep(1)
        print(f'執行緒 {threading.current_thread().name} 釋放資源')

threads = []
for i in range(3):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

理解這些概念及其實際應用將幫助您編寫高效且並行的 Python 程式。

---

## 並行程式設計的實際應用

並行程式設計廣泛應用於各種現實世界的應用中，以提高效能和響應性。在這裡，我們將討論三個主要應用：處理多個客戶端請求的網路伺服器、資料處理管道和即時系統。

### 處理多個客戶端請求的網路伺服器

網路伺服器需要同時處理多個客戶端請求，以有效地提供網頁服務。使用多執行緒或多程序，網路伺服器可以同時管理眾多請求，確保快速的響應時間。

#### 範例：簡單的多執行緒網路伺服器
```python
import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"收到：{request.decode('utf-8')}")
    client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)
print("伺服器正在監聽端口 8080...")

while True:
    client_socket, addr = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
```

### 資料處理管道

資料處理管道通常需要處理大量資料。使用並行程式設計，您可以同時處理資料的不同部分，加速整體處理時間。

#### 範例：多程序資料管道
```python
import multiprocessing

def process_data(data_chunk):
    # 模擬資料處理
    result = sum(data_chunk)
    return result

if __name__ == '__main__':
    data = [i for i in range(1000000)]
    chunk_size = len(data) // 4
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(process_data, chunks)

    total_result = sum(results)
    print(f"總結果：{total_result}")
```

### 即時系統

即時系統，如機器人或嵌入式系統，需要立即處理資料以正確運作。使用並行程式設計，這些系統可以同時處理多個任務，確保及時響應。

#### 範例：多執行緒即時系統
```python
import threading
import time

def sensor_reading():
    while True:
        # 模擬感測器讀取
        print("感測器讀取")
        time.sleep(1)

def actuator_control():
    while True:
        # 模擬致動器控制
        print("致動器控制")
        time.sleep(2)

sensor_thread = threading.Thread(target=sensor_reading)
actuator_thread = threading.Thread(target=actuator_control)

sensor_thread.start()
actuator_thread.start()

sensor_thread.join()
actuator_thread.join()
```

通過理解這些應用並完成練習，您將更深入地了解如何在現實世界場景中利用並行程式設計來增強 Python 程式的效能和響應性。