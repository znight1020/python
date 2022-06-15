class Knight:
    __item_limit = 10

    def print_item_limit(self):
        print(Knight.__item_limit)

x = Knight()
x.print_item_limit()

# print(Knight.__item_limit) 오류

# 정적 메소드 사용하기
class Calc:
    @staticmethod
    def add(a,b):
        print(a + b)
    @staticmethod
    def mul(a,b):
        print(a * b);

Calc.add(10,20) #클래스에서 바로 메서드 호출
Calc.mul(10,20)

# 클래스 메서드 사용하기
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count() # 2명 생성되었습니다.