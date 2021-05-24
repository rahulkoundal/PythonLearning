"""
Private inheritance
"""


class Parents:
    surname = 'Koundal'     # Public Field
    __parentsname = 'Chander'   # Private Field
    _parentsaccount = 2         # PROTECTED FIELD

    def rooms(self):
        self.surname = self.surname + 's'
        self.__parentsname = self.__parentsname + 'k'
        self._parentsaccount = self._parentsaccount
        print(self.surname, self.__parentsname, self._parentsaccount)


# obj = Parents()
#
# obj.rooms()
# obj.__parentsname  # accessing private Field or attribute outside the class
#
# obj.surname   # accessing public Field or attribute-  outside class
#
# obj._parentsaccount # accessing protected Field or attribute-  outside class


class Children(Parents):

    def mybody(self):
        print("romss", self.rooms())
        print("sss", self._parentsaccount)


obj = Children()

print(type(obj))

print(dir(obj))
obj.mybody()
