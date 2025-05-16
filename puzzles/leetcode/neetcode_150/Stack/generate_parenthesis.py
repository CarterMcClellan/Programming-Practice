"""
Brute force method (there might be further optimization with back tracking)

Basic realization is we can add a open parent whenever (until we run out)
Can only add a closing paren if there are more open then closed
Base Case: The len of the str is 2*N
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def dfs(curr_str: str, n_open: int, n_closed: int):
            if len(curr_str) == 2*n:
                ans.append(curr_str)
                return

            if n_open > 0:
                dfs(curr_str + "(", n_open - 1, n_closed)

            if n_open < n_closed:
                dfs(curr_str + ")", n_open, n_closed - 1)
        
        dfs("", n, n)

        return ans