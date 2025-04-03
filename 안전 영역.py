from collections import deque
from copy import deepcopy

def rains(maps, sheep): #맵과 강수량입력되면 계산
    langemap = len(maps)
    result = 0 #안전영역 개수
    visited = [[False for _ in range(langemap)] for _ in range(langemap)]
    
    for x in range(langemap): #순회하며 안전영역 찾기
        for y in range(langemap):
            # 안전한 지역이고 아직 방문하지 않은 경우
            if maps[x][y] > sheep and not visited[x][y]:
                result += 1
                que = deque()
                que.append([x, y])
                visited[x][y] = True  # 방문 표시
                
                while que:   #상하 좌우 좌표 큐에넣기
                    xy = que.popleft()
                    a, b = xy[0], xy[1]
                    
                    if a-1 >= 0 and maps[a-1][b] > sheep and not visited[a-1][b]:
                        visited[a-1][b] = True  # 방문 표시
                        que.append([a-1, b])
                    if a+1 < langemap and maps[a+1][b] > sheep and not visited[a+1][b]:
                        visited[a+1][b] = True  # 방문 표시
                        que.append([a+1, b])
                    if b-1 >= 0 and maps[a][b-1] > sheep and not visited[a][b-1]:
                        visited[a][b-1] = True  # 방문 표시
                        que.append([a, b-1])
                    if b+1 < langemap and maps[a][b+1] > sheep and not visited[a][b+1]:
                        visited[a][b+1] = True  # 방문 표시
                        que.append([a, b+1])

    return result

#입력받기
N = int(input())

maps = []
maxrain = 0
for x in range(N):
    lines = list(map(int, input().split()))
    if max(lines) > maxrain:
        maxrain = max(lines)
    maps.append(lines)

maxresult = 0

for x in range(0, maxrain+1):  # 0부터 최대 높이까지 확인
    counts = rains(maps, x)
    if counts > maxresult:
        maxresult = counts

print(maxresult)