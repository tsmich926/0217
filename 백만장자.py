def baeckman(prices):
    max_P = 0
    benef = 0 #위치 고치기
    for Price in Prices:
        if max_P < Price:
            max_P = Price
    idx = Prices.index(max_P)
    if idx != 0:
        PL = Prices[0:idx]
        buy = 0
        for i in PL:
            buy += i
        sell_P = Prices[idx] * idx
        benef = sell_P - buy
        return benef
    else:
        benef = 0
        return  benef
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Prices = list(map(int,input().split()))
    ans =baeckman(Prices)
    print(f'#{tc} {ans}')

    ---------------------


    def baeckman(prices):
        max_P = 0
        benef = 0# 위치 고치기
        for i in range(len(Prices)):
            if max_P < Price:
                max_P = Price
        idx = Prices.index(max_P)
        if idx != 0:
            PL = Prices[0:idx]
            buy = 0
            for i in PL:
                buy += i
            sell_P = Prices[idx] * idx
            benef = sell_P - buy
            return benef
        else:
            benef = 0
            return benef


    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        Prices = list(map(int, input().split()))
        ans = baeckman(Prices)
        print(f'#{tc} {ans}')
-----------------------------------
T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        Prices = list(map(int, input().split()))
        i = ans = 0
        while i <N: #i부터 끝까지 최대갑 인덱스 찾기
            i_mx = i
            for j in range(i+1,N):
                if lst[i_mx]<lst[j]:
                    i_mx =j
            #i부터i_mx까지의 최대값과 차이 누적
            for j in range(i,i_mx):
                ans += lst[i_mx]-lst[j]
            i = i_mx + 1

    print(f'#{tc} {ans}')

------------------
#기준값 뒤에서 정하기
#작은값- 차이계산, 큰값-최대값갱신
T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        lst = list(map(int, input().split()))
        anx = mx = 0
        for n in lst:
            if mx>n:
                ans += mx-n
            else:
                max = n
    print(f'#{tc} {ans}')


------------------------------
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in lst:
        if mx > n:
            ans += mx - n
        else:
            mx = n

    print(f'#{test_case} {ans}')