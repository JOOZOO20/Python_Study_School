print('섭씨\t\t화씨')

for celsius in range(0,60,10):
    fahrenheit = (9/5) * celsius + 32 # 섭씨온도(celsius)를 화씨온도(fahrenheit)로 변환하는 식
    print('{}\t\t\t{}'.format(celsius,fahrenheit))