class Plant:
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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm")
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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower (Plant):
    def __init__(self, name: str, height: float, age: int, color: str, bloom: bool = False) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = bloom

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True

    def show(self) -> None:   
        print("=== Flower\n")
        super().show()
        if self._bloom:
            print("Rose has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree (Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = round(trunk_diameter, 1)

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]\n" +
              f"Tree Oak now produces a shade of {self._height}cm long" +
              f"and {self._trunk_diameter}cm wide.")

    def show(self) -> None:   
        print("=== Tree\n")
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")


class Vegetables (Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None: 
        print("=== Vegetable\n")
        super().show()
        print(f"Harvest season: {self._harvest_season}" +
              f"Nutritional value: {self._nutritional_value}")
      
    def set_nutritional_value(self, nutritional_value: int = 20) -> None:
        self._nutritional_value = nutritional_value

    def grow_and_age(self, height: int = 42, age: int = 20) -> None:
        self._height = self._height + height
        self._age = self._age + age
        super().show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._age}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()
    tomato = Vegetables("tomato", 5, 10, "April", 0)
    tomato.grow_and_age()
