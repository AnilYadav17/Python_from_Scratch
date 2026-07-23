#Python uses Abstract classes for it. 
# Abstract class is a class that can not be instanciated. 
# It acts as an blueprint for other classes.


from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass


obj = Bank()
obj.interest()


#ABC stands for Abstaract Base Class 
#it is an built in module in Python that helps us to create Abstract classes ans Abstract Methods .

            #ABC#
#It is a Base class use to create abstract class.


            #abstractmethod 
#It is a decorator use to declare a method without implementation.
#It force the child class to implement that method.

