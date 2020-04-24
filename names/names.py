import time
import sys
sys.path.append('../bst.py')
from bst import BinarySearchTreeNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

search_tree = BinarySearchTreeNode('Mneme')

for name in names_1:
    search_tree.insert(name)

# print(search_tree.value)
# print(search_tree.left.value)
# print(search_tree.right.value)
# print(search_tree.left.right.value)
# print(search_tree.left.left.value)

for name in names_2:
     if search_tree.contains(name):
         duplicates.append(name)

print(duplicates)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
