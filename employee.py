from datetime import datetime, date
from collections import defaultdict


class Employee:
    def __init__(self, fname: str, lname: str, employid: int, hourly: float, overtime: float):
        self.fname = fname
        self.lname = lname
        self.employid = employid
        self.hourly = hourly
        self.overtime = overtime
        self.moods = defaultdict(list)

    def name(self):
        return f'{self.fname} {self.lname}'.title()

    def update_mood(self, today, mood):
        self.moods[today] = mood


if __name__ == '__main__':
    today = datetime.now().date()
    x = Employee('John', 'smith', 123123, 12.00, 14.00)
    print(x.fname)
    print(x.name())
    boolin = True
    while boolin:
        userinput = input(f'How are you feeling today ({today})')
        print(type(userinput))
        if userinput in ['1', '2', '3', '4', '5']:
            x.update_mood(today, userinput)
        elif userinput == 'q':
            boolin = False
        else:
            pass

    for key, val in x.moods.items():
        print(f'On {key} you happiness was a {val} on a scale of 1-5')
