class Contact:
    def __init__(self, name: str, image: str, link: str):
        self.__name = name
        self.__image = image
        self.__link = link

    @property
    def name(self) -> str:
        return self.__name

    @property
    def image(self) -> str:
        return self.__image

    @property
    def link(self) -> str:
        return self.__link

    @name.setter
    def name(self, value: str) -> None:
        self.__name: str = value

    @image.setter
    def image(self, value: str) -> None:
        self.__image: str = value

    @link.setter
    def link(self, value: str) -> None:
        self.__link: str = value
