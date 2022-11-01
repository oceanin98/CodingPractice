#a미터 올라간다 b만큼 떨어진다 올라가려면 며칠?
#a, b ,v
#낮에 올라가는 숫자, 떨어지는 숫자, 올라가야될 숫자
#계산을 어떻게 했더라...

import sys
import math
input= sys.stdin.readline
a,b,v = map(int,input().split())
day= math.ceil((v-a)/(a-b))+1

print(day)


            