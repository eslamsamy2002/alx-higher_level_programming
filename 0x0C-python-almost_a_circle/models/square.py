#!/usr/bin/python3
"""sqaure"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.height}"
    
    @property
    def size(self):
        """getter"""

        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = self.width
    
    def update(self, *args, **kwargs):
        """update"""

        if args:

            att_list = ["id", "size", "x", "y"]
            for i , value in enumerate(args):
                setattr(self, att_list[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is not attribute in this class")










