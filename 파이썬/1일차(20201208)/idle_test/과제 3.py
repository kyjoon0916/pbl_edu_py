import random

b=1
while True:
    a = random.randrange(10,61)
    print("%d 번째 번호는 %d 입니다." %(b,a))
    b +=1
    if b ==8:
        break