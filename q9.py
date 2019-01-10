# 9. Write a program illustrating overriding method in program
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1

c = Child()
print(c.get_value())
# 6