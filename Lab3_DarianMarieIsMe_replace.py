'''Lab 3- Programming Assignment - Part 3
Darian Marie Bruce
The purpose of this program is to import the list from part 2 and replace
one of the string items from this list with binoculars and use slice notation
01/29/2026'''

# Importing the list

from Lab3_DarianMarieIsMe_add import items

# Modifying the list

items[1] = 'binoculars'

# Printing list to binoculars using slice notation

print("Items I will be taking with me up to binoculars:", items[:2])