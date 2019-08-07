class Object:
    """
    This is a test class.
    """
    def __init__(self, name="no_name"):
        self.name= name

class Object2:
    def __init__(self, name="no_name"):
        self.name=name

list_of_objects = []

a = Object("A")
b = Object2("B")
c = Object("C")
d = Object("D")

list_of_objects.append(a)
list_of_objects.append(b)
list_of_objects.append(c)

if a in list_of_objects:
    print("True")