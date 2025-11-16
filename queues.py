from typing import Any

class Queue:
  def __init__(self, size: int) -> None:
    self.size: int = size
    self.available: int = size
    self.queue: list[Any] = [None for _ in range(size)]
    self.front: int = 0
    self.rear: int = 0

  def enqueue(self, item: Any) -> None:
    if self.available > 0:
      self.queue[self.rear] = item
      self.rear = (self.rear + 1) % self.size
      self.available -= 1
    else: print(f"Failed to enqueue item; queue is full")
  
  def dequeue(self) -> Any:
    if self.available < self.size:
      self.queue[self.front] = None
      self.front = (self.front + 1) % self.size
      self.available += 1
    else: print(f"Failed to dequeue; queue is empty")
  
  def clear(self) -> None:
    self.available = self.size
    self.queue = [None for _ in range(self.size)]
    self.front = 0
    self.rear = 0
  
  def get_front(self) -> Any: return self.queue[self.front]

  def get_rear(self) -> Any: return self.queue[self.rear]

  def display(self) -> None: print(self.queue)