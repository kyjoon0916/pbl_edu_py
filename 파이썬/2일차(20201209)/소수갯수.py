x = int(input())
num = 2
a =[]
while num <= x:
    count = 0  # 약수의 개수를 세어줄 변수
    i = 1  # 1~num까지 증가할 변수
    while i <= num:
        if num % i == 0:  # 나누어지면 약수
        
            count += 1
        i += 1  # 1증가
    if count == 2:  # 약수의 개수가 2개면 출력
        a.append(num)
    num += 1 # 판별수 증가
print(len(a))
