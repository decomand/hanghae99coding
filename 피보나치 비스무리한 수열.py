
#입력값 받기
n=int(input())
#기본수열생성
pibo=[1,1,1]
count=3
while 1:
    if count>=n:#n이상이면 멈춤
        break
    pibo.append(pibo[count-3]+pibo[count-1]) #점화식
    count+=1 #다음숫자

print(pibo[-1])#맨마지막숫자 출력 (n번째)
