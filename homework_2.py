class Person:
    def __init__(self, name: str, birth_date: int, occupation: str - "unemployed", higher_education: bool = False):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        return f"{self.name} was born in {self.birth_date}, works as a {self.occupation} and has higher education: {self.higher_education}"


class Classmate(Person):
    def __init__(self, name: str, birth_date: int, occupation: str = "unemployed", higher_education: bool = False, group_name: str = "unknown"):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        return f"{super().introduce()}, and is in group: {self.group_name}"

class Friend(Person):
    def __init__(self, name: str, birth_date: int, occupation: str = "unemployed", higher_education: bool = False, hobby: str = "unknown"):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        return f"{super().introduce()}, and has hobby: {self.hobby}"


