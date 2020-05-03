
import HumanEntity

class Guest(HumanEntity.HumanEntity):
    
    def __init__(self, expiryDate, id, accessLevel):
        self.expiryDate = expiryDate
        self.id = id
        self.accessLevel = accessLevel