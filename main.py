'''
Functional Prompt
    Implement a function that will flatten and sort an array of integers in ascending order,
    and which adheres to a function programming prardigm
'''
def flat_and_sort(array):
    array = []
    for item in array:
        for i in item:
            array.append(i)
        
        return sorted(array)
'''
How does this solution ensure data immutability?
    This soltion ensures data immutability because everything it outputs is based on everything that is inputed. 
    In this case the array being within the function prevents immutability.

Is this solution a pure function? Why or why not?
    The solution is a pure function becuase there are no side effects.and the output is strictly dependent on the input 

Is this solution a higher order function? Why or why not?
    This soulution is not a higher order function becuase a function is not passed as a argument

Would it have been easier to solve this problem using a different programming style?
    For this particular problem. The functional programming method appears to be the easiest method
    because we needed a function to flatten and sort which makes functional programming easier because 
    it allows us to tell what we want it to do. 

Why in particular is functional programming a helpful paradigm when solving this problem?
    with functional programming it allows one to tell the program exactly what it wants to do. in this case
    we were able to tell the program exactly what we wanted it to do which was flatten and sort. OPP doesnt allow for that
    instead it allows us to tell the program how to obtain results by altering state through object.
'''


'''
Object Oriented Prompt

    First, he'll need a general Podracer class defined with max_speed, 
    condition (perfect, trashed, repaired) and price attributes.

'''
class Podracer:
  def __init__(self,max_speed, condition, price): 
    self.max_speed = max_speed
    self.condition = condition
    self.price     = price

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


'''

Object Oriented Question Anwers

        1a. Inheritance was demonstrated because everyone of the classes inheirited the parent class Podracer
           b.Abstraction was also demonstrated because it allows the cose to be reused  and each class 
              #has the same interface
           c.Abstraction was also present because boost mode is implemented a person may use boost mode,
              #but doesnt understand the math behind it

        2. No, as I believe that this would be the easiest way to code this problem. using OOP
            because this method allows for more code flexibility and reusability and allows it to be easier 
            to read. as oppose to other methods which could be more repetitive and lengthy.
        
        3. OOP assisted with the solving for this problem because it used 3/4 pillars which, allowed for the 
            code to be cleaner with less repetition because it allows for reusability, flexibility and readability.

'''