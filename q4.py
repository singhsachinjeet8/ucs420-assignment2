## Q4. Sets

digits = [1, 0, 2, 4, 1, 7, 0, 3, 7, 6]

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}

print(A)
print(B)

# vi. Union

print(A.union(B))

# vii. Intersection

print(A.intersection(B))

# viii. Difference

print(A.difference(B))
print(B.difference(A))

# difference() gives elements only in one set, while symmetric_difference() gives elements in either set but not both.

# ix. Symmetric difference

print(A.symmetric_difference(B))

# x. Subset and superset

print(A.issubset(B))
print(B.issuperset(A))

# xi. Remove a value from set A using discard()

x = int(input())
A.discard(x)
print(A)

# discard() is safer because it does not raise an error if the value is absent.
