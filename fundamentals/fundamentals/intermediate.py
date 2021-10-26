# Update Values in Dictionaries and Lists

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# x = [[5,2,3], [10,8,9]]
# students = [
#     {'first_name': 'michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# x[1][0] = 15
# students[0]['last_name'] = 'Byrant'
# sports_directory['soccer'][0] = 'Andres'
# z[0]['y'] = 30

# print(students)
# print(x)
# print(sports_directory)
# print(z)

# Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the 
# function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
# #     ]
# # iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary(some_list):
#     for name in range(len(students)):
#         print(students[name])
#     return(students)

# iterateDictionary(students)


# #3 Get Values From a List of Dictionaries

# # Create a function iterateDictionary2(key_name, some_list) that, given a list of 
# # dictionaries and a key name, the function prints the value stored in that key for each 
# # dictionary. For example, iterateDictionary2('first_name', students) should output:

# def iterateDictionary2(key_name, sone_list):
#     for idx in range(len(students)):
#         print(students[idx][key_name])
#     return students

# iterateDictionary2('first_name', students)

# 4 Iterate Through a Dictionary with List Values

#  Create a function printInfo(some_dict) that given a dictionary whose values are all lists
# prints the name of each key along with the size of its list, and then prints the associated 
# values within each key's list. For example:

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

# pseudo code
# 1. create a function takes in a dictionary
# 2. loop thru the dictionary
# 3. get the length of the list
# 4. get the key and caps it
# 5. loop thru the list
# 6. print the item



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_dojo(some_dict):
    for key in some_dict:
        list_length = len(some_dict[key])
        print(f'{list_length} {key.upper()}')
        for name in some_dict[key]:
            print(name)
        print()
print_dojo(dojo)

