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


#Object Oriented Question Anwers

        #1a. Inheritance was demonstrated because everyone of the classes inheirited the parent class Podracer
        #   b.Abstraction was also demonstrated because it allows the cose to be reused  and each class 
              #has the same interface
        #   c.Abstraction was also present because boost mode is implemented a person may use boost mode,
              #but doesnt understand the math behind it

        #2. No, as I believe that this would be the easiest way to code this problem. using OOP
            #because this method allows for more code flexibility and reusability and allows it to be easier 
            #to read. as oppose to other methods which could be more repetitive and lengthy.
        
        #3. OOP assisted with the solving for this problem because it used 3/4 pillars which, allowed for the 
            #code to be cleaner with less repetition because it allows for reusability, flexibility and readability.