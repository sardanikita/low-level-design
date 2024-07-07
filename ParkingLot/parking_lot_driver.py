from parking_lot import ParkingLot
from level import Level
from car import Car
from truck import Truck
from motorcycle import Motorcycle
from vehicle_type import VehicleType


class ParkingLotDriver:
    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_levels(Level(1,50))
        parking_lot.add_levels(Level(2, 50))

        car = Car('xsd')
        truck = Truck("XYZ789")
        motorcycle = Motorcycle("M1234")

        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)
        parking_lot.display_availability()
        parking_lot.unpark_vehicle(motorcycle)
        parking_lot.display_availability()


if __name__ == "__main__":
    ParkingLotDriver.run()


