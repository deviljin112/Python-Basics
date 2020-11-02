# What is concatination

first_name = "James"
middle_name = "007"
last_name = "Bond"

print(first_name, middle_name, last_name)  # => James 007 Bond

age = 56

print(first_name, middle_name, last_name, age)  # => James 007 Bond 56

# Casting int to string

print("Age " + str(age))  # => Age: 56

# Casting string to int

print(int(middle_name))  # => 7

# Concatinating Variables

name = input("Please input your name\n=> ")
print(f"Hello {name}")
