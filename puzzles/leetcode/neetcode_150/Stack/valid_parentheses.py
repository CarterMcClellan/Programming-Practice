"""
Basic thought process

Every open paren must have a corresponding in order closing
paren. (I called open parens 'right facing' in this soln).
"""
class Solution:
    def isValid(self, s: str) -> bool:
        right_facing = []

        for c in s:
            if c in "({[":
                right_facing.append(c)
            elif c in ")}]":

                if len(right_facing) == 0:
                    return False

                if c == ")" and right_facing[-1] != "(":
                    return False
                
                elif c == "}" and right_facing[-1] != "{":
                    return False
            
                elif c == "]" and right_facing[-1] != "[":
                    return False

                right_facing.pop(-1)
        
        return len(right_facing) == 0