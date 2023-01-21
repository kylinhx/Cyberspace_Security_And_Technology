num=[]
i=2
for i in range(4096,8180):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)
print(num)
print(len(num))