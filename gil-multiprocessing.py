from multiprocessing import Process
import time

def count_number():
    print(f"Started counting...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Finished counting...")

if __name__ == "__main__":
    start = time.time()
    p1 = Process(target=count_number)
    p2 = Process(target=count_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()

    print(f"Total time taken {end - start:.2f} seconds")