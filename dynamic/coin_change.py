class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [None] * (amount + 1)
        
        def try_change(amount: int) -> int:
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if cache[amount] is not None:
                return cache[amount]
            
            result = -1
            for coin in coins:
                r = try_change(amount - coin)
                if r != -1 and (r < result or result == -1):
                    result = r
            
            if result != -1:
                result += 1
            
            cache[amount] = result
            return result
        
        return try_change(amount)

#######



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change: list[int] = [amount + 1] * (amount + 1)
        change[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                candidate = change[i - coin] + 1
                if change[i] > candidate:
                    change[i] = candidate
                    
        if change[amount] > amount:
            return -1
        return change[amount]
