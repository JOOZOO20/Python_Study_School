a=int(input('숫자 입력해: '))
n=a


for j in range((a//3)+2):
    print('\t',end='')
    print(' '*j,end='')
    print('*'*n)
    n-=2