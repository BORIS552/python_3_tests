def numSquareSum(n): 
    squareSum = 0
    while(n): 
        squareSum += (n % 10) * (n % 10) 
        n = int(n / 10)
    return squareSum
  
def numbers_mood(n): 
    slow = n 
    fast = n
    while(True):
        slow = numSquareSum(slow)

        fast = numSquareSum(numSquareSum(fast))
        if(slow != fast): 
            continue 
        else: 
            break

    if (slow == 1): 
        return "happy"
    else: 
        return "sad"
  
# Driver Code 
n = 12; 
print(numbers_mood(n))