import inspect
from position import EarthPosition, typename


# class decorators run once defined and once the module is imported
def auto_repr(cls):  # identity function, which return its arguments
    # print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)  # a dictionary representing member name vs member object
    # for name, member in members.items():
    #     print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    # print("__init__ parameter names: ", parameter_names)

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Can not apply auto_repr to {cls.__name__} because not "
            f"all __init__ parameters have matching properties"
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(name=name, value=getattr(self, name)) for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    # def __repr__(self):
        # return f"{typename(self)}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.name == other.name) and (self.position == other.position)

    def __hash__(self):
        return hash((self.name, self.position))


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
maracaibo = Location("Maracaibo", EarthPosition(54.44, 13.91))
rotterdam = Location("Rotterdam", EarthPosition(44.23, 17.22))
