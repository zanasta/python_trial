import random

random.seed(0)
a = [random.randint(0, 1) for i in range(1000)]

print("0: ", a.count(0))
print("1: ", a.count(1))

