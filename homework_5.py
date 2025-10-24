class Distance:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"value = {self.value}; \nunit = {self.unit}"

    def __add__(self, obj):
        try:
            if self.unit == obj.unit:
                new_obj = Distance(value = self.value + obj.value, unit = self.unit)
                return new_obj
            else:
                return "у атрибутов должна быть еденица измерения"
        except AttributeError:
            return "Проверьте что оба атрибута являются обьектами на основекласса Money"
        except:
            return "Произошла ошибка, проверьте вводимые данные"

    def __sub__(self, obj):
        try:
            if self.unit == obj.unit:
                new_obj = Distance(value = self.value - obj.value, unit = self.unit)
                if new_obj.value < 0 :
                    raise ValueError ("Расстояние не может быть отрицательным")
                return new_obj
            else:
                return


