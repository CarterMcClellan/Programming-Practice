from typing import Optional, Callable, Union, List

"""
Honestly I think I tried too hard to be neat with this one.
The core realization I had early on was that we can traverse the list
backwards to construct a nested expression object which could then be evaluated.

But I did not realize until looking through the solution that I didn't have to 
pass the index backward I could just mutate the list object by popping.
"""

class Expression:
   def __init__(self, operand: Optional['Operand'] = None, val: Optional[str] = None):
       self.operand: Optional[Operand] = operand
       self.val: Optional[int] = int(val) if val else None
       self.left: Optional[Expression] = None 
       self.right: Optional[Expression] = None

   def evaluate(self) -> int:
       if self.operand and self.left and self.right:
           return self.operand(self.left.evaluate(), self.right.evaluate())

       if self.val:
           return self.val

       raise Exception("something went wrong ")

class Operand:
   def __init__(self, operator: str):
       self.operator: str = operator
   
   def __call__(self, arg1: int, arg2: int) -> int:
       match self.operator:
           case "+": return arg1 + arg2
           case "-": return arg1 - arg2
           case "/": return int(arg1 / arg2)
           case _: return arg1 * arg2

class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
       def traverse() -> Expression:
           token = tokens.pop()
           if token in "*+-/":
               root = Expression(operand=Operand(token))
               root.right = traverse()
               root.left = traverse()
               return root
           return Expression(val=token)
       
       root = traverse()
       return root.evaluate()