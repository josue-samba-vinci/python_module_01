class Plant: 
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def grow(self) -> int:
        self._height += 0.8

    def age(self) -> int:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")    
    i = 1
    while i <= 7:
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
        i += 1
