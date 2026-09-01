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
    print("=== Garden Plant Growth ===")
    rose = Plant('Rose', 25.0, 30, 0.8)
    start_height: float = rose.height
    rose.show()
    for i in range(1, 8):
        print(f'=== Day {i} ===')
        rose.grow()
        rose.age()
        rose.show()
    print(f'Growth this week: {round(rose.height - start_height, 1)}cm')
