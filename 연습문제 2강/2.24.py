n=int(input('세 자리 정수를 입력하세요 : '))
other=n%100
print('일의 자리 :',other%10)
print('십의 자리 :',other//10)
print('백의 자리 :',n//100)