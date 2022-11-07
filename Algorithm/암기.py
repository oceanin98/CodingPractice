prime_list = [False, False] + [True]*10002

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
            prime_list[j]= False
            
t= int(int)