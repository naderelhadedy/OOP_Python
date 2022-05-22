class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f'Latitude {latitude} out of range!')
        if not (-180 <= longitude <= +180):
            raise ValueError(f'Longitude {longitude} out of range!')

        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    # make it in the form of a constructor call
    def __repr__(self):
        # return f"{self.__class__.__name__} -> lat:{self.latitude} lon:{self.longitude}"
        # the class of an object is the same as the type of an object
        # results this > Position(latitude=-40, longitude=120)
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

        # how to call
        # x1 = Position(-40, 120)
        # x2 = repr(x1) # repr, str, format are similar
        # x3 = eval(x2)

    def __str__(self):  # it's called when using print
        return format(self)
        # return (
        #     f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
        #     f"{abs(self.longitude)}° {self.longitude_hemisphere}"
        # )

    def __format__(self, format_spec):  # used with format string method and f"{}"
        component_format_spec = '.2f'
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"

        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}° {self.latitude_hemisphere}, "
            f"{longitude}° {self.longitude_hemisphere}"
        )
        # call it by format(object, '.3')
        # x1 = Position(-20.3232, 100.26257)
        # f'{x1:.1}', f'{x1!r}', f'{x1!s}', f'{x1=}'


def typename(obj):
    return type(obj).__name__


class EarthPosition(Position):
    pass
