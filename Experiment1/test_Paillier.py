from Paillier import Paillier
from time import *

if __name__=="__main__":
    print("------------------------------------------")
    pa = Paillier()
    print("加解密参数如下：")
    pa.gen_Key()
    print("------------------------------------------")
    message=eval(input("请输入需要加密的明文："))
    Enc_begin_time=time()
    print("加密前明文： ",message)
    c=pa.encode(message)
    Enc_end_time=time()
    Enc_time=Enc_end_time-Enc_begin_time
    print("加密后密文： ",c)
    print("加密运行时间： ",Enc_time)
    print("------------------------------------------")
    Dec_begin_time=time()
    print("需要解密的密文：",c)
    m=pa.decode(c)
    Dec_end_time=time()
    Dec_time=Dec_end_time-Dec_begin_time
    print("解密后的明文：",m)
    print("解密运行时间: ",Dec_time)

