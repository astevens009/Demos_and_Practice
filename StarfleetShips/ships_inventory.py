"""
@author: A. Stevens
@date : 10/31/2023
@description:
Demo code to practice and understand classes in Python
"""

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
        """
        FleetVessel status constants
        """
        COMMISSIONED = "Commissioned"
        ACTIVE = "Active"
        DECOMMISSIONED = "Decommissioned"
        REPAIRED = "Being Repaired"
        ON_ASSIGNMENT = "On_Assignment"
        DESTROYED = "Destroyed"
        MISSING = "Missing"
    
    def __init__(self, registration = None, name = None, status = Status.COMMISSIONED.value):
        self.ship_registration = registration
        self.ship_name = name
        self.current_status = status
        self._scratch_variable = 'I am a rogue variable'
        
    def __str__(self):
        return(f"\nShip Information:\n{self.ship_name}\nRegistration ID: {self.ship_registration}\nCurrent Status: {self.current_status}\n")
    
# region Instantiating the Class
    # """
    # Instantiating the class so that we can access its members. To be defined at a later time.
    # """
    
    # fleet_ship = FleetVessel()
# endregion
    
def get_ship_name(ship : FleetVessel):
    """
    Getter to access the vessel's name. The FleetVessel object that is instantiated 
    outside the class is passed in
    """
    return ship.ship_name

def get_ship_registration(ship: FleetVessel):
    """
    Getter to access the vessel's registration ID. The FleetVessel 
    object that is instantiated outside the class is passed in
    """
    return ship.ship_registration

def get_ship_status(ship : FleetVessel):
    """
    Getter to access the vessel's current. The FleetVessel object that is instantiated 
    outside the class is passed in
    """
    return ship.current_status

def set_ship_name(ship : FleetVessel):
    """
    Setter to modify the vessel's name. The FleetVessel object that is instantiated 
    outside the class is passed in
    """
    if ship.ship_name is None or ship.ship_name == "":
        logging.warning("The ship has no name. The ship instance doesn't exist yet.")
    else:
        ship.self.ship_name = ship.ship_name

def set_ship_registration(ship: FleetVessel):
    """
    Setter to modify the vessel's registration ID. The FleetVessel object that is instantiated 
    outside the class is passed in
    """
    if ship.ship_registrtion is None or ship.ship_registration == "":
        logging.warning("The ship has no registration. The ship instance doesn't exist yet.")
    else:
        ship.self.ship_registration = ship.ship_registration

def set_ship_status(ship : FleetVessel):
    """
    Setter to modify the vessel's current. The FleetVessel object that is instantiated 
    outside the class is passed in
    """
    if ship.current_status is None or ship.current_status == "":
        logging.warning("The ship has no current status. The ship instance doesn't exist yet.")
    else:
        ship.self.current_status = ship.current_status
    
# TODO: Create a method with variables in the block and find a way to access them from an instantiated object
def active_ship_info(ship : FleetVessel, ship_class = "", commander = "", first_officer = "", mission = ""):
    ship_class = ship_class
    ship_commander = commander
    ship_first_officer = first_officer
    ship_mission = mission

    formatted_display = f"\n{get_ship_name(ship)}\nRegistration: {get_ship_registration(ship)} - Class: {ship_class}\nCommander: {ship_commander}\nCurrent Status: {get_ship_status(ship)}"
    print(formatted_display)


if __name__ == '__main__':
    pass