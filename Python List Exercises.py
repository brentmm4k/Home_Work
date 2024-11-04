fruits = ['mango', 'banana', 'apple', 'grape', 'orange']
print(fruits)

# Prints all the strings in the list "fruits".

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[4])

# Prints the 1st, 3rd, and the 5th strings in the "colors" list.

numbers = [10, 20, 30, 40, 50]
numbers[1]= 25
numbers.append(60)
print(numbers)

# Changes the 2nd integer into "25" and then appends the number "60" as the 6th integer.

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = [names[0], names[1], names[2]]
print(subset)

# Creates a subset only consisting of the 1st, 2nd, and 3rd strings in the "names" list and prints the subset.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    squared = numbers[0] ** 2
    print(squared)
    numbers[0] += 1
    if numbers[0] == 11: 
        break
# Creates a loop that defines a variable as the number list being squared by 2 as it starts with 0(the first integer) 
# Adds one to the number value every loop until it prints '100', then the loop breaks.

shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('egg')
shopping_cart2 = ['butter', 'cheese']
shopping_cart.extend(shopping_cart2)
print(shopping_cart)

# Appends milk, bread, and egg strings into the empty list then extends it with strings 'butter' and 'cheese'.

numbers = [45, 22, 88, 56, 92, 33]
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

# max/min finds the highest and lowest integers in the list. 

letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = letters.count('a')
print("The amount of times a shows up in the list is:", count_of_a)

# It counts how many times the string "a" appears on the list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [square ** 2 for square in numbers if square % 2 == 0]
print(even_numbers)

# Checks if the integer in the list is an even number or not, even numbers get printed and the odd numbers dont.

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = (set(nums))
print(unique_nums)

# Converts the "nums" list to a set as sets do not print duplicates of the same integer/string.