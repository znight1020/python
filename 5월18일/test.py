div = 0
try:
    x = int(input('첫번째 수 입력'))
    y = int(input('두번째 수 입력'))
    div = x / y
except ZeroDivisionError as e:
    print('나누기 에러 발생했지롱')
except ValueError:
    print('정수가 아닙니다.')
else:
    print('제대로 나누기를 합니다')
finally:
    print(div)