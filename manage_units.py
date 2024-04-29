from trash import BottleTrash, PaperTrash

class Sensor(BottleTrash, PaperTrash):
    def __init__(self, trash_id: int = "Undefined", status: bool = False, fill_percentage: float = 0, coordinates: str = "Undefined", amount_bottles: int = 0) -> None:
        super().__init__(trash_id, status, fill_percentage, coordinates, amount_bottles)
    
    def connect(id):
        print(f"Вы подключились к объекту с номером: {id}")

class MainControlUnit(Sensor):
    def __init__(self, trash_id: int = "Undefined", status: bool = False, fill_percentage: float = 0, coordinates: str = "Undefined", amount_bottles: int = 0) -> None:
        super().__init__(trash_id, status, fill_percentage, coordinates, amount_bottles)

    def change_status(self, status):
        self.__status = status
        print(f'Статус изменён на {status}')