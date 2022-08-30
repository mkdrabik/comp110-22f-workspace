"""Example of iterating through a string"""

user_string: str = input("Enter a word ")

#Common variable name for a counter
i: int = 0

while i<len(user_string):
    print(user_string[i])
    i = i + 1

print("Done")