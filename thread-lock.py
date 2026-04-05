import threading

counter = 0
lock = threading.Lock()

def inc():
    global counter
    with lock:
        for _ in range(100000):
            counter += 1

threads = [threading.Thread(target = inc) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final count {counter}")