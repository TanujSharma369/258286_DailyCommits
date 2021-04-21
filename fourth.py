class ParkingLot:
    slots = []

    def __init__(self, big, medium, small):
        self.slots = [big, medium, small]

    def add_car(self, car_type):
        if self.slots[car_type-1] > 0:
            self.slots[car_type-1] -= 1
            return True
        return False


if __name__ == "__main__":
    parking_lot = ParkingLot(1, 1, 0)
    print("Add car on big slot " + str(parking_lot.add_car(1)))
    print("Add car on medium slot " + str(parking_lot.add_car(2)))
    print("Add car on small slot " + str(parking_lot.add_car(3)))
