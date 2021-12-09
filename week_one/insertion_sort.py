def insertionSort1(n, arr):
    i = len(arr)-1
    j = i-1
    key = arr[i]
    while key < arr[j] and j>-1:
        arr[j+1] = arr[j]
        j = j-1
        for i in arr:
            print(i, end=' ')
        print()
    arr[j+1] = key
    for i in arr:
            print(i, end=' ')
