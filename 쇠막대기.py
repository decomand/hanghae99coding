
#라인을 입력받는다.

#반복문을통해 아래 규칙에 따라 순회
'''
1. ( 다음항목이바로 ) 일경우 레이저로 판단
2. 1번이 아닌경우 ( 이 나오면 리스트에 값 1 하나 추가 
3. 만약 레이저로 판단될시, 모든 0이아닌 리스트값은 +1 
4. ) 가 나온경우 순서대로 값 추출후 0으로 변환
'''

thick_and_hard = input()

razer_pass=0 #레이저 판별을 위함
block=[] #막대를 담아두는곳
result=0 #정답을 담는곳

for work in range(len(thick_and_hard)):

    #이전 작업이 레이저작업일경우 패스
    if razer_pass==1: 
        razer_pass=0
        continue

    #레이저일경우
    if thick_and_hard[work] == '(' and thick_and_hard[work+1] ==')': 
        razer_pass=1 
        result+=len(block) #블록커팅
        continue

    #막대 등장
    if thick_and_hard[work] == '(':
        block.append(1)
        result+=1
    
    #막대 끝
    if thick_and_hard[work] == ')':
        block.pop(0)

print(result)


