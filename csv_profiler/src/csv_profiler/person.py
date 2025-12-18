class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        assert 0 <= value <= 200
        self._age = value

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


if __name__ == "__main__":
    person1 = Person("wael", 21)
    person2 = Person("wael", 21)

    print(person1 == person2)