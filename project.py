class Project:
    def __init__(self, title: str, description: str, link: str, images: list[str] | None = None):
        self.__title = title
        self.__description = description
        self.__link = link
        self.__images = images if images is not None else []

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def link(self) -> str:
        return self.__link

    @property
    def images(self) -> list[str]:
        return self.__images

    @title.setter
    def title(self, value: str) -> None:
        self.__title: str = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description: str = value

    @link.setter
    def link(self, value: str) -> None:
        self.__link: str = value

    @images.setter
    def images(self, value: list[str] | None) -> None:
        self.__images: list[str] = value if value is not None else []
