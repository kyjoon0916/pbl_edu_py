import random

b=1
print("-"*18)
print("행운의 번호 생성 프로그램")
print("-"*18)
while True:
    a = random.randrange(10,61)
   
    print("%d 번째 번호는 %d 입니다." %(b,a))
    
    b +=1
    if b ==8:
        break