import random
import collections
import time
import matplotlib.pyplot as plt

numbers = []
results = []
for i in range(1000):
    numbers.append(random.randint(1, 10))
choice = int(input('Выберите метод(1 или 2)'))
start_time = time.time()
if choice == 1:
    result = collections.Counter(numbers)
    print(f'{result} \n Время:{time.time() - start_time}')
    for i in range(1, 11):
        results.append(result.get(i))
elif choice == 2:
    count = 0
    for z in range(1, 11):
        for i in range(1000):
            if numbers[i] == z:
                count += 1
        print(f"'{z}': {count} ")
        results.append(count)
        count = 0
    print(time.time() - start_time)

x = [x for x in range(1, 11)]
plt.bar(x, results)
plt.show()
