def fibonacci_recursive(n: int) -> int | ValueError:
  if n < 2:
    if n < 0: return ValueError("Number can not be lower than 0")
    return 1
  else: return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

#print(*[fibonacci_recursive(i) for i in range(0, 10)])

def fibonacci(n: int) -> int | ValueError:
  if n < 2:
    if n < 0: return ValueError("Number can not be lower than 0")
    return 1
  
  f: list[int] = [0, 1]
  for _ in range(n):
    f.append(f[-1] + f[-2])
    f.pop(0)
  return f[-1]

#print(*[fibonacci(i) for i in range(0, 10)])

def factorial(n: int) -> int | ValueError:
  if n < 2:
    if n == 1: return 1
    return ValueError("Number can not be lower than 1")
  else: return n * factorial(n - 1)

#print(*[factorial(i) for i in range(1, 10)])

def sum_of_number(n: int) -> int:
  if n > -2 and n < 2: return n
  sign: int = 1 if n > 0 else -1
  return sum([i for i in range(abs(n) + 1)]) * sign

#print(*[sum_of_number(i) for i in range(-9, 10)])

def sum_of_number_recursive(n: int) -> int | ValueError:
  if n < 2:
    if n >= 0: return n
    return ValueError("Number can not be lower than 0")
  else: return n + sum_of_number_recursive(n - 1)

#print(*[sum_of_number_recursive(i) for i in range(0, 10)])