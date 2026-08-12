## Q5. Dictionaries

my_dict = {
"name": "Sachinjeet",
"roll_no": "1024170376",
"branch": "CSE",
"age": 20,
"city": "Dhuri"
}

# i. Rename city to location

my_dict["location"] = my_dict.pop("city")
print(my_dict)

# ii. Add cgpa

my_dict["cgpa"] = 6
print(my_dict)

# iii. Increase age by 1

my_dict["age"] += 1
print(my_dict)

# iv. Delete branch using pop()

dict1 = my_dict.copy()
dict1.pop("branch")
print(dict1)

# Delete branch using del

dict2 = my_dict.copy()
del dict2["branch"]
print(dict2)

# pop() returns the removed value, while del only deletes the key.

# v. Print key-value pairs

for key, value in my_dict.items():
print(key, "->", value)

# vi. Check if email exists

if "email" in my_dict:
print(my_dict["email"])
else:
print("Email key not found")

# vii. Create friend dictionary and merge

friend_dict = {
"name": "Aman",
"roll_no": "1024170000",
"branch": "CSE",
"age": 21,
"city": "Ludhiana"
}

merged_dict = {**my_dict, **friend_dict}
print(merged_dict)

# When both dictionaries have the same key, values from friend_dict overwrite values from my_dict.

# viii. Dictionary comprehension with only string values

string_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print(string_dict)
