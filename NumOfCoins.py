import sys

def minCoins(coins, m, V):
 
    # base case
    if (V == 0):
        return 0
 
    # Initialize result
    res = sys.maxsize
     
    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V-coins[i])
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
 
    return res
 
# Driver program to test above function
coins = [0.01, 0.02, 0.05, 0.1,0.2,0.5,1,2]
m = len(coins)
V = 11
print("Minimum coins required is",minCoins(coins, m, V))
 
# This code is contributed by
# Smitha Dinesh Semwal
