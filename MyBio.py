from datetime import *
class MyBio:
    _birthday: date = date(2007, 2, 6)

    @property
    def age(self) -> int:
        age: int = date.today().year - self._birthday.year - ((date.today().month, date.today().day) < (self._birthday.month, self._birthday.day))
        return age