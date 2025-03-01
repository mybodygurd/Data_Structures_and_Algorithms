class Array:
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
        
    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if n >= 0 and n <= self.__nItems:
            return self.__a[n]
        
    def set(self, n, value):
        if n >= 0 and n <= self.__nItems:
            self.__a[n] = value
            
    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1
        
    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
            
        return -1
    
    def search(self, item):
        return self.get(self.find(item))
    
    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for i in range(j, self.__nItems):
                    self.__a[j] = self.__a[i + 1]
                return True
        return False
    
    def traverse(self, function=print):
        for i in range(self.__nItems):
            function(self.__a[i])
            
    def deleteMaxNum(self):
        max_num = 0
        contain_num = False
        
        for i in range(self.__nItems):    
            if isinstance(self.__a[i], (int, float)):
                contain_num = True
                if self.__a[i] > max_num:
                    max_num = self.__a[i]
        if contain_num:
            self.delete(max_num)
            return max_num
        else:
            return None