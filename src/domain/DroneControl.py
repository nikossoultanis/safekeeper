class DroneControl:
    def connectToDrone(drone_id):
        if drone_id == 1:
            print("Connected to drone")
            return True
        else: 
            print("Could Not Connect to drone")
            return False


    def checkInactivity(drone_id):
        if drone_id == 1:
            print("Drone is active")
            return False
        else: 
            print("Drone isnt active")
            self.autoRecall(drone_id)
            return True

    def autoRecall(drone_id):
        if self.connectToDrone(drone_id):
            print("Recalling Drone")
        else
            print("Drone isnt online")

    def recogniseIncident(drone_id):
        #todo

    def photosAndLivestream(drone_id):
        #todo

    def backOnline(drone_id):
        #dummy
        return True

        
