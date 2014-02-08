# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.

""" AMY: how would you make it so it returns odd numbers out of list mixed with #s and strings"""

def all_odd(some_list):
    new_list = []

    for item in some_list:
        if type(item) == int:
            if item % 2 == 1:
                new_list.append(item)
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []

    for item in some_list:
        if type(item) == int:
            if item % 2 == 0:
                new_list.append(item)
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []

    for item in word_list:
        if len(item) > 4:
            new_list.append(item)

    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.

""" AMY: how would you do this without min function?"""
def smallest(some_list):
    for i in range(len(some_list)):
        if some_list[i+1] < some_list[i]:
             smallest = some_list[i+1]

    return smallest

#    return min(some_list)

# Write a function that finds the largest element in a list of integers and returns it.

""" AMY: how would you do this without min function?"""
def largest(some_list):
    return max(some_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for num in some_list:
        half = float(num)/2
        new_list.append(half)
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for word in word_list:
        count = len(word)
        new_list.append(count)
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):

    return []

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return []

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None
