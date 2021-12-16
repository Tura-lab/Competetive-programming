class Solution:
    def index_of_max(self, arr):
        m = 0
        for i in range(len(arr)):
            if arr[i]> arr[m]:
                m=i
        return m
    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i]<arr[i-1]:
                return False
        return True
    def pancakeSort(self, arr):
        ks = []
        unsorted = len(arr)
        while not self.isSorted(arr):
            idx = self.index_of_max(arr[:unsorted])
            if idx == unsorted-1:
                unsorted-=1
                continue
            arr[:idx+1] = arr[:idx+1][::-1]
            ks.append(idx+1)
            arr[:unsorted] = arr[:unsorted][::-1]
            ks.append(unsorted)
            unsorted-=1
        return ks
        
