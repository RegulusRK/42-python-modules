class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f'{self.name}: {round(self.height, 1)}cm, {self.days} days old')


if __name__ == "__main__":
    print('=== Plant Factory Output ===')
    rose = Plant("Rose", 25.0, 30, 0)
    print('Created: ', end='')
    rose.show()
    oak = Plant("Oak", 200.0, 365, 0)
    print('Created: ', end='')
    oak.show()
    cactus = Plant("Cactus", 5.0, 90, 0)
    print('Created: ', end='')
    cactus.show()
    sunflower = Plant("Sunflower", 80.0, 45, 0)
    print('Created: ', end='')
    sunflower.show()
    fern = Plant("Fern", 15.0, 120, 0)
    print('Created: ', end='')
    fern.show()
