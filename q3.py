## Q3. Random Numbers

import random
from collections import Counter

# Set random seed using roll number

random.seed(1024170376)

# i. Generate a list of 100 random numbers between 100 and 900

numbers = [random.randint(100, 900) for _ in range(100)]
print(numbers)

# ii. Count and print all odd numbers

odd_numbers = [n for n in numbers if n % 2 != 0]
print(len(odd_numbers))

# iii. Count and print all even numbers

even_numbers = [n for n in numbers if n % 2 == 0]
print(len(even_numbers))

# iv. Count and print all prime numbers, and create a list of prime numbers

def is_prime(n):
if n < 2:
return False
for i in range(2, int(n ** 0.5) + 1):
if n % i == 0:
return False
return True

prime_numbers = [n for n in numbers if is_prime(n)]
print(len(prime_numbers))
print(prime_numbers)

# v. Print the most frequent number and its frequency

counter = Counter(numbers)
most_common = counter.most_common(1)[0]
print(most_common[0])
print(most_common[1])
