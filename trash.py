import ssl
import certifi
import geopy.geocoders
from abc import ABC, abstractmethod
from geopy.distance import great_circle
from geopy.geocoders import Nominatim

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

class address_of_trash():
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


class Trash(ABC):
    def __init__(self, unit_id: int = "Undefined", status: bool = False, trash_type: str = "Undefined",
                  coordinates: str = None, fill_percentage: float = 0) -> None:
        self.__unit = unit_id
        self.__status = status
        self.__trash_type = trash_type
        self.__address = address_of_trash(coordinates)
        self.__fill_percentage = fill_percentage

    @abstractmethod
    def check_fill_status(self) -> None:
        if self.fill_percentage >= 80:
            return "Мусорка заполнена на 80% или более. Необходимо опустошить."

    @abstractmethod
    def get_trash(self):
        None

    @abstractmethod
    def set_trash(self):
        None

    def get_status(self):
        return self.__status

    def get_trash_type(self):
        return self.__trash_type
    
    def get_address(self):
        return self.__address

    def get_fill_percentage(self):
        return self.__fill_percentage

    def find_nearest_trash(self, all_cans):
        current_coordinates = (self.address['latitude'], self.address['longitude'])
        nearest_trash = None
        nearest_distance = float('inf')

        for can in all_cans:
            if can.trash_id != self.trash_id:
                trash_coordinates = (can.address['latitude'], can.address['longitude'])
                distance = great_circle(abs(current_coordinates, trash_coordinates))

                if distance < nearest_distance:
                    nearest_trash = can
                    nearest_distance = distance

        return nearest_trash.get_address() if nearest_trash else None


class BottleTrash(Trash):
    def __init__(self, trash_id: int = "Undefined", status: bool = False, fill_percentage: float = 0, 
                 coordinates: str = "Undefined", amount_bottles: int = 0) -> None:
        super().__init__(trash_id, "Bottle", status, coordinates, fill_percentage)
        self.__bottle_count = amount_bottles
        self.__max_bottles = 50

    def check_fill_status(self) -> None:
        if self.fill_percentage >= 80:
            return "Мусорка заполнена на 80% или более. Необходимо опустошить."

    def display_message(self):
        return "Как ты помогаешь этому миру, выкинув так много бутылок"
    
    def get_trash(self):
        return self.__bottle_count
    
    def set_trash(self, amount):
        if self.__bottle_count + amount < self.__max_bottles:
            self.__bottle_count += amount
            return self.__bottle_count
        else:
            return "It's overwhelm"


class PaperTrash(Trash):
    def __init__(self, trash_id, status, fill_percentage, coordinates, amount_bottles: int = 0) -> None:
        super().__init__(trash_id, "Paper", status, coordinates, fill_percentage)
        self.__kilogramms = 0
        self.__max_killogramms = 10

    def check_fill_status(self) -> None:
            if self.fill_percentage >= 80:
                return "Мусорка заполнена на 80% или более. Необходимо опустошить."
            
    def display_message(self):
        return "Как ты помогаешь этому миру, выкинув так много бумаги"

    def get_trash(self):
        return self.__kilogramms
    
    def set_trash(self, amount):
        if self.__kilogramms + amount < self.__max_killogramms:
            self.__kilogramms += amount
            return self.__kilogramms
        else:
            return "It's overwhelm"