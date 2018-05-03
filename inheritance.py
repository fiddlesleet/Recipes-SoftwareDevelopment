class Parent():
    def __init__(self, last_name, eye_color):
        print("In parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print("In child constructor")
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys

parent = Parent("Blob", "purple")
print(parent.last_name)

kid = Child("Blobly", "green", "all of them")
print(kid.last_name)
print(kid.eye_color)
print(kid.toys)
