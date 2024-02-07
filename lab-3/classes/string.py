from typing import Union


class StringOperator:
    __string: Union[str, None] = None

    @property
    def string(self):
        return self.__string

    def getString(self):
        self.__string = input("Enter a string: ")
        return self.__string
    
    def printString(self):
        print(self.__string.upper())

obj = StringOperator()
obj.getString()
obj.printString()
