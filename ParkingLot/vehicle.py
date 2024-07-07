from abc import ABC
from vehicle_type import VehicleType


class Vehicle(ABC):
    def __init__(self, license_plate:str, vehicle_type:VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.vehicle_type
