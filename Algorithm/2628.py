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



#다른버전 ####################
# x,y= map(int,input().split())
# x_list= [0,x]
# y_list=[0,y]
# for _ in range(int(input())):
#     xy, length= map(int,input().split())
#     if xy ==0:
#         y_list.append(length)
#     else:
#         x_list.append(length)

# x_list.sort()
# y_list.sort()

# max_square=0
# for i in range(1,len(x_list)):
#     for j in range(1, len(y_list)):
#         width= x_list[i]-x_list[i-1]
#         height= y_list[j]- y_list[j-1]
#         max_square= max(max_square, width,*height)

# print(max_square) 
        