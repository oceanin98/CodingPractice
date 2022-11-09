#종이자르기 
#dp할때 처럼 하면 안대나..?

r,c = map(int,input().split()) #종이의 가로세로
row=[0,r]
column=[0,c] 
for i in range(int(input())): #여기에 바로 넣을 수 있구나 
    r_or_c,linenumber=map(int,input().split())
    if r_or_c==1:
        row.append(linenumber)
    else:
        column.append(linenumber)

row.sort()# 정렬은 왜하지? 뺴서 최대 길이 구하려고 
column.sort()

subtracted_r=[]
subtracted_c=[] #빼서 넣을 곳

for i in range(len(row)-1):
    subtracted_r.append(row[i+1]-row[i])
for i in range(len(column)-1):
    subtracted_c.append(column[i+1]-column[i])
    
print(max(subtracted_r)*max(subtracted_c))
