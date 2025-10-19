arr: list[int] = [-16, -20, 7, -5, 13, 0]

for i in range(1, len(arr)):
  key: int = arr[i]
  j: int = i - 1
  while j >= 0 and key < arr[j]:  # While index > 1 and value at index is smaller than j
    print(arr)
    arr[j + 1] = arr[j]
    j -= 1
  print(arr)
  arr[j + 1] = key
  print(arr)
  print("")