#하노이탑 
#크기도 중요한데 그거를 어떻게 계산해 놓은걸까?
#이동을 어떻게 시키는 걸까?

def hanoi(start, mid, end, disc):
    if disc >= 1:
        hanoi(start, end, mid, disc-1)
        print(start, end)
        hanoi(mid,start,end,disc -1) 
        
n= int(input())
print(2**n-1)

if n<=20:
    hanoi(1,2,3,n)
    
#와 천젠대???
