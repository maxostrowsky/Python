
# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) 
# down to 0 (as the last element).

#     Example: countdown(5) should return [5,4,3,2,1,0]
# from typing import List


newList = []

def countDown(num):
    for x in range(num, -1, -1):
        newList.append(x)
    return(newList)

print(countDown(5))

# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.

#     Example: print_and_return([1,2]) should print 1 and return 2

def returnOne(num1, num2):
    print(num1)
    return num2

returnOne(1,2)

# First Plus Length - Create a function that accepts a list 
# and returns the sum of the first value in the list plus the list's length.

#     Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

plusList = [1,2,3,4,5]

def plusLength(list):
    sum = list[0] + len(list)
    return sum
print(plusLength(plusList))

# Values Greater than Second - Write a function that accepts a list 
# and creates a new list containing only the values from the original 
# list that are greater than its 2nd value. Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

#     Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#     Example: values_greater_than_second([3]) should return False

first_list = [5,2,3,2,1,4]
second_list = []


def makeList(list):
    if len(list) >= 2:
        third_list = []
        for x in range(len(list)):
            if list[x] > list[1]:
                third_list.append(list[x])
        return third_list
    else:
        return False
print(makeList(second_list))
print(makeList(first_list))

# This Length, That Value - Write a function that accepts two integers as parameters: size 
# and value. The function should create and return a list whose length is equal to the 
# given size, and whose values are all the given value.

#     Example: length_and_value(4,7) should return [7,7,7,7]
#     Example: length_and_value(6,2) should return [2,2,2,2,2,2]



def lengthValue(num1, num2):
    list_one = []
    for idx in range(num1):
        num1 = len(list_one)
        list_one.append(num2)
    return list_one
print(lengthValue(4,7))
print(lengthValue(6,2))