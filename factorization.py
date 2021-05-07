def prime_factorization(n):
    #素因数分解の結果を辞書に保存して返す
    #1の時は空の辞書を返す
    num = int(n ** 0.5)
    rec = dict()
    for prime in range(2, num + 2):
        if n % prime == 0:
            cnt = 0
            while True:
                if n % prime != 0:break
                cnt += 1
                n = n // prime
            rec[prime] = cnt

    if n != 1:rec[n] = 1
    return rec

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])

    return arr