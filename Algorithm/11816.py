#8진수, 10진수, 16진수

# def convert(num):
#     if num[:2] =='0x':
#         answer= int(num,16)
#     elif num [:1]=='0':
#         answer = int(num,8)
#     else: 
#         answer =int(num)
#     return answer
        
# if __name__ == "__main__":
#     num= input()
#     print(convert(num))

x= input()
if '0x' in x:
    x= int(x,16)
elif x[0] =='0':
    x= int(x,8)
print(x)

#똑똑하네.. 0x가 들어가면 16진수로 바꾸고, 0으로 시작하면 8진수로 바꾸고, 아니면 10진수로 바꾼다.
    

    
    