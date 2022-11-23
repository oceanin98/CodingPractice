#pypy3
#가로 세로 대각선으로 서로 공격할수 없게 하자 - N-QUEENS
#이전에 놓은 퀸과 대각선으로 위치하면 return

n=int(input())
visit=[-1]*n
answer=0

#이전에 놓은 퀸들과 대각선 검사
def check(depth):
    cur=visit[depth-1]
    cnt=1
    for i in range(depth-2, -1, -1):
        if cur -cnt ==visit[i] or cur + cnt == visit[i]:
                return False
        cnt += 1
    return True

def dfs(depth):
    global answer
    if  depth > 1 and not check(depth):
        return
    
    if depth ==  (n):
        answer += 1
        return
    
    for i in range(n):
        if i not in visit:
            if visit[depth] == -1:
                visit[depth] = i
                dfs(depth + 1)
                visit[depth] = -1
dfs(0)
print(answer)

#a mo ru get da 

        
    
         