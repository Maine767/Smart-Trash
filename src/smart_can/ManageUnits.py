from __init__ import Unit
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_squared_log_error

class Sensors(Unit):
    def __init__(self, unit_id: int = "Undefined", trash_type: str = "Undefined", number_type: str = int(0)) -> None:
        super().__init__(unit_id, trash_type)
        self.__number_type = None

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

    @property
    def number_type(self):
        self.__number_type = type(self.number_type)
    
    @number_type.setter
    def number_type(self, value):
        self.__number_type = type(value)
        

class MainControlUnit(Sensors):
    def __init__(self, unit_id: int = "Undefined", trash_type: str = "Undefined") -> None:
        super().__init__(unit_id, trash_type)

    def change_status(self, id, status):
        self._objects[id][0] = status
        print(f'Статус изменён на {status}')

    def check_fill_status(self, id) -> None:
        return self._objects[id][3]
        
    def average_fill(self, _logger):
        try:
            cursor = _logger.read_data('fillment')
            time = []
            avg_fill = []
            for item in cursor:
                time.append(item['timestamp'])
                counter = 0
                f = []
                for i in item:
                    if counter >= 2:
                        f.append(item[i]["fillment"])
                    counter += 1

                avg_fill.append(np.average(f))
            return time, avg_fill

        except Exception:
            
            raise f'np error'
    
    def new_chart(self, _logger):
        try:
            time, avg_fill = self.average_fill(_logger)

            if self.os == 'win32' or self.os == 'cygwin':
                path = self.path + "\static\images"
            else:
                path = self.path + "/static/images"


            x = np.arange(0, len(time)).reshape((-1, 1))
            y = np.array(avg_fill)
            y = np.nan_to_num(y)
            
            plt.figure(10)
            plt.plot(x, y)
            plt.xticks(rotation=90)
            plt.ylim(0, 1)
            plt.savefig(path + "/source.png", bbox_inches='tight')

            print("Графики построенны")
        
        except Exception:
            
            return f'Графики не удалось построить по причине: {Exception}'

    def evaluate(self, true, predicted):
        mae = mean_absolute_error(true, predicted)
        mse = mean_squared_error(true, predicted)
        rmse = np.sqrt(mean_squared_error(true, predicted))
        r2_square = r2_score(true, predicted)
        return mae, mse, rmse, r2_square

    def new_prediction(self, _logger):
        # try:
        time, avg_fill = self.average_fill(_logger)

        x = np.arange(0, len(time)).reshape((-1, 1))
        x_1 = np.arange(len(time), len(time) * 2).reshape((-1, 1))
        x_axis = np.row_stack([x, x_1])
        y = np.array(avg_fill)
        y = np.nan_to_num(y)

        if self.os == 'win32' or self.os == 'cygwin':
            path = self.path + "\static\images"
        else:
            path = self.path + "/static/images"

        plt.figure(1)
        model_1 = LinearRegression().fit(x, y)
        y_pred_1 = model_1.predict(x_1)
        y_axis_1 = np.concatenate([y, y_pred_1])
        print("-----------------Linear-----------------")
        print('Mean Absolute Error: ',self.evaluate(y, y_pred_1)[0])
        print('Mean Squared Error: ', self.evaluate(y, y_pred_1)[1])
        print('Root Mean Squared Error: ',self.evaluate(y, y_pred_1)[2])
        print('R2 Score: ',self.evaluate(y, y_pred_1)[3])
        plt.plot(x_axis, y_axis_1)
        plt.xticks(rotation=90)
        plt.savefig(path + "/predict_linear.png", bbox_inches='tight')

        plt.figure(2)
        model_2 = xgb.XGBRFRegressor().fit(x, y)
        y_pred_2 = model_2.predict(x_1)
        y_axis_2 = np.concatenate([y, y_pred_2])
        print("-----------------XGBR-----------------")
        print('Mean Absolute Error: ',self.evaluate(y, y_pred_2)[0])
        print('Mean Squared Error: ', self.evaluate(y, y_pred_2)[1])
        print('Root Mean Squared Error: ',self.evaluate(y, y_pred_2)[2])
        print('R2 Score: ',self.evaluate(y, y_pred_2)[3])
        plt.plot(x_axis, y_axis_2)
        plt.xticks(rotation=90)
        plt.savefig(path + "/XGB.png", bbox_inches='tight')

        plt.figure(3)
        model_3 = DecisionTreeRegressor().fit(x, y)
        y_pred_3 = model_3.predict(x_1)
        y_axis_3 = np.concatenate([y, y_pred_3])
        print("-----------------DesitionTree-----------------")
        print('Mean Absolute Error: ',self.evaluate(y, y_pred_3)[0])
        print('Mean Squared Error: ', self.evaluate(y, y_pred_3)[1])
        print('Root Mean Squared Error: ',self.evaluate(y, y_pred_3)[2])
        print('R2 Score: ',self.evaluate(y, y_pred_3)[3])
        plt.plot(x_axis, y_axis_3)
        plt.xticks(rotation=90)
        plt.savefig(path + "/desition_tree.png", bbox_inches='tight')
        print("Графики построенны")

        plt.figure(4)
        model_4 = RandomForestRegressor().fit(x, y)
        y_pred_4 = model_4.predict(x_1)
        y_axis_4 = np.concatenate([y, y_pred_4])
        print("-----------------RandomForest-----------------")
        print('Mean Absolute Error: ',self.evaluate(y, y_pred_4)[0])
        print('Mean Squared Error: ', self.evaluate(y, y_pred_4)[1])
        print('Root Mean Squared Error: ',self.evaluate(y, y_pred_4)[2])
        print('R2 Score: ',self.evaluate(y, y_pred_4)[3])
        plt.plot(x_axis, y_axis_4)
        plt.xticks(rotation=90)
        plt.savefig(path + "/randomforest.png", bbox_inches='tight')
        print("Графики построенны")


    
        # except Exception:
        #     return f'Графики не удалось построить по причине: {Exception}'