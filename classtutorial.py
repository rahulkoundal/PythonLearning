# """
# Class Tutorial
# """
#
#
# class FamilyMember:
#     count = 0
#
#     def name(self):
#         print("self", self)
#         self.count = self.count + 1
#         print("count variable values =", self.count)
#
#
# # obj = FamilyMember()
# #
# # print(obj)
# #
# # print(type(obj))
# #
# # print(dir(obj))
# #
# # obj.name()
# #
# # obj.name()
#
#
# class JuniorFamily(FamilyMember):
#     l = 0
#
#     def test(self):
#         print(self)
#         self.l = self.l + 2
#         print("my name is rahul")
#
#
# obj = JuniorFamily()
# print(dir(obj))
#



#
#
#
#
#
#
#


class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

        # public member function

    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()
