# -*- coding: utf-8 -*-

class Cat:
    def __init__(self):
        self.name = "ミケ"
        
    def get_name(self):
        return self.name

cat = Cat()
print(cat.name)

cat1 = Cat()
print(cat1.name)
print(cat1.get_name())