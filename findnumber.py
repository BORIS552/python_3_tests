
def findnumber(arr, k):
    try:
        arr.index(k)
        return 'YES'
    except:
        return 'NO'

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    val = findnumber(arr, 10)
    print(val)