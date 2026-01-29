'''Lab 3 Programming Assignment- Part 2
Darian Marie Bruce
The purpose of the second part of this assignment is to import the list from
part 1, append 5 more items to this list, and print the resulting list 
reversed alphabetically.
01/28/2026
'''

#Importing the list from Lab3_DarianMarieIsMe_list.py

from Lab3_DarianMarieIsMe_list import items

#Appending 5 more items to the list

items.append('hair ties')
items.append('toothpase')
items.append('blankets')
items.append('cookies')
items.append('camping chairs')

#Sorting and printing the list in reverse alphabetical order

items.sort(reverse=True)

print("Items I will be taking with me, sorted in reverse alphabetical order:")

print(items[0].title())
print(items[1].title())
print(items[2].title())
print(items[3].title())
print(items[4].title())
print(items[5].title())
print(items[6].title())
print(items[7].title())
print(items[8].title())
print(items[9].title())
print(items[10].title())
print(items[11].title())
print(items[12].title())
print(items[13].title())
print(items[14].title())