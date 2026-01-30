'''Lab 3 - Programming Assignment - Part 4
Darian Marie Bruce
The purpose of this assignment is to import the list from part 3, remove an item 
from the list, print the resulting list, and print an f string afterwards
01/29/2026 
'''

# Importing the list

from Lab3_DarianMarieIsMe_replace import items

# Removing an item from the list

items.remove('binoculars')

# Printing the resulting list

print("Items I will now be taking with me:", items)
print(f"I will be taking this many items with me: {len(items)}")