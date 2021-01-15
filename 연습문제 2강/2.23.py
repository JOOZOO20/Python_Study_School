#세자리정수, 백의자리, 십의자리, 일의자리
number=int(input('세 자리 정수를 입력하세요 : '))
other=number%100
print('백의 자리 :',number//100)
print('십의 자리 :',other//10)
print('일의 자리 :',other%10)