from stack import Stack

OPEN_PAR: list[str] = ['(', '[', '{']
CLOSE_PAR: list[str] = [')', ']', '}']

PAR_PAIRS: dict[str, str] = {')': '(', ']': '[', '}': '{'}

def parentheses_correct(s: str) -> bool:
  stack: Stack = Stack(len(s))

  for c in s:
    stack.display()
    if c in OPEN_PAR: stack.push(c)
    elif c in CLOSE_PAR:
      if not stack.is_empty() and PAR_PAIRS[c] == stack.top: stack.pop()
      else: return False
  return True

print(parentheses_correct("([](((()))){{{{}}}})"))