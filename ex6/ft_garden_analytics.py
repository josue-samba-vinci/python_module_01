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

    def grow(self, height: float = 30) -> None:
        self._height = round(self._height + height)
        self._stats._grow += 1

    def age(self, age: int = 20) -> None:
        self._age = age + self._age
        self._stats._age += 1

    def display_stats(self) -> None:
        self._stats.display(self._name)

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
                 bloom: bool = False, seeds: int = 0) -> None:
        super().__init__(name, height, age, color, bloom)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def grow_age_bloom(self) -> None:
        self.grow()
        self.age()
        self.bloom()
        self._stats._grow -= 1
        self._seeds += 42
        self._height += 30
        self._bloom = True
        print("[make sunflower grow, age and bloom]")


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
        self._stats._show += 1


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
    oak = Tree("Oak", 200, 365, 5)
    print("=== Tree")
    oak.show()
    oak._stats.display(oak._name)
    oak.produce_shade()
    oak._stats.display(oak._name)
    print("")
    sunflower = Seed("sunflower", 80, 45, "yellow")
    print("\n=== Seed")
    sunflower.show()
    sunflower.grow_age_bloom()
    sunflower.show()
    sunflower._stats.display(sunflower._name)
    print("\n=== Anonymous")
    anonymous = Plant.anonymous_plant()
    anonymous.show()
    anonymous._stats.display(anonymous._name)

