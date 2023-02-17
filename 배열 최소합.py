def per(k, curS):
    global minV
    if minV < curS:
        return
    if k == N:
        # print(bits)
        # sumV = 0
        # for i in range(N):
        #     # col = bits[i]
        #     # row = i
        #     sumV += arr[i][bits[i]]
        # if minV > sumV:
        #     minV = sumV
        if minV > curS:
            minV = curS
        return
 
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            bits[k] = i
            per(k+1, curS+arr[k][i])
            visited[i] = 0
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
 
    minV = 10000000
    bits = [-1] * N
    visited = [0] * N
    per(0, 0)
    print(f'#{t} {minV}')