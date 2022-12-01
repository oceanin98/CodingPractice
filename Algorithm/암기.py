#TJadnjs 
#my bu

n= int(input())
arr=[0]*1001
for i in range(n):
    a= int(input())
    arr[a-1] +=1
    
for i in range(1001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
    
        