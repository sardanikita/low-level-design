from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import VehicleType
from random import Random


class Level:
    def __init__(self, num, total_slots):
        self._id = num
        self._total_slots= total_slots
        self.parking_slots = [ParkingSpot(slot, VehicleType((slot%3)+1)) for slot in range(total_slots)]

    def get_level_number(self) -> int:
        return self._id

    def get_total_slots(self) -> int:
        return self._total_slots

    def park_vehicle(self, vehicle:Vehicle) -> bool:
        for slot in self.parking_slots:
            if slot.is_available() and slot.vehicle_type == vehicle.vehicle_type:
                slot.park_vehicle(vehicle)
                return True
        return False

    def unpark_vehicle(self, vehicle:Vehicle) -> bool:
        for slot in self.parking_slots:
            if slot.get_parked_vehicle() == vehicle:
                slot.unpark_vehicle()
                return True
        return False

    def display_availability(self) -> None:
        print(f"Availability of slots in Level {self.get_level_number()}")
        for slot in self.parking_slots:
            print(f"Slot {slot.get_spot_number()}: {'Available' if slot.is_available() else 'Occupied'}")


