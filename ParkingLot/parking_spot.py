from vehicle import Vehicle
from vehicle_type import VehicleType


class ParkingSpot:
    def __init__(self, spot_number: int, vehicle_type:VehicleType= VehicleType.CAR):
        self._spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.parked_vehicle = None

    def get_spot_number(self) -> int:
        return self._spot_number

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle:Vehicle) -> None:
        if self.is_available() and vehicle.vehicle_type == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid Vehicle type or Unavailable Slot ")

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None



