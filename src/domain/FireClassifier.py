

import IncidentClassifier

class FireClassifier(IncidentClassifier.IncidentClassifier):
    def __init__(self, incidentOccured, isFire):
        super().__init__(self, incidentOccured)
        self.isFire = isFire