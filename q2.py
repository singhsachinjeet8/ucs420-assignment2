## Q2. Tuples

# First 8 values from Q1 list

scores = (10, 0, 20, 40, 10, 70, 0, 30)

# i. Highest score and its index, lowest score and count

print(max(scores))
print(scores.index(max(scores)))
print(min(scores))
print(scores.count(min(scores)))

# ii. Reverse the tuple and return it as a list

reversed_list = list(scores[::-1])
print(reversed_list)

# Tuples are immutable, so they cannot be reversed in place.

# iii. Input a score and print its first occurrence index

x = int(input())
if x in scores:
print(scores.index(x))
else:
print("Score not present")

# iv. Attempt to change one element of the tuple

try:
scores[0] = 100
except TypeError as e:
print(e)

# Tuples are immutable, unlike lists which are mutable.

# v. Unpack the tuple

first, second, *remaining = scores
print(first)
print(second)
print(remaining)
