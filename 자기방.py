#시작복도 번호 ~끝 복도번호 누적cnt표시
#최대값 찾기
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0]*200
    for _ in range(N):
        s, e =map(int,input().split())
        if s > e:
            s,e = e,s
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i] += 1
    ans = max(cnts)
    print(f'#{test_case} {ans}')


-------------------
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnts=[0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s>e:
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i]+=1
    ans = max(cnts)
    print(f'#{test_case} {ans}')