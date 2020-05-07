
class EmployeeSchedule:
    
    @staticmethod
    def isPinActiveNow(pin) -> bool:
        if pin == 9999: # select this pin to be inactive (this is the database)
            return False
        
        return True