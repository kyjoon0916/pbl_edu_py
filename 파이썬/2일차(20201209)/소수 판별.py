ipt = int(input())              #판별 수
num =1                          #증가 수
count =0                        #약수 개수
while num <=ipt:
    
    if ipt % num ==0:
        count +=1
    num+=1
if count ==2:
    print("%d = 소수입니다"%ipt)
else:
    print("%d = 소수아닙니다"%ipt)
    