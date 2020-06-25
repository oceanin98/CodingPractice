# https://codeforces.com/problemset/problem/118/A

string = input()
result = ""

for s in string:
    if s.isupper():
        s = s.lower()
    
    if s in 'aieouy':
        continue
    else:
        result += ".{}".format(s)

print(result)
