class TechStack:
    def __init__(self, name: str, icon_url: str):
        self.__name = name
        self.__icon_url = icon_url

    @property
    def name(self) -> str:
        return self.__name

    @property
    def icon_url(self) -> str:
        return self.__icon_url

    @name.setter
    def name(self, value: str) -> None:
        self.__name: str = value

    @icon_url.setter
    def icon_url(self, value: str) -> None:
        self.__icon_url: str = value