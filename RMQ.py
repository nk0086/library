class Segment_tree:
    
    def __init__(self, n, init_val):
        self.max_val = 10**10
        self.num_min = pow(2, (n-1).bit_length())
        self.arr = [self.max_val] * 2 * self.num_min

        for i in range(n):
            self.arr[i+self.num_min-1] = init_val[i]

        for i in range(self.num_min-2, -1, -1):
            self.arr[i] = min(self.arr[2*(i+1)-1], self.arr[2*(i+1)])
    
    #区間の更新:arr[k]をxに更新する
    def update(self, k, x):
        k += self.num_min-1
        self.arr[k] = x

        while k:
            k = (k-1)//2
            self.arr[k] = min(self.arr[2*k+1], self.arr[2*k+2])

    #[s, t)の最小を求める
    def query(self, s, t):
        res = self.max_val
        s += self.num_min-1
        t += self.num_min-2

        while t - s > 1:
            #s: 区間の左端 t: 右端
            #arr[s]の親nodeに対して右側の時上に遷移する必要はない
            if s&1 == 0:
                res = min(res, self.arr[s])
            
            #arr[t]の親nodeに対し左側の時上に遷移する必要はない
            if t&1 == 1:
                res = min(res, self.arr[t])
                t -= 1

            s //= 2
            t = (t-1)//2
        
        return min(res, self.arr[s], self.arr[t])

#使用例
n, q = map(int, input().split())
S = Segment_tree(n, [pow(2, 31) - 1] * n)

for _ in range(q):
    com, x, y = map(int, input().split())
    if com:
        print(S.query(x, y+1))
    else:
        S.update(x, y)
        
        
