class Car:
    def __init__(self, model = None):
        self.__model = model
    
    def get_model(self):
        return self.__model
    def set_model(self, model):
        if type(model) is str and 2 <= len(model) <= 100:
            self.__model = model

    model = property(get_model, set_model)
car = Car()
car.model = "Toyota"
print(car.model)

# @property
# def model(self):
#     return self.__model
# @model.setter
# def model(self, model):
#     if type(model) is str and 2 <= len(model) <= 100:
#             self.__model = model
