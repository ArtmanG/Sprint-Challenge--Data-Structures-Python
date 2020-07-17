# #### Task 2. Runtime Optimization

# ***!Important!*** If you are running this using PowerShell by clicking on the green play button, you will get an error that `names1.txt` is not found.  To resolve this, run it, get the error, then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

# Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

# Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

# *You may not use the built in Python list, set, or dictionary in your solution for this problem.  However, you can and should use the provided `duplicates` list to return your solution.*

# (Hint: You might try importing a data structure you built during the week)

import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10,000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10,000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# [0] so that we can compare a string "name" to not the whole list, but the names on the list 
bst = BSTNode(names_1[0]) 

# insert the list of names into a BST
for name in names_1:
    bst.insert(name)

# Check the names on the second list against the first list. Add all duplicates to the duplicates list
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
