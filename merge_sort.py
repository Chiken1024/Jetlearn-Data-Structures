def merge(arr: list[int], low: int, mid: int, high: int) -> None:
  temp: list[int] = [0] * len(arr)
  p1: int = low
  p2: int = mid + 1

  while p1 <= mid and p2 <= high:
    if arr[p1] < arr[p2]:
      temp.append(arr[p1])
      p1 += 1
    else:
      temp.append(arr[p2])
      p2 += 1
  
  while p1 <= mid:
    temp.append(arr[p1])
    p1 += 1

  while p2 < high:
    temp.append(arr[p2])
    p2 += 1
  
  for i in range(low, high + 1): arr[i] = temp[i]

def merge_sort(arr: list[int], high: int, low: int = 0) -> None:
  if high > low:
    mid: int = low + high // 2
    merge_sort(arr, mid, low)
    merge_sort(arr, high, mid + 1)
    merge(arr, low, mid, high)

print(merge_sort([0, 6, 3, 2, 65, 34, 71, -5, -54], 9))