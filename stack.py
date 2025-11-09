from typing import Any

class Stack:
  def __init__(self, cap: int, init_val: list[Any] = []) -> None:
    self.cap: int = cap
    self.stack: list[Any] = init_val

  @property
  def size(self) -> int: return len(self.stack)

  @property
  def top(self) -> Any: return self.stack[-1]

  def is_empty(self) -> bool: return self.size == 0

  def push(self, val: Any) -> None:
    if len(self.stack) < self.cap: self.stack.append(val)

  def pop(self) -> Any: return self.stack.pop()

  def display(self) -> None: print(self.stack)