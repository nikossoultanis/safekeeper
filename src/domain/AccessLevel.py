
class AccessLevel:
    @staticmethod
    def isAccessLevelValid(guestsAllowed, level):
        return (guestsAllowed and level < 2) or (level >= 3 and not guestsAllowed)

    def __init__(self, guestsAllowed, level):
        self.guestsAllowed = guestsAllowed
        self.level = level