
class FuelStation:
    
    def __init__(self, diesel: int, petrol: int, electric: int):
        
        self.fuel_slots: dict[str, int] = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }
        self.fuelling: dict[str, int] = {
            "diesel": 0,
            "petrol": 0,
            "electric": 0
            } 
        
    def fuel_vehicle(self, fuel_type: str) -> bool:
        
        if self.fuelling[fuel_type] < self.fuel_slots[fuel_type]:
            self.fuelling[fuel_type] += 1
            
            return True
        else:
            return False
    
    def open_fuel_slot(self, fuel_type: str) -> bool:
        if self.fuelling[fuel_type] > 0: 
            self.fuelling[fuel_type] -= 1
            
            return True
        else:
            return False        
        
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

print(fuel_station.fuel_vehicle("diesel")) # true
print(fuel_station.fuel_vehicle("petrol")) # true
print(fuel_station.fuel_vehicle("diesel")) # true
print(fuel_station.fuel_vehicle("electric")) # true
print(fuel_station.fuel_vehicle("diesel")) # false
print(fuel_station.open_fuel_slot("diesel")) # true
print(fuel_station.fuel_vehicle("diesel")) # true
print(fuel_station.open_fuel_slot("electric")) # true
print(fuel_station.open_fuel_slot("electric")) # false
