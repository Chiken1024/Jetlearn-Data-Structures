def isr(arr: list[int], i: int = 1) -> list[int]:
  key: int = arr[i]
  j: int = i - 1

  while j >= 0 and key < arr[j]:
    arr[j + 1] = arr[j]
    j -= 1

  arr[j + 1] = key

  if i + 1 < len(arr): return isr(arr, i + 1)
  else: return arr

def risr(arr: list[int], i: int = -1) -> list[int]:
  if i < 0: i = len(arr) - 2
  
  key: int = arr[i]
  j: int = len(arr) - i + 1

  print(j, len(arr), arr[j])
  while j <= len(arr) and key > arr[j]:
    print(arr, i)
    arr[j - 1] = arr[j]
    j -= 1

  arr[j + 1] = key

  if i > 0: return risr(arr, i - 1)
  else: return arr

arr: list[int] = [-16, -20, 7, -5, 13, 0]
print(risr(arr))