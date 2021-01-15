n=int(input('정수를 입력하시오 : '))
print('{} 의 2진수 값 : {}'.format(n,bin(n)))
print('{}의 2진수 값에 대한 비트단위 부정값 : {}'.format(n,bin(~n)))