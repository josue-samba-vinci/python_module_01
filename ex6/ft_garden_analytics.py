class Plant:
    class _Stats:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0

        def display(self, name) -> None:
            print(f" [statistics for {name}]")
            print(f"Stats: {self._grow} grow, {self._age} age, {self._show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height >= 0:
            self._height = round(height, 1)
        else:
            self._height = 0.0
        if age >= 0:
            self._age = round(age)
        else:
            self._age = 0
        self._stats = Plant._Stats()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height:.1f}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    @staticmethod
    def is_older(age: int) -> bool:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
            return True
        print(f"Is {age} days more than a year? -> False")
        return False

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def display_stats(self) -> None:
        self._stats.display(self._name)


class Flower (Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 bloom: bool = False) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = bloom

    def bloom(self) -> None:
        self._stats._grow += 1
        self._bloom = True
        print(f"[asking the {rose._name.lower()} to bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        self._stats._show += 1
        if self._bloom:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed (Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 bloom: bool = False) -> None:
        super().__init__(name, height, age, color, bloom)
        self._seeds


class Tree (Plant):
    class _Stats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self._shade = 0

        def display(self, name) -> None:
            super().display(name)
            print(f" {self._shade} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = round(trunk_diameter, 1)
        self._stats = Tree._Stats()

    def produce_shade(self) -> None:
        self._stats._shade += 1
        print(f"[asking the {self._name} to produce shade]\n" +
              f"Tree Oak now produces a shade of {self._height:.1f}cm long" +
              f"and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f} cm")


class Vegetables (Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None: 
        print("=== Vegetable")
        super().show()
        print(f"Harvest season: {self._harvest_season}\n" +
              f"Nutritional value: {self._nutritional_value}")
      
    def set_nutritional_value(self, nutritional_value: int = 20) -> None:
        self._nutritional_value = nutritional_value

    def grow_and_age(self, height: int = 42, age: int = 20) -> None:
        self._height = self._height + height
        self._age = self._age + age
        self._nutritional_value = self._nutritional_value + age
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    Plant.is_older(30)
    Plant.is_older(366)
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose._stats.display(rose._name)
    rose.bloom()
    rose.show()
    rose._stats.display(rose._name)


    print("")
    print("")
    print("")
    print("")
    oak = Tree("Oak", 200, 365, 5)
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    tomato = Vegetables("tomato", 5, 10, "April", 0)
    tomato.show()
    tomato.grow_and_age()
