from typing import Self

class Fruit:
  def __init__(self, color: str, taste: str, shape: str, amount: int) -> None:
    self.color: str = color
    self.taste: str = taste
    self.shape: str = shape
    self.amount: int = amount
  
  def get_shape(self) -> str: return self.shape

  def set_shape(self, new_shape: str) -> Self:
    self.shape = new_shape
    return self

  def set_amount(self, new_amount: int) -> Self:
    self.amount = new_amount
    return self
  
  def mod_amount(self, mod_amount: int) -> Self:
    if self.amount > -mod_amount: self.amount += mod_amount
    else: self.amount = 0

    return self
  
  def display(self) -> None:
    print(f"{self.amount} fruits that are {self.color}, taste {self.taste} and are {self.shape} shaped")

blueberry: Fruit = Fruit(
  "blue", "sweet", "", 1
).set_shape(
  "sphere"
).mod_amount(
  5
).display()

pear: Fruit = Fruit("green", "sweet", "egg", 5)
pear.set_amount(16)
print(pear.get_shape())