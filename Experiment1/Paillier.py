import math
import random
import gmpy2 as gy
from time import *

class Paillier(object):

    def __init__(self,pubKey=None,priKey=None):
        self.pubKey = pubKey
        self.priKey = priKey

    #密钥生成算法第一步，获得p和q
    def get_pq(self):
        list=[521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
              601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
              673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751,
              757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
              839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
              929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009,
              1013, 1019, 1021]
        pq=[]
        while True:
            p=list[random.randint(0,74)]
            q=list[random.randint(0,74)]
            if (math.gcd(p*q,(p-1)*(q-1))==1):
                pq.append(p)
                pq.append(q)
                break
            else:
                continue
        return p,q
        #print(p)
        #print(len(list))

    #密钥生成算法第二步，获得N和栏目大（x）
    def calculate_N(self,p,q):
        N=p*q
        x=(p-1)*(q-1)
        return N,x

    #密钥生成算法第三步，获得g，y
    def get_random(self,N,X):
        u=0
        while u==0:
            g=N+1
            u=gy.invert(X,N)
        return g,u

    #构建L（x）
    def L_x(self,N,x):
        z=(x-1)//N
        return z

    #加密过程
    def enc_m(self,publicKey,message):
        N=publicKey[0]
        g=publicKey[1]
        r = random.randint(1,N)
        c = (g ** message % N ** 2) * (r ** N % N ** 2) % N **2
        return c

    #解密过程
    def dec_c(self,N,priverKey,crypto):
        if crypto > N**2:
            return 0
        else:
            x=priverKey[0]
            u=priverKey[1]
            z=self.L_x(N,crypto**x % N**2)
            m=z*u % N
            return m

    #同态加法验证
    def com(self,message1,message2,publicKey,N):
        N = publicKey[0]
        g = publicKey[1]
        r = random.randint(1, N)
        c1 = (g ** message1 % N ** 2) * (r ** N % N ** 2) % N **2
        print("明文1加密后的密文为：",c1)
        c2 = (g ** message2 % N ** 2) * (r ** N % N ** 2) % N **2
        print("明文2加密后的密文为：", c2)
        c=(c1%N**2) * (c2 % N ** 2) % N**2
        print("密文为相乘后得到：", c)
        return c

    def gen_Key(self):
        p,q=self.get_pq()
        print('p = ',p)
        print('q = ',q)

        N,x=self.calculate_N(p,q)
        print("N = ",N)
        print("x = ",x)
        g,u=self.get_random(N,x)
        print("g = ",g)
        print("u = ",u)

        self.pubKey=[N,g]
        self.priKey=[x,u]
        print("publicKey = ",self.pubKey)
        print("priverKey = ",self.priKey)

    #加密
    def encode(self,message):
        return self.enc_m(self.pubKey,message)

    #解密
    def decode(self,message):
        return self.dec_c(self.pubKey[0],self.priKey,message)

    #相加
    def plus(self,message1,message2):
        return self.com(message1,message2,self.pubKey,self.pubKey[0])
