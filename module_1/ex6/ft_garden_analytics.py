class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(f'Stats: {self._grow_calls} grow, '
                  f'{self._age_calls} age, '
                  f'{self._show_calls} show')

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

    def __init__(self, name: str, height: float, days: int,
                 growth: float) -> None:
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth = growth
        self.stats = Plant.Stats()

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = new_height

    def get_height(self) -> float:
        return (self._height)

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print('Age update rejected')
        else:
            self._days = new_age

    def get_age(self) -> int:
        return (self._days)

    def grow(self) -> None:
        self._height += self.growth
        self.stats.record_grow()

    def age(self, days: int = 1) -> None:
        self._days += days
        self.stats.record_age()

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, {self._days} days old"
            )
        self.stats.record_show()

    @staticmethod
    def is_older(days: int) -> bool:
        if (days > 365):
            return (True)
        return (False)

    @classmethod
    def empty_plant(cls) -> "Plant":
        new_plant = cls('Unknown plant', 0.0, 0, 0.0)
        return (new_plant)


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, days, growth)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f'Color: {self.color}')
        if (self.bloomed is True):
            print(f'{self.name} is blooming beautifully!')
        elif (self.bloomed is False):
            print(f'{self.name} has not bloomed yet')


class Tree(Plant):
    class StatsTree(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f'{self._shade_calls} shade')

        def record_shade(self) -> None:
            self._shade_calls += 1

    stats: "Tree.StatsTree"

    def __init__(self, name: str, height: float, days: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth)
        self.stats = Tree.StatsTree()
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter}cm')

    def produce_shade(self) -> None:
        print(
              f'Tree {self.name} now produces a shade of '
              f'{self._height}cm long and {self.trunk_diameter}cm wide.'
        )
        self.stats.record_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, growth: float,
                 harvest_season: str) -> None:
        super().__init__(name, height, days, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self.harvest_season}')
        print(f'Nutritional value: {self.nutritional_value}')

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, days, growth, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f'Seeds: {self.seeds}')

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


def show_statistics(plant: Plant) -> None:
    plant.stats.display()


if __name__ == "__main__":
    print('=== Garden statistics ===')
    print('=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.is_older(30)}')
    print(f'Is 400 days more than a year? -> {Plant.is_older(400)}')
    print('\n')
    print('=== Flower')
    rose = Flower('Rose', 15.0, 10, 8.0, 'red')
    rose.show()
    print('[statistics for Rose]')
    show_statistics(rose)
    print('\n[asking the rose to grow and bloom]')
    rose.bloom()
    rose.grow()
    rose.show()
    print('[statistics for Rose]')
    show_statistics(rose)
    print('\n')
    print('=== Tree')
    oak = Tree('Oak', 200.0, 365, 0.0, 5.0)
    oak.show()
    print('[statistics for Oak]')
    show_statistics(oak)
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print('[statistics for Oak]')
    show_statistics(oak)
    print('\n')
    print('=== Seed')
    sunflower = Seed('Sunflower', 80.0, 45, 30.0, 'yellow')
    sunflower.show()
    print('[make sunflower grow, age and bloom]')
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print('[statistics for Sunflower]')
    show_statistics(sunflower)
    print('\n')
    print('=== Anonymous')
    new_plant = Plant.empty_plant()
    new_plant.show()
    print('[statistics for Unknown plant]')
    show_statistics(new_plant)
