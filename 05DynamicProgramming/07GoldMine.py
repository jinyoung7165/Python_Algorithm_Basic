#n*m크기 금광. 각 칸에 특정 크기의 금광이 들어있음
#첫번째 열부터 출발해 금을 캔다
#맨처음에는 첫번째열의 어느행에서든 출발 가능
#이후 m-1번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 중 하나로 이동 가능
#채굴자가 얻을 수 있는 금의 최대 크기
#왼쪽 위에서 오는 경우. 왼쪽 아래서 오는 경우, 왼쪽에서 오는 경우를 고려
#arr[i][j]:i행j열에 존재하는 금의 양
#dp[i][j]:i행j열까지의 최적의 해(금의 양)
#dp[i][j]=arr[i][j]+max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])
#테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크
#테스트 케이스 입력
for tc in range(int(input())):
    #금광 정보 입력
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    dp=[]
    index=0
    for i in range(n):
        dp.append(arr[index:index+m])
        index+=m
    #다이나믹 프로그래밍 진행
    for j in range(1,m):#열기준,오른쪽으로 이동해 나가며 각 열마다 전체 행 확인
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i==0:left_up=0 #map을 벗어나는 경우 초기화
            else:left_up=dp[i-1][j-1]
            #왼쪽 아래서 오는 경우
            if i==n-1:left_down=0 #map을 벗어나는 경우 초기화
            else:left_down=dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left=dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    result=0
    for i in range(n):
        result=max(result,dp[i][m-1]) #마지막 행의 열들까지 저장한 금의 양 중 최댓값
    print(result)