from Paillier import Paillier


#投票工作：每个elector对每个candidate进行投票，然后将每个elector的投票结果进行加密，返回chiper_lists
def vote(can,ele):
    chiper_lists=[]
    for i in range(1,ele+1):
        chiper_list = []

        print("--------------Elector{},Please vote.--------------".format(i))
        for j in range(1,can+1):
            chiper_list.append(pa.encode(eval(input("Candidate{}:".format(j)))))
        print("Elector{},your result is : ".format(i),chiper_list)
        chiper_lists.append(chiper_list)

    return chiper_lists

#计数方主要的工作：获得vote的结果，然后运算其乘积，返回一个候选人得分密文列表
def count(chiper_lists,can,ele,N):
    chiper_list=[]
    for i in range(can):
        chiper_list.append(1)
    print('-------------------------------------------------')
    print("Please wait for a moment, the cpu is computing.")
    for i in chiper_lists:
        count=0
        for j in i:
            chiper_list[count]=(chiper_list[count] % N**2) * (j % N ** 2) % N**2
            count=count+1

    return chiper_list

#公布者：拿到count的密文列表对其解密，输出候选人得分
def theority(chiper_list):
    result=[]
    for i in chiper_list:
        result.append(pa.decode(i))

    return result

#对结果进行排序
def sort(result):
    index=[]
    for i in range(0,len(result)):
        index.append(i)

    #冒泡排序
    for i in range(0,len(result)):
        for j in range(i,len(result)):
            if result[j] > result[i]:
                t=index[i]
                index[i]=index[j]
                index[j]=t
            else:
                continue

    return index

if __name__=="__main__":
    candidate=eval(input("Please input the number of candidates:"))
    electors=eval(input("Please input the number of electors:"))

    #System init
    pa=Paillier()
    pa.gen_Key()
    publicKey=pa.pubKey
    chiper_lists=vote(candidate,electors)

    chiper_list=count(chiper_lists,candidate,electors,publicKey[0])

    result=theority(chiper_list)

    print("---------------------result----------------------")
    for i in range(len(result)):
        print("Candidate{}:".format(i+1),result[i])

    print("---------------------sorted----------------------")

    index=[]
    index=sort(result)

    for i in index:
        print("Candidate{}".format(i+1),result[i])
    print(index)


