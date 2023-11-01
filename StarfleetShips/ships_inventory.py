import logging
from enum import Enum, auto

class FleetVessel:
    """
    Starfleet ship object
    @param registration : ship's registration ID
    @param name : ship's name
    @param statis : the current status of the ship
    """
    
    class Status(Enum):
        Commissioned = auto()
        Active = auto()
        Decommissioned = auto()
        Repairs = auto()
        On_Assignment = auto()
        Destroyed = auto()
        Missing = auto()
    
    def __init__(self, registration = None, name = None, status = Status.Commissioned):
        self.ship_registration = registration
        self.ship_name = name
        self.current_status = status
        
    def __str__(self):
        return(f"\nShip Information:\n{self.ship_name}\nRegistration ID: {self.ship_registration}\nCurrent Status: {self.current_status}\n")
    
# region Instantiating the Class
    """
    Instantiating the class so that we can access its members. To be defined at a later time.
    """
    
    # fleet_ship = FleetVessel()
# endregion
    
def get_ship_name(ship : FleetVessel):
    return ship.self.ship_name

def get_ship_registration(ship: FleetVessel):
    return ship.self.ship_registration

def get_ship_status(ship : FleetVessel):
    return ship.self.current_status

def set_ship_name(ship : FleetVessel):
    if ship.ship_name == None or ship.ship_name == "":
        logging.warn("The ship has no name. The ship instance doesn't exist yet.")
    else:
        ship.self.ship_name = ship.ship_name

def set_ship_registration(ship: FleetVessel):
    if ship.ship_registrtion == None or ship.ship_registration == "":
        logging.warn("The ship has no registration. The ship instance doesn't exist yet.")
    else:
        ship.self.ship_registration = ship.ship_registration

def set_ship_status(ship : FleetVessel):
    if ship.current_status == None or ship.current_status == "":
        logging.warn("The ship has no current status. The ship instance doesn't exist yet.")
    else:
        ship.self.current_status = ship.current_status
    

# if __name__ == '__main__':
    