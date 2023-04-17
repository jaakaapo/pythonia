class Car():
    def __init__(self, malli) -> None:
        self.malli = malli

    def merkki(self):
        print("Auton merkki on", self.malli)

if __name__ == "__main__":
    auto = Car("Fiat")
    auto.merkki()
