class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 0 -> it takes 0 coins to make 0 cents
        # -1 -> we cannot represent this denomination
        amts = [0] + [-1 for _ in range(amount)]
        
        # initialize counts
        # skip coins > target -> we dont care
        for coin in coins:
            if coin > amount:
                continue
            amts[coin] = 1
        
        for i in range(amount+1):
            for coin in coins:
                if coin > i:
                    continue
                
                # (i) is the denomination we want to make
                # (coin) is a denomination we have
                # -> if (i-coin) can be made
                # -> then i = 1 + (i-coin)
                if amts[i-coin] > 0:
                    if amts[i] == -1:
                        amts[i] = 1+amts[i-coin]
                    else:
                        amts[i] = min(amts[i], 1+amts[i-coin])
                    
        # print(f"amts {amts}")            
        return amts[amount]
