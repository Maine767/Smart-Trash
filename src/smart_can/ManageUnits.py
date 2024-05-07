from __init__ import Unit
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class Sensors(Unit):
    def __init__(self, unit_id: int = "Undefined", trash_type: str = "Undefined", number_type: str = int(0)) -> None:
        super().__init__(unit_id, trash_type)
        self.__number_type = type(number_type)

    def check_fill_percentage(self, id, step):
        cur_am_of_trash = self._objects[id][5]
        max_am_of_trash = self._objects[id][4]

        if cur_am_of_trash + step < max_am_of_trash:
            cur_am_of_trash += step
            self._objects[id][3] = cur_am_of_trash / max_am_of_trash

            print(f'Теперь мусорка загружена на {round(self._objects[id][3] * 100, 2)}%')

            return cur_am_of_trash
        else:
            print("Вы привысили допустимое место!")
            return -1
    
    def set_trash(self, id, step) -> None:

        if not isinstance(step, self.__number_type):
            raise ValueError("Invalid Data type")
        
        status = self.check_fill_percentage(id, step)

        if status != -1:
            self._objects[id][5] = status
        
        print(f'Теперь здесь находиться {status} {self._trash_type} ')
    
    def get_trash(self, id):
        return self._objects[id][5]

    def set_max(self, id, amount) -> None:
        self._objects[id][4] = amount
        
        print(f"Вы задали ограничение равное = {amount}")

    def set_number_type(self, number_type):
        self.__number_type = type(number_type)
        

class MainControlUnit(Sensors):
    def __init__(self, unit_id: int = "Undefined", trash_type: str = "Undefined") -> None:
        super().__init__(unit_id, trash_type)

    def change_status(self, id, status):
        self._objects[id][0] = status
        print(f'Статус изменён на {status}')

    def check_fill_status(self, id) -> None:
        return self._objects[id][3]
        
    def new_charts(self, _logger):
        try:
            cursor = _logger.read_data('fillment')
            time = []
            avg_fill = []

            if self.os == 'win32' or self.os == 'cygwin':
                path = self.path + "\static\images"
            else:
                path = self.path + "/static/images"

            for item in cursor:
                time.append(item['timestamp'])
                counter = 0
                f = []
                for i in item:
                    if counter >= 2:
                        f.append(item[i]["fillment"])
                    counter += 1

                avg_fill.append(np.average(f))

            x = np.arange(0, len(time)).reshape((-1, 1))
            y = np.array(avg_fill)
            
            plt.plot(x, y)
            plt.xticks(rotation=90)
            plt.ylim(0, 1)
            plt.savefig(path + "/source.png", bbox_inches='tight')

            model = LinearRegression().fit(x, y)
            x = np.arange(len(time), len(time) * 2).reshape((-1, 1))
            y_pred = model.predict(x)
            plt.plot(x, y_pred)
            plt.xticks(rotation=90)
            plt.savefig(path + "/predict.png", bbox_inches='tight')

            return "Графики построенны"
        
        except Exception:

            return f'Графики не удалось построить по причине: {Exception}'