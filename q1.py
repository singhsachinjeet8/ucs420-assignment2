## Q1. Lists

# Roll Number: 1024170376

# Create list L by multiplying each digit of the roll number by 10

L = [10, 0, 20, 40, 10, 70, 0, 30, 70, 60]

# i. Print L

print(L)

# ii. Add two numbers

L.append(90)
print(L)

L.insert(3, 50)
print(L)

# iii. Remove two elements

L.remove(0)
print(L)

L.pop()
print(L)

# iv. Sort in ascending and descending order

L.sort()
print(L)

L.sort(reverse=True)
print(L)

# v. Print first three and last three elements

print(L[:3])
print(L[-3:])

# vi. Create a new list with elements greater than the average

avg = sum(L) / len(L)
new_list = [x for x in L if x > avg]
print(new_list)

