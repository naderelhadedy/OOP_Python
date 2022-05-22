# import module
import bic_code


class Car:
    next_model_num = 1
    HEIGHT = 200
    WIDTH = 800

    # static method is associated with the class not instance, NO self here
    # Act as a private method that will not be used outside the scope
    @staticmethod
    def _generate_model_number():
        result = Car.next_model_num
        Car.next_model_num += 1
        return result

    @staticmethod
    def _generate_bic_code(name, number):
        return bic_code.create_bic_code(name=name, number=number)

    # Named constructor, creates an object of the class, which in turn invokes the __init__ constructor
    @classmethod
    def create_empty(cls, name, length, **kwargs):
        return cls(name, length, **kwargs)

    # when we call it with the class name, the class object is passed through the cls argument
    @classmethod
    def reset_model_number(cls):
        cls.next_model_num = 1

    def __init__(self, name, length, **kwargs):
        self.name = name
        self.length = length
        self.model_num = Car._generate_model_number()
        self.bic = self._generate_bic_code(name=self.name, number=self.model_num)
        # We can access next_model_num with self
        # but if we said self.next_model_num, this will add a new instance attribute for the object

    @property
    def volume(self): # now it becomes a template method
        return self._calc_volume()

    def _calc_volume(self):
        return Car.HEIGHT * Car.WIDTH * self.length


# static method with inheritance
class BmwCar(Car):
    MAX_TEMP = 70.0
    UNWANTED_VOLUME = 10000

    # override base class initializer
    def __init__(self, name, length, *, temp, **kwargs):  # temp is a keyword-only argument due to inserting a star before
        super().__init__(name, length, **kwargs)
        # this check is done by setter property
        # if temp > BmwCar.MAX_TEMP:
            # raise ValueError('Temp is high!')
        # self._temp = temp
        self.temp = temp

    # @property
    # def volume(self):
       #  # return Car.HEIGHT * Car.WIDTH * self.length - BmwCar.UNWANTED_VOLUME
      #   return super().volume - BmwCar.UNWANTED_VOLUME

    # overriding the baseclass method
    def _calc_volume(self):
        return super()._calc_volume() - BmwCar.UNWANTED_VOLUME

    @staticmethod
    def _c_to_f(temp):
        return temp * 9 / 5 + 32

    @staticmethod
    def _f_to_c(temp):
        return (temp - 32) * 5 / 9

    @property
    def temp_f(self):
        return BmwCar._c_to_f(self.temp)

    @temp_f.setter
    def temp_f(self, value):
        self.temp = BmwCar._f_to_c(value)

    # getter >> call it like object_name.temp
    @property
    def temp(self):
        return self._temp

    # setter >> call it like object_name.temp = value
    @temp.setter
    def temp(self, value):
        return self._set_temp(value)
        # if value > BmwCar.MAX_TEMP:
        #     raise ValueError('Temp is high!')
        # self._temp = value

    def _set_temp(self, value):
        if value > BmwCar.MAX_TEMP:
            raise ValueError('Temp is high!')
        self._temp = value

    # override the static method
    @staticmethod
    def _generate_bic_code(name, number):
        return bic_code.create_bic_code(name=name, number=number, year=2020)


class BmwModel(BmwCar):
    MIN_TEMP = 10

    # @BmwCar.temp.setter
    # def temp(self, value):
    #     if not (BmwModel.MIN_TEMP <= value <= BmwCar.MAX_TEMP):
    #         raise ValueError('Temperature out of range!')
    #     self._temp = value

    # overriding the baseclass method
    def _set_temp(self, value):
        if value < BmwModel.MIN_TEMP:
            raise ValueError('Temperature too cold!')
        super()._set_temp(value)
