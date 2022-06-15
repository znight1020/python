# 가방을 공유하게 됨
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag("책")

maria = Person()
maria.put_bag("열쇠")

print(james.bag)
print(maria.bag)

# 인스턴스 속성 사용하여 개인 가방 만들기
class Person:
    bag = []

    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag("책")

maria = Person()
maria.put_bag("열쇠")

print(james.bag)
print(maria.bag)