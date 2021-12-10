def countingSort(arr):
  least = greatest = 0
  for i in range(1, len(arr)):
      if arr[i] > arr[greatest]:
          greatest = i
      elif arr[i] < arr[least]:
          least = i

  range_dict = {}
  for i in range(0, 100):
      range_dict[i] = 0

  for item in arr:
      range_dict[item]+=1
  return [n for m,n in range_dict.items()]
