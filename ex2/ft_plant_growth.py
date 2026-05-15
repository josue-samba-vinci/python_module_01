class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = round(age)

    def grow(self, height: float = 0.8) -> None:
        self._height = self._height + height

    def age(self, age: int = 1) -> None:
        self._age = age + self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    start_growth = plant1._height
    print("=== Garden Plant Growth ===")
    i = 1
    while i <= 7:
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
        i += 1
    growth = plant1._height - start_growth
    print(f"Growth this week: {growth:.1f}cm")
