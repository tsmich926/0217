def RPS(a,b): #가위바위보
    if card[a] == card[b]: #비긴경우에 값 반환
        return a
    elif card[a] - card[b] == 1 or card[a] - card[b] == -2:
        return a
    else:
        return b
 
def sp(x,y): #나누기
    if x == y:
        return x
 
    osp = sp(x,(x+y)//2)
    isp  = sp((x+y)//2+1,y)
    return RPS(osp,isp)
 
T = int(input())
for tc in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc+1} {sp(0, N-1)+1}')
