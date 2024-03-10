from threading import Thread

counter = 0
rounds = 100000

class Counter(Thread):


    def run(self):
        global counter
        for _ in range(rounds):
            counter += 1
        print(counter)
        
counter1 = Counter()
counter2 = Counter()

counter1.start()
counter2.start()

counter1.join()
counter2.join()

print("Final counter value:", counter)