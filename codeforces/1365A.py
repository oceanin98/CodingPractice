def read_ints():
    temp = input().split()
    ints = [int(t) for t in temp]
    return ints

t = int(input())

for _ in range(t):
    n,m = read_ints()
    cols = [0] * m
    for _ in range(n):
        occupied = 0
        row = read_ints()
        for i in range(m):
            if row[i]:
                occupied = 1
                cols[i] = 1

        n -= occupied

    m -=  sum(cols)
    if min(m,n) % 2:
        print("Ashish")
    else:
        print("Vivek")
