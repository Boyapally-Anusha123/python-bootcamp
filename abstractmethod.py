from abc import ABC
class RBIBank(ABC):
    def interest():
        pass
    def loan():
        print("provides home loan")
class HDFC(RBIBank):
    def interest():
        print("7.5% interest")
class SBI(RBIBank):
    def interest():
        print("11% interest")
class AXIS(RBIBank):
    def interest():
        print("9% interest")
obj=AXIS
obj.interest()
obj.loan()
