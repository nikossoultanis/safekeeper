
import Employee

class SecurityGuy(Employee.Employee):
    def __init__(self, fullname, id, accessLevel, pin):
        super().__init__(self, fullname, id, accessLevel)
        self.pin = pin

        