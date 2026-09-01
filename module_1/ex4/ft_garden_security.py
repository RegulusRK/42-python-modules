class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth: float) -> None:
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth = growth

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

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, {self._days} days old"
            )


if __name__ == "__main__":
    print('=== Garden Security System ===')
    rose = Plant('Rose', 15, 10, 0.0)
    print('Plant created: ', end='')
    rose.show()
    print('\n')

    rose.set_height(25)
    print(f'Height updated: {rose.get_height()}cm')
    rose.set_age(30)
    print(f'Age updated: {rose.get_age()} days')

    print('\n')

    rose.set_height(-20)
    rose.set_age(-20)

    print('Current state: ', end='')
    rose.show()

