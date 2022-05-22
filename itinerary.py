from location import *
import functools


def post_condition(predicate):
    def function_decorator(f):

        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(f"Post-condition {predicate.__name__} not maintained for {self!r}")
            return result
        return wrapper
    return function_decorator


def at_least_two_locations(itinerary):
    return len(itinerary.locations) >= 2


class Itinerary:
    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    @post_condition(at_least_two_locations)
    def __init__(self, locations):
        self.__locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self.__locations)

    @property
    def locations(self):
        return tuple(self.__locations)

    @property
    def origin(self):
        return self.__locations[0]

    @property
    def destination(self):
        return self.__locations[-1]

    @post_condition(at_least_two_locations)
    def add(self, location):
        self.__locations.append(location)

    @post_condition(at_least_two_locations)
    def remove(self, name):
        removal_indexes = [
            index for index, location in enumerate(self.__locations) if location.name == name
        ]
        for index in reversed(removal_indexes):
            del self.__locations[index]

    @post_condition(at_least_two_locations)
    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self.__locations):
            if location.name == name:
                stop = index+1

        self.__locations = self.__locations[:stop]


trip = Itinerary.from_locations(hong_kong, stockholm)
