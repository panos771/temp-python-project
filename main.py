# main.py

"""Module DocString"""
from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    """Class DocString"""
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # self.sort_index = self.strength
        # cannot assign to field 'sort_index'
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self) -> str:
        return f'{self.name}, {self.job} ({self.age})'


person1 = Person("Geralt", "Footballer", 30, 99)
person2 = Person("John", "Painter", 25)
person3 = Person("John", "Painter", 25)
# person1.age = 12
# error: cannot assign to field 'age'

print(id(person2))
print(id(person3))
print(person1)

print(person3 == person2)
print(person1 > person2)
