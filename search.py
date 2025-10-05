numbers = [2, 5, 8, 15, 24, 27, 43]
item = 15

for i, num in enumerate(numbers):
  if num == item:
    output = [num, i]
    break
else:
  raise ValueError("List does not contain value")

print(f"{output[0]} found at index {output[1]}")