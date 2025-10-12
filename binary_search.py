def binary_search_recursive(nums: list[int], key: int, is_sorted: bool = False, low: int = 0) -> int:
  # Sort the list if not previously sorted (Does not return the correct index)
  if not is_sorted:
    nums = sorted(nums)
    is_sorted = True
  
  # Get the middle element of the range
  mid: int = len(nums) // 2

  # Return the index if the selected item matches the key
  if nums[mid] == key: return low + mid
  # Returns -1 if the list does not contain the key
  elif len(nums) == 1: return -1
  
  # If the selected item is larger than the key
  if nums[mid] > key: return binary_search_recursive(nums[:mid], key, is_sorted, low)
  # If the selected item is smaller than the key
  else: return binary_search_recursive(nums[mid + 1:], key, is_sorted, low + mid + 1)

print(binary_search_recursive([0, 5, 18, 23, 30, 71, 104], 30))