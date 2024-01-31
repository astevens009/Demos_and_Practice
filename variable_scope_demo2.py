# TODO: Create a class and modify the global variable
class StarfleetShip:
    global ship_status

    def __init__(self, registration, ship_name):
        self.ship_reg = registration
        self.ship_name = ship_name

    def set_ship_status(self):
        ship_status = 'Being repaired'
    

# TODO: Create a second class and display the value of the global variable 
class Foo:
    global ship_status
    
    def get_ship_status(self):
        return ship_status

if __name__ == '__main__':
    # TODO: Declare a global variable to be used in both classes
    ship_status = 'Active'

