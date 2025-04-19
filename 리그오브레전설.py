def count_skill_combinations(N, M):
    MOD = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1  # 0초에는 아무 스킬도 사용하지 않는 1가지 방법
    
    for i in range(1, N + 1):
        dp[i] = dp[i - 1]  # 이전 시간에 A를 추가하는 경우
        
        if i >= M:
            dp[i] = (dp[i] + dp[i - M]) % MOD  # 이전 시간에 B를 추가하는 경우
    
    return dp[N]

# 입력 받기
N, M = map(int, input().split())

# 결과 출력
result = count_skill_combinations(N, M)
print(result)