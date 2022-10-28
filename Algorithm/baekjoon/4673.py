#앞자리수 더하기 뒷자리수  주르륵 출력



selfnumber= set(range(1,10001))
generated_num=set()

for i in range(1,10001):
    for j in str(i):
        print(j)
        i += int(j)
    generated_num.add(i)
    

