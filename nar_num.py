def getCountDigitRecur(n) :
    if (n == 0) :
        return 0
    return (1 + getCountDigitRecur(n // 10))

def egocentricNumbers(n) :
    c = getCountDigitRecur(n)
    d = n; sm = 0
    while (d) :
        sm = sm + pow(d % 10, c)
        d = d // 10
     
    if (n == sm):
        return 1
    else:
        return 0
     
 
# Driver code 
n = 1630
print(egocentricNumbers(n))