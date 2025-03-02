from Array import Array

MaxSize = 100
arr = Array(MaxSize)
str_arr = Array(MaxSize)

for item in range(20):
    arr.insert(item)

print("Array containing", len(arr), "items")
arr.traverse()

print("search for 6 returns", arr.search(6))

print("Deleting 11 returns", arr.delete(11))

print("Setting item at index 3 to 14")
arr.set(3, 14)

print("Array after deletions has", len(arr), "items")
arr.traverse()

print("The highest number of array:", arr.deleteMaxNum())

print("Array after deleting the maximum number has", len(arr), "items")
arr.traverse()

str_items = ['Mahdi', 'string', 'Python', 'data structure']

for item in str_items:
    str_arr.insert(item)
    
print('the highest number in string array returns', str_arr.deleteMaxNum())

duplicated_items = [1,3,6,8,3,10,33,10,37,1,37,100,100,100]
for item in duplicated_items:
    arr.insert(item)
print("Array after inserting duplicated items has", len(arr), "items")
arr.traverse()

arr.removeDupes()

print("Array after deleting the duplicated items has", len(arr), "items")
arr.traverse()