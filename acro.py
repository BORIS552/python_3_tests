
def acronym(input):
    s = input
    final = ''
    count = 0
    res = []
    for x in s:
        for ch in x:
            if ch.isupper():
                res.append(ch)
        # res = [char for char in x if char.isupper()]

    for y in res:
        if(count < len(s)-1):
            final += y+'.'
        else:
            final += y
        count = count + 1
    
    return final


s = ['What','You']

print(acronym(list(s)))





