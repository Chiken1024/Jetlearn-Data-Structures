def swap(arr: list[any], pos: int) -> list[any]:
  arr[pos:(pos + 2)] = arr[pos:(pos + 2)][::-1]
  return arr

nums: list[int] = [0, 6, 3, 2, 65, 34, 71, -5, -54]

is_sorted: bool = False
while not is_sorted:
  is_sorted = True
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]: nums = swap(nums, i)
    if i > 0 and nums[i] < nums[i - 1]: is_sorted = False
  print(nums)