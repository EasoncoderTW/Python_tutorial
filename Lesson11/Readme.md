# Lesson 11: Multi-Threading, Multi-Processing, Mutex, and Semaphores

In this lesson, we will explore concurrent programming concepts in Python, focusing on multi-threading, multi-processing, mutexes, and semaphores. We will also discuss advanced topics and practical applications of these concepts.

## Introduction to Concurrent Programming

Concurrent programming involves executing multiple sequences of operations simultaneously. This can improve the performance of programs, especially those that perform I/O-bound or CPU-bound tasks.

## Multi-Threading

Multi-threading allows multiple threads to run concurrently within a single process, sharing the same memory space. This is useful for I/O-bound tasks.

### Example: Multi-Threading
```pythond
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

## Multi-Processing

Multi-processing involves running multiple processes concurrently, with each process having its own memory space. This is useful for CPU-bound tasks.

### Example: Multi-Processing
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

## Mutex

A mutex (mutual exclusion) is used to prevent multiple threads from accessing shared resources simultaneously, which can cause race conditions.

### Example: Mutex
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

print(f'Counter: {counter}')  # Expected output: 100000
```

## Semaphores

A semaphore is a synchronization primitive that controls access to a resource by multiple threads. It allows a limited number of threads to access the resource concurrently.

### Example: Semaphores
```python
import threading
import time

semaphore = threading.Semaphore(2)

def access_resource():
    with semaphore:
        print(f'Thread {threading.current_thread().name} accessing resource')
        time.sleep(1)
        print(f'Thread {threading.current_thread().name} releasing resource')

threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

## Advanced Topics

### Deadlocks
A deadlock occurs when two or more threads are blocked forever, waiting for each other to release resources.

### Avoiding Deadlocks
To avoid deadlocks, you can use techniques such as:
- Lock ordering: Always acquire locks in a consistent order.
- Lock timeout: Use timeouts when acquiring locks.

### Example: Avoiding Deadlocks
```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print('Thread 1 acquired lock 1')
        with lock2:
            print('Thread 1 acquired lock 2')

def thread2():
    with lock2:
        print('Thread 2 acquired lock 2')
        with lock1:
            print('Thread 2 acquired lock 1')

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()
```

## Practical Applications

Concurrent programming can be used in various applications, such as:
- Web servers handling multiple client requests.
- Data processing pipelines.
- Real-time systems.

## Exercises

### Exercise 1: Multi-Threading
Create a multi-threaded program that prints numbers from 1 to 10 using two threads.

### Solution
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

### Exercise 2: Multi-Processing
Create a multi-processing program that prints numbers from 1 to 10 using two processes.

### Solution
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

### Exercise 3: Mutex
Create a program that increments a counter using 5 threads, ensuring that the counter value is correct by using a mutex.

### Solution
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

print(f'Counter: {counter}')  # Expected output: 5000
```

### Exercise 4: Semaphores
Create a program that simulates accessing a shared resource using 3 threads, with a semaphore allowing only 2 threads to access the resource concurrently.

### Solution
```python
import threading
import time

semaphore = threading.Semaphore(2)

def access_resource():
    with semaphore:
        print(f'Thread {threading.current_thread().name} accessing resource')
        time.sleep(1)
        print(f'Thread {threading.current_thread().name} releasing resource')

threads = []
for i in range(3):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

Understanding these concepts and their practical applications will help you write efficient and concurrent Python programs.

---

## Practical Applications of Concurrent Programming

Concurrent programming is widely used in various real-world applications to improve performance and responsiveness. Here, we will discuss three major applications: web servers handling multiple client requests, data processing pipelines, and real-time systems.

### Web Servers Handling Multiple Client Requests

Web servers need to handle multiple client requests simultaneously to serve web pages efficiently. Using multi-threading or multi-processing, a web server can manage numerous requests at the same time, ensuring a fast response time.

#### Example: Simple Multi-Threaded Web Server
```python
import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received: {request.decode('utf-8')}")
    client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)
print("Server listening on port 8080...")

while True:
    client_socket, addr = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
```

### Data Processing Pipelines

Data processing pipelines often require handling large volumes of data. Using concurrent programming, you can process different parts of the data simultaneously, speeding up the overall processing time.

#### Example: Multi-Processing Data Pipeline
```python
import multiprocessing

def process_data(data_chunk):
    # Simulate data processing
    result = sum(data_chunk)
    return result

if __name__ == '__main__':
    data = [i for i in range(1000000)]
    chunk_size = len(data) // 4
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(process_data, chunks)
    
    total_result = sum(results)
    print(f"Total result: {total_result}")
```

### Real-Time Systems

Real-time systems, such as robotics or embedded systems, require immediate processing of data to function correctly. Using concurrent programming, these systems can handle multiple tasks simultaneously, ensuring timely responses.

#### Example: Multi-Threaded Real-Time System
```python
import threading
import time

def sensor_reading():
    while True:
        # Simulate sensor reading
        print("Sensor reading")
        time.sleep(1)

def actuator_control():
    while True:
        # Simulate actuator control
        print("Actuator control")
        time.sleep(2)

sensor_thread = threading.Thread(target=sensor_reading)
actuator_thread = threading.Thread(target=actuator_control)

sensor_thread.start()
actuator_thread.start()

sensor_thread.join()
actuator_thread.join()
```

## Exercises

### Exercise 1: Web Server Handling Multiple Client Requests
Create a simple multi-threaded web server that handles multiple client requests and responds with a personalized message.

#### Solution
```python
import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received: {request.decode('utf-8')}")
    client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, Client!")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)
print("Server listening on port 8080...")

while True:
    client_socket, addr = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
```

### Exercise 2: Data Processing Pipeline
Implement a multi-processing data pipeline that processes large data chunks concurrently and combines the results.

#### Solution
```python
import multiprocessing

def process_data(data_chunk):
    # Simulate data processing
    result = sum(data_chunk)
    return result

if __name__ == '__main__':
    data = [i for i in range(1000000)]
    chunk_size = len(data) // 4
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(process_data, chunks)
    
    total_result = sum(results)
    print(f"Total result: {total_result}")
```

### Exercise 3: Real-Time System
Create a multi-threaded program simulating a real-time system with two threads: one for sensor reading and another for actuator control.

#### Solution
```python
import threading
import time

def sensor_reading():
    while True:
        # Simulate sensor reading
        print("Sensor reading")
        time.sleep(1)

def actuator_control():
    while True:
        # Simulate actuator control
        print("Actuator control")
        time.sleep(2)

sensor_thread = threading.Thread(target=sensor_reading)
actuator_thread = threading.Thread(target=actuator_control)

sensor_thread.start()
actuator_thread.start()

sensor_thread.join()
actuator_thread.join()
```

By understanding these applications and working through the exercises, you will gain a deeper insight into how concurrent programming can be utilized in real-world scenarios to enhance the performance and responsiveness of your Python programs.
```
