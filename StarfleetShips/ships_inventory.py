class FleetVessel:
    def __init__(self, registration, name, status):
        self.ship_registration = registration
        self.ship_name = name
        self.current_status = status
        
    def __str__(self):
        return(f"\nShip Information:\n{self.ship_name}\nRegistration ID: {self.ship_registration}\nCurrent Status: {self.current_status}\n")
    
def get_ship_name(ship : FleetVessel):
    return ship.self.ship_name


    

# if __name__ == '__main__':
    