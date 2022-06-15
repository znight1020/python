'''
class Person:
    def greeting(self):
        print("안녕하세요.")

class Student(Person):
    def study(self):
        print("공부하기")


class PersonList():
    def __init__(self):
        self.Person_list = []

    def append_person(self, person):
        self.Person_list.append(person)

james = Student()
james.greeting()
james.study()
'''
'''
# 기반 클래스의 속성 사용하기, 메서드 오버라이딩 사용하기, 다중상속
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

    def greeting(self):
        print('안녕하세요')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school = '파이썬 코딩 도장'

    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩 도장 학생입니다')
'''
'''
james = Student()
print(james.school)
print(james.hello)
james.greeting()

###
james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()
'''
#메서드 탐색 순서 확인하기 10주차 2 27분

#추상클래스 사용하기

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기') # go_to_school 메서드 구현하지 않아서 에러 발생

    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()