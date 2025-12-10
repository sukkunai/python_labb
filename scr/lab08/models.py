from datetime import datetime, date
from dataclasses import dataclass


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверный формат даты")
        
        if date.today().year < int(self.birthdate.split('-')[0]):
            raise ValueError('Год рождения больше нынешнего')
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должен быть [0,5]")
        
    def age(self) -> int:
        '''возвращает количество полных лет'''
        today = date.today()
        birth_year, birth_month, birth_day = map(int, self.birthdate.split('-'))
        age = today.year - birth_year
        
        if (today.month, today.day) < (birth_month, birth_day):
            age -= 1
        return age
    
    def to_dict(self) -> dict:
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fio=data['fio'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=data['gpa']
        )
    
    def __str__(self):
        '''красивый вывод'''
        return f'ФИО студента: {self.fio}\n Дата рождения: {self.birthdate}\n Возраст: {self.age()}\n Группа: {self.group}\n GPA: {self.gpa}'