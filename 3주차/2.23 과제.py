# 사용자로부터 세 자리 정수를 입력받아 백의 자리, 십의 자리, 일의 자리의 값을 출력하는 문제

number = int(input('세 자리의 정수를 입력하세요 : '))
a = number//100
print('백의 자리 : ',a)
a = number % 100
print('십의 자리 : ',a//10)
print('일의 자리 : ',a%10)