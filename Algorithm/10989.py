#수정렬3
#얘는 중복이 그대로 나타나야해

n= int(input())
arr=[0]*10001  
for i in range(n):
    a= int(input())
    arr[a-1] +=1 #이게 무슨말임??
    #[2,2,2,1,2,0,1,0...] 이렇게 중복된만큼 숫자가 그자리에 +1 되어서 저장됨 
    
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]): #여기서부터는 위에 arr에 있는 자리수에서 
            print(i+1) #+1 되어서 프린트 됌 
            
            #내가 이걸 어떻게 생각해내냐고 시방 