import HumanEntity

class Employee(HumanEntity.HumanEntity):

    def __init__(self, fullname, id, accessLevel):
        super().__init__(fullname)
        self.id = id
        self.accessLevel = accessLevel

