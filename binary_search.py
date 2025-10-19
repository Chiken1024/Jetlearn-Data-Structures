def binary_search(nums: list[int], key: int) -> int:
  low: int = 0
  mid: int = len(nums) // 2

  while nums[mid] != key and len(nums) > 1:
    if nums[mid] < key:
      nums = nums[mid + 1:]
      low += mid + 1
    else: nums = nums[:mid]
    
    mid //= 2
  
  if nums[mid] == key: return low + mid
  else: return -1

print(binary_search([-50, -32, -5, 0, 4, 9, 12, 18, 37], 12))