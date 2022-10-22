#Functional Prompt
#Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a function programming prardigm




#Object Oriented Prompt
#First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
from typing_extensions import Self


class Podracer(Self):
  def __init__(max_speed, condition, price): 
    Self.max_speed = max_speed
    Self.condition = condition
    Self.price     = price

#define a repair() method that will update the condition of the podracer to "repaired".
  def get_repair(self):
    self.condition = "Repaired"

#Define a new class, AnakinsPod that inherits the Podracer class,
#  but also contains a special method called boost that will 
# multiply max_speed by 2.

class AnakinsPod(Podracer):
  def __init__(max_speed, condition, price):
    super().__init__(max_speed, condition, price)

    def boost(self):
        max_speed *= 2

#Define another class that inherits Podracer and call this one
#  SebulbasPod. This class should have a special method called 
# flame_jet that will update the condition of another podracer to "trashed"

class SebulbasPod(Podracer):
    def __init__(max_speed, condition, price):
       super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "Trashed"


