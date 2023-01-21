from Paillier import Paillier
import time

if __name__=="__main__":
    print("------------------------------------------")
    print("加解密参数如下：")
    pa=Paillier()
    pa.gen_Key()
    print("------------------------------------------")
    m1=eval(input("请输入需要加密的明文1："))
    m2=eval(input("请输入需要加密的明文2："))
    print("------------------------------------------")
    c=pa.plus(m1,m2)
    m=pa.decode(c)
    print("解密后明文为：",m)