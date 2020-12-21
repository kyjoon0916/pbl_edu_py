
print("1부터 10까지수를 입력하시오")
while True:
    try:
        ipt =int(input())
        star =[]
        break
    except ValueError:
        print("다시입력하시오")
        continue
    
for i in range(1,ipt+1):
    if ipt % i == 0:
        star.append(i)
for j in star:
    print("*"*j)
