def init (self, name, birth_date, occcupation, higher_education):
    self.name = name
    self.birth_date = birth_date
    self.occcupation = occcupation
    self.higher_education = higher_education

def str (self):
    return (f"Имя: {self.name}"
            f"Дата рождения: {self.birth_date}"
            f"Профессия: {self.occcupation}"
            f"Высшее образование: {'да' if self.higher_education else 'нет' }")
person1 = Person(
    name= "Иван Петров",
    birth_date= "1990-05-15",
    occupation= "Учитель",
    higher_education= True)

person2 = Person(
    name= "Елена Павловна",
    birth_date= "1990-05-16",
    occupation= "Пекарь",
    higher_education= False)
