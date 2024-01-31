import ships_inventory as inventory
from ships_inventory import FleetVessel

ship_data = inventory
enterprise = FleetVessel()

# Bad practice - directly accessing class members instead of using getters/setters
# But this is simulating a project that I'm working on
enterprise.ship_name = "U.S.S. Enterprise"
enterprise.ship_registration = "NCC-1701"
enterprise.current_status = FleetVessel.Status.ACTIVE.value

# Accessing the module with data from the FleetVessel class
# ship_data.set_ship_name(enterprise.ship_name)
# ship_data.set_ship_registration(enterprise.ship_registration)
# ship_data.set_ship_status(enterprise.current_status)

ship_data.active_ship_info(enterprise, "Constellation", "Captain Christopher Pike", "Science/Exploration")

vessel = FleetVessel()
print(vessel._scratch_variable)