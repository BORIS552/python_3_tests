s = ['What','You']

print(list(s))
s = list(s)
final = ''
count = 0
res = []
for x in s:
    print(x)
    for ch in x:
        if ch.isupper():
            print(ch)
            res.append(ch)
    # res = [char for char in x if char.isupper()]

for y in res:
    if(count < len(s)-1):
        final += y+'.'
    else:
        final += y
    count = count + 1

print(final)