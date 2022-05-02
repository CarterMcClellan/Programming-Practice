class Solution:
    def countAndSay(self, n: int) -> str:
        n0 = "1"
        
        for _ in range(n-1):
            n0 = self.in_order_count(n0)
        
        return n0
    
    def in_order_count(self, number: str) -> List[str]:
        """ 
        iterate through the digits in a number
        keep a count of consecutive digits
        """
        N = len(number)
        curr_digit = number[0]
        result = []
        curr_count = 1
        for idx in range(1, N):
            if number[idx] == curr_digit:
                curr_count += 1
            else:
                result.append(str(curr_count) + str(curr_digit))
                curr_digit = number[idx]
                curr_count = 1
                
        result.append(str(curr_count) + str(curr_digit))        
        return "".join(result)
        
