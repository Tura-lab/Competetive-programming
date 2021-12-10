def select(self,arr, j):
    selected = j
    for i in range(j+1, len(arr)):
        if arr[i] < arr[selected]:
            selected = i
    return selected        

def selectionSort(self,arr,n):
    for i in range(len(arr)):
        selected = self.select(arr,i)
        arr[i], arr[selected] = arr[selected], arr[i]
    return arr
