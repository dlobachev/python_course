def ladders(k, n):
    ans = 0
    if n == 0:
        return ans+1
    elif k < n:
        for i in range(k+1, n+1):
            ans += ladders(i, n-i)
        return ans
    else:
        return ans


for i in range(100):
    print(ladders(0, i))

