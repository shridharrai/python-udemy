import threading

count = 0

def inc():
    global count
    for _ in range(1000000):
        count += 1

threads = [threading.Thread(target=inc) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Count inc completed: ", count)