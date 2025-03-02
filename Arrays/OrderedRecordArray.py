def identity(x):
    return x

class OrderedRecordArray:
    def __init__(self, initialSize, key=identity):
        self.__a = [None] * initialSize
        self.__nItem = 0
        self.__key = key
        
    def __len__(self):
        return self.__nItem
    
    def get(self, n):
        if n >= 0 and n <= self.__nItem:
            return self.__a[n]
        raise IndexError("Index" + str(n) + "is out of range")
    
    def traverse(self, function=print):
        for idx in range(self.__nItem):
            function(self.__a)
            
    def __str__(self):
        ans = "["
        for idx in range(self.__nItem):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[idx])
        ans += "]"
        return ans
    
    def find(self, key):
        low = 0
        high = self.__nItem - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.__key(self.__a[mid]) == key:
                return mid
            elif self.__key(self.__a[mid]) < key:
                low = mid + 1
            else:
                high = mid - 1
        return low
    
    def search(self, key):
        idx = self.find(key)
        if idx < self.__nItem and self.__key(self.__a[idx]) == key:
            return self.__a[idx]
        
    def insert(self, item):
        if self.__nItem >= len(self.__a):
            raise Exception("Array overflow")
        j = self.find(self.__key(item))
        
        for k in range(self.__nItem, j, -1):
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item
        self.__nItem += 1
        
    def delete(self, item):
        j = self.find(self.__key(item))
        if j < self.__nItem and self.__a[j] == item:
            self.__nItem -= 1
            for k in range(j, self.__nItem):
                self.__a[k] = self.__a[k + 1]
            return True
        return False
            
        
    