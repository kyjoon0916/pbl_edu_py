#숫자를 입력 받아 원의 두레와 면적을 계산하는 프로그램 작성
Pi=3.14
n = int (input("input a number: "))
print("circumference = %5.1f" %(Pi*2*n))
print("Area = %5.1f" %(Pi*n**2))