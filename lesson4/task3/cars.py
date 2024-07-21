class Cars:

    def __init__(self, vin_number, name_model):  
        self.vin_number = vin_number
        self.name_model = name_model

    #Запуск двигателя
    def engine_starting(self):                
        print("Двигатель запустился")
    
    def turn_engine(self):                
        print("Двигатель заглушен")

    #Начать движение
    def drive(self):
        print('Машина едет вперед')

    def reverse(self):
        print('Машина едет назад ')
        
    #Получить информацию
    def get_info(self):
        print(f'VIN номер: {self.vin_number}\nНазвание модели: {self.name_model}')