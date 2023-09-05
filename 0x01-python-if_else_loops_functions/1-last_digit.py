#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of " + f"{number}"
last = abs(number) % 10
if last > 5:
	print(f"{str} is {last:d} and is greater than 5")
elif last == 0:
	print(f"{str} is {last:d} and is 0")
else:
	print(f"{str} is {last:d} and is less than 6 and not 0")
