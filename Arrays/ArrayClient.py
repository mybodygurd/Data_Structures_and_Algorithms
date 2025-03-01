from Array import Array

MaxSize = 30
arr = Array(MaxSize)
str_arr = Array(MaxSize)
items = [2, 98, 3, 7, 10, 88, 33, 12, 36, 68, 'string', 2.4, 0.01, 'Mahdi']

for item in items:
    arr.insert(item)

print("Array containing", len(arr), "items")
arr.traverse()

print("search for 6 returns", arr.search(36))

print("Deleting 88 returns", arr.delete(88))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()

print("The highest number of array:", arr.deleteMaxNum())

str_items = ['Mahdi', 'string', 'Python', 'data structure']

for item in str_items:
    str_arr.insert(item)
    
print('the highest number in string array returns', str_arr.deleteMaxNum())