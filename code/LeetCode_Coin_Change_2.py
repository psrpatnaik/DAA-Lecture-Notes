 # https://leetcode.com/problems/coin-change-2/
  class Solution:
     def change(self, amount: int, coins: List[int]) -> int:
        @cache        
        def change_temp(amount: int, coins: Tuple[int]) -> int:
            # Base case
            if amount == 0:
                return 1
            if amount < 0 or len(coins) == 0:
                return 0
            # make recursive call to using a coin and not using a coin
            return change_temp(amount, coins[:-1]) + change_temp(amount - coins[-1], coins)
        return change_temp(amount, tuple(coins)) 

        
