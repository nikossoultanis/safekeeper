import SecurityIncident

class PerimeterMonitoringEvent(SecurityIncident.SecurityIncident):
    def __init__(self, description, sector, time, securityGuyId, employeeId, cause, incidentType):
        super().__init__(self, description, sector, time, securityGuyId, employeeId, cause, incidentType)