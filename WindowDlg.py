class WindowDlg:
    def __init__(self, title, width = None, height = None):
        self.__title = title
        self.__width = width
        self.__height = height
    
    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) is int and 0 <= width <= 10000:
            if self.__width:
                self.show()
            self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if type(height) is int and 0 <= height <= 10000:
            if self.__height:
                self.show()
            self.__height = height
    