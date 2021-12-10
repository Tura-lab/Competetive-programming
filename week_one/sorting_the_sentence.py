def select(self,arr, j):
        selected = j
        for i in range(j+1, len(arr)):
            if arr[i] < arr[selected]:
                selected = i
        return selected        

def selectionSort(self, w, arr,n):
    for i in range(len(arr)):
        selected = self.select(arr,i)
        arr[i], arr[selected] = arr[selected], arr[i]
        w[i], w[selected] = w[selected], w[i]
    return w
def sortSentence(self, s: str) -> str:
    w = s.split(' ')
    nums = [int(n[-1]) for n in w]
    return ' '.join([wrd[:-1] for wrd in self.selectionSort(w, nums, len(nums))])
        
