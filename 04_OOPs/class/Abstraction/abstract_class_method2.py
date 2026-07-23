#ABC providing the template for its child classes.


from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass


class SBI(Bank):
    def interest(self):
            print("SBI interest 8.0")


class HDFC(Bank):
    pass

obj = SBI()
obj.interest()

obj1=HDFC()
obj1.interest()