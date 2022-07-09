class HashTable:
    
    def __init__(self, size=7):
        self.data_map = [None]*size
    
    def __hash(self, key):
        myhash = 0
        for letter in key:
            myhash = (myhash + (ord(letter)*23)) % len(self.data_map)
        return myhash
        
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for k, v in self.data_map[index]:
                if k == key:
                    return v
        
    def print_hash(self):
        for i,v in enumerate(self.data_map):
            print(f"{i} : {v}")
            
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in self.data_map[i]:
                    all_keys.append(j[0])
        return all_keys

myht = HashTable()
myht.set_item('apple', 100)
myht.set_item('mangos',999)
myht.print_hash()
myht.get_item('apple')
print(myht.keys())
