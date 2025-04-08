from collections import deque
from copy import deepcopy

def island(maps,w,h): #섬 개수 카운트
    result = 0 #섬 개수
    
    for x in range(h): #순회하며 안전영역 찾기
        for y in range(w):
            # 안전한 지역이고 아직 방문하지 않은 경우
            if maps[x][y] == 1:
                result += 1
                que = deque()
                que.append([x, y])
                maps[x][y] = 0  # 방문 표시
                
                while que:
                    a, b = que.popleft()

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                        na, nb = a + dx, b + dy

                        if 0 <= na < h and 0 <= nb < w:
                            if maps[na][nb] == 1:
                                maps[na][nb] = 0
                                que.append([na, nb])

    return result


while 1:
    #입력받기
    w,h = input().split()
    w,h=int(w),int(h)
    if w+h==0: #0 0 이면  종료
        break
    maps = []

    for x in range(h):
        lines = list(map(int, input().split()))
        maps.append(lines) 

    print(island(maps,w,h))