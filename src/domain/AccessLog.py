class AccessLog:
    @staticmethod
    def writeFailedCheckInOut(reason):
        print(f'FailedCheckInOut {reason}')

    @staticmethod
    def writeCheckInOut(user, isCheckIn):
        print(f'WriteCheckInOut {user}, check in: {isCheckIn}')

    @staticmethod
    def writeIncidentToAccessLogs(incident):
        print(f'Write incident to access logs: {incident}')
