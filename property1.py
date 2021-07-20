# -*- coding: utf-8 -*-
"""
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
"""

class PropertyClass:
      def __init__(self, msg):
        self.message = msg

      def __str__(self):
        return self.message
"""
      @property
      def message(self):
        return self.__message

      @message.setter
      def message(self, value):
        if value != '':
          self.__message = value
"""

pc= PropertyClass('Hello')
pc1 = PropertyClass('Hello1')

print(pc.message)
print(pc1.message)

pc.message = 'Hello1'
print(pc.message)