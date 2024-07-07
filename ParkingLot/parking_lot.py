from level import Level
from vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("ParkingLot class is not instantiated")
        else:
            ParkingLot._instance = self
            self.levels = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_levels(self, level:Level)-> None:
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()
