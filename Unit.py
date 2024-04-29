import ssl
import certifi
import geopy.geocoders
from abc import ABC, abstractmethod
from geopy.distance import great_circle
from geopy.geocoders import Nominatim

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

class address_of_sensor():
    def __init__(self, coordinates: str = None) -> str:
        self.__geolocator = Nominatim(user_agent="Trash_geo")

        try:
            self.__location = self.__geolocator.reverse(coordinates)
        except Exception:
            self.__location = "Undefined"

    def get_location(self) -> str:
        if self.__location != "Undefined":
            location = self.__location.address

        return location


class Unit(ABC):
    def __init__(self, unit_id: int = "Undefined", trash_type: str = "Undefined") -> None:
        self.__unit_id = unit_id
        self._trash_type = trash_type
        self._objects = dict()

    @abstractmethod
    def set_number_type(self, number_type):
        None

    @abstractmethod
    def get_trash(self):
        None

    @abstractmethod
    def set_trash(self):
        None

    def add_new_sensor(self):
        id = len(self._objects) + 1
        self._objects[id] = [False, "None", 0, None, None, 0]

        print(f'Вы создали {id} сенсор')

    def set_address(self, id, coordinates):
        location = address_of_sensor(coordinates).get_location()
        self._objects[id][2] = location

        print(f'Вы задали локацию: {location}')

    def get_unit_id(self):
        print(f"Вы находитесь в юните {self.__unit_id}")
        return self.__unit_id
    
    def get_object(self, id):
        return self._objects[id]
    
    def get_object(self):
        return self._objects
