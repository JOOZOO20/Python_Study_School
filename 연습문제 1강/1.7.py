a=int(input('숫자 입력하세요: '))
n=a

for i in range(1,a+1,2):
    print('\t',end='')
    print(' '*(n//2),end='')
    print('*'*i)
    n-=2