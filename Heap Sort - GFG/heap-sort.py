#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, p, heapSize):
        l = 2*p+1
        r = 2*p+2
        largest = p
        
        if l<heapSize and arr[l] > arr[largest]:
            largest = l
        if r<heapSize and arr[r] > arr[largest]:
            largest = r 
        
        if largest != p:
            arr[p], arr[largest] = arr[largest], arr[p]
            self.heapify(arr, largest, heapSize)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,p):
        for i in range(len(arr)//2-1, -1, -1):
            self.heapify(arr, i, len(arr))

    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        heapSize = len(arr)
        self.buildHeap(arr,0)
        
        for i in range(len(arr)):
            arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
            heapSize-=1
            self.heapify(arr, 0, heapSize)




#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends