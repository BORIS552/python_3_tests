def oddNumbers(l,r):
    arr = []
    while l <= r:
        if l%2 != 0:
            arr.append(l)
        l  = l + 1
    return arr


if __name__ == "__main__":
    val = oddNumbers(2, 11)
    print(val)