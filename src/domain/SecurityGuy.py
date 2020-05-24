
from . import Employee

class SecurityGuy(Employee.Employee):
    def __init__(self, fullname, id, accessLevel, pin):
        super().__init__(self, fullname, id, accessLevel)
        self.pin = pin
    
    @staticmethod
    def doesPinExist(pin):
        # this is the database
        return pin in [1234, 5678, 1111, 0000, 9999]
