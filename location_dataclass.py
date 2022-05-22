from dataclasses import dataclass
from position import Position, EarthPosition


# this class decorator collects those class attributes and make a synthesized implementation for
# __init__ with those parameters and __repr__
@dataclass(init=True, frozen=True)
class Location:
    name: str
    position: Position

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Location name cannot be empty!")


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
maracaibo = Location("Maracaibo", EarthPosition(54.44, 13.91))
rotterdam = Location("Rotterdam", EarthPosition(44.23, 17.22))
