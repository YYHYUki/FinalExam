def count(li, m):
    cnt = 0
    for n in li:
        cnt += (n // m)
    return cnt
            
def binarySearch(li, K):
    s, e = 1, max(li)
    while s <= e:
        m = (s + e) // 2
        if count(li, m) >= K:
            ans = m
            s = m + 1
        else:
            e = m - 1
    return ans
    
    
N, K = map(int, input().split())
li = sorted([int(input()) for _ in range(N)])

print(binarySearch(li, K))