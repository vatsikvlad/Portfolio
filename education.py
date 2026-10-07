class Education:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @name.setter
    def name(self, value: str) -> None:
        self.__name: str = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description: str = value
