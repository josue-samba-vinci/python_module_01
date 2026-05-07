class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height >= 0:
            self._height = height
        else:
            self._height = 0.0
        if age >= 0:
            self._age = age
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
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", -2, -2)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print()
    print("Current state: ", end="")
    rose.show()
