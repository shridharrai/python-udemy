from multiprocessing import Process
import time

def brew_chai(num):
    print(f"Start of {num} chai brewing...")
    time.sleep(3)
    print(f"End of {num} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker is #{i + 1}", ))
        for i in range(3)
    ]

    # start all process
    for p in chai_makers:
        p.start()

    # wait for all to completed
    for p in chai_makers:
        p.join()

    print("All chai served")